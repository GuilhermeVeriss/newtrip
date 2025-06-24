from datetime import datetime
import re

## FUNÇÕES PARA MANIPULAÇÃO DE RESERVAS

def buscar_reserva(value, database, by='id'):
    """Busca uma reserva específica por ID, nome, CPF ou outro campo."""
    lista = database.data.get('reservas', [])

    for reserva in lista:
        if reserva.get(by) == value:
            return reserva
    return None


def listar_reservas(database):
    """Exibe todas as reservas de forma formatada e organizada."""
    lista = database.data.get('reservas', [])

    if not lista:
        print("Nenhuma reserva encontrada.")
        return
    for i, reserva in enumerate(lista, start=1):
        print("=" * 42)
        print(f"RESERVA #{i}")
        print("=" * 42)

        # Cliente
        nome = reserva.get("nome_cliente", "N/A")
        cpf = reserva.get("cpf_cliente", "")
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if len(cpf) == 11 else cpf
        email = reserva.get("email", "N/A")
        telefone = reserva.get("telefone", "N/A")
        
        # Destino
        destino = reserva.get("destino", "N/A")
        hotel = reserva.get("hotel", "N/A")
        tipo_quarto = reserva.get("tipo_quarto", "N/A")

        # Datas
        checkin = reserva.get("data_entrada", "N/A")
        checkout = reserva.get("data_saida", "N/A")
        criacao = reserva.get("data_criacao", "N/A")
        
        def formatar_data(data):
            return f"{data[8:10]}/{data[5:7]}/{data[:4]}" if len(data) == 10 else data
        checkin = formatar_data(checkin)
        checkout = formatar_data(checkout)
        criacao = formatar_data(criacao)

        # Valor
        valor = reserva.get("preco_total", 0)
        valor_formatado = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Status
        status_reserva = reserva.get("status_reserva", "indefinido").capitalize()
        status_pagamento = reserva.get("status_pagamento", "indefinido").capitalize()

        # Impressão formatada
        print(f"Cliente: {nome} (CPF: {cpf_formatado})")
        print(f"Email: {email}")
        print(f"Telefone: {telefone}\n")

        print(f"Destino: {destino}")
        print(f"Hotel: {hotel}")
        print(f"Tipo de Quarto: {tipo_quarto}\n")

        print(f"Check-in: {checkin}")
        print(f"Check-out: {checkout}")
        print(f"Valor Total: {valor_formatado}\n")

        print(f"Status da Reserva: {status_reserva}")
        print(f"Status do Pagamento: {status_pagamento}")
        print(f"Data de Criação: {criacao}")
        print("=" * 42)


def criar_reserva(nova_reserva, database):
    """Cria uma nova reserva com validações completas."""
    
    # Validação de campos essenciais não vazios
    campos_obrigatorios = ["destino", "hotel", "tipo_quarto", "data_entrada", "data_saida", 
                             "preco_total", "nome_cliente", "cpf_cliente", "email"]
    for campo in campos_obrigatorios:
        if campo not in nova_reserva or not nova_reserva[campo]:
            print(f"Erro de Validação: O campo '{campo}' é obrigatório e não pode estar vazio.")
            return None
        
    # Validação do tipo de quarto
    tipos_quarto_validos = ['Standard', 'Deluxe', 'Suite']
    if nova_reserva['tipo_quarto'] not in tipos_quarto_validos:
        print(f"Erro de Validação: Tipo de quarto '{nova_reserva['tipo_quarto']}' é inválido. Válidos: {tipos_quarto_validos}")
        return None
    
    # Validação das datas
    try:
        data_atual = datetime.now().date()
        data_entrada = datetime.strptime(nova_reserva['data_entrada'], '%Y-%m-%d').date()
        data_saida = datetime.strptime(nova_reserva['data_saida'], '%Y-%m-%d').date()

        if data_entrada < data_atual:
            print(f"Erro de Validação: A data de entrada ({data_entrada.strftime('%d/%m/%Y')}) não pode ser anterior à data atual ({data_atual.strftime('%d/%m/%Y')}).")
            return None
        if data_saida <= data_entrada:
            print(f"Erro de Validação: A data de saída ({data_saida.strftime('%d/%m/%Y')}) deve ser posterior à data de entrada ({data_entrada.strftime('%d/%m/%Y')}).")
            return None
    except ValueError:
        print("Erro de Validação: Formato de data inválido. Use 'YYYY-MM-DD'.")
        return None
    
    # Validação do CPF
    cpf = nova_reserva['cpf_cliente']
    if not cpf.isdigit() or len(cpf) != 11:
        print(f"Erro de Validação: CPF '{cpf}' é inválido. Deve conter exatamente 11 dígitos numéricos.")
        return None

    # Validação do Email
    email = nova_reserva['email']
    if not re.search(r"@[^@]+", email):
        print(f"Erro de Validação: Formato de email '{email}' é inválido.")
        return None

    # Validação do Preço
    try:
        preco = float(nova_reserva['preco_total'])
        if preco <= 0:
            print(f"Erro de Validação: O preço total ({preco}) deve ser maior que zero.")
            return None
    except (ValueError, TypeError):
        print("Erro de Validação: O preço total deve ser um número válido.")
        return None
    
    reserva_final = database.criar(nova_reserva, 'reservas')
    
    return reserva_final


def atualizar_reserva(dicionario, id, database):
    """Atualiza uma reserva existente com validações."""
    
    # Buscar a reserva pelo ID
    reserva = database.buscar(id, 'reservas', by='id')
    if not reserva:
        print(f"Reserva com ID {id} não encontrada.")
        return None

    # Não permitir alteração de reservas finalizadas
    if reserva.get("status_reserva") == "finalizada":
        print("Reservas finalizadas não podem ser alteradas.")
        return None

    # Prevenir alteração de campos proibidos
    if "cpf_cliente" in dicionario:
        print("O campo 'cpf_cliente' não pode ser alterado.")
        dicionario.pop("cpf_cliente")

    if "id" in dicionario:
        print("O campo 'id' não pode ser alterado.")
        dicionario.pop("id")

    # Validações
    hoje = datetime.today().date()

    if "data_entrada" in dicionario:
        try:
            entrada = datetime.strptime(dicionario["data_entrada"], "%Y-%m-%d").date()
            if entrada < hoje:
                print("A data de entrada deve ser hoje ou no futuro.")
                return None
        except ValueError:
            print("Formato inválido para data de entrada. Use 'YYYY-MM-DD'.")
            return None

    if "data_saida" in dicionario:
        try:
            saida = datetime.strptime(dicionario["data_saida"], "%Y-%m-%d").date()
            entrada = datetime.strptime(
                dicionario.get("data_entrada", reserva["data_entrada"]), "%Y-%m-%d"
            ).date()
            if saida <= entrada:
                print("A data de saída deve ser posterior à data de entrada.")
                return None
        except ValueError:
            print("Formato inválido para data de saída. Use 'YYYY-MM-DD'.")
            return None

    if "email" in dicionario and "@" not in dicionario["email"]:
        print("E-mail inválido. Deve conter '@'.")
        return None

    if "preco_total" in dicionario:
        try:
            preco = float(dicionario["preco_total"])
            if preco <= 0:
                print("Preço total deve ser maior que zero.")
                return None
        except ValueError:
            print("Preço total inválido. Deve ser um número.")
            return None

    # Validação dos status
    if "status_pagamento" in dicionario and dicionario["status_pagamento"] not in ["pendente", "pago", "cancelado"]:
        print("Status de pagamento inválido.")
        return None

    if "status_reserva" in dicionario and dicionario["status_reserva"] not in ["confirmada", "cancelada", "finalizada"]:
        print("Status de reserva inválido.")
        return None

    return database.atualizar(dicionario, 'reservas', id)


def deletar_reserva(id, database):
    """Deleta uma reserva com verificações de segurança."""
    
    reserva = buscar_reserva(id, database, by='id')
    if not reserva:
        print(f"Reserva com ID {id} não encontrada.")
        return None

    # Verificar se a reserva pode ser deletada
    if reserva.get("status_reserva") == "finalizada":
        print("Reservas finalizadas não podem ser deletadas.")
        return None
    
    return database.deletar('reservas', id)


def buscar_por_filtros(lista, **filtros):
    """Busca reservas aplicando múltiplos filtros simultaneamente."""
    # TODO: Implementar busca com múltiplos filtros
    pass

