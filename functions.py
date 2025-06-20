import database
from datetime import datetime


## FUNÇÕES PARA MANIPULAÇÃO DE RESERVAS

# TODO: TASK 5 - IMPLEMENTAR BUSCAR RESERVA
def buscar_reserva(value, lista, by='id'):
    """
    TASK 5 - BUSCAR RESERVA (PRIORIDADE: ALTA)
    
    Wrapper da função database.buscar() específica para reservas.
    
    PARÂMETROS:
    - value: valor a ser buscado
    - lista: lista de reservas
    - by: campo para busca ('id', 'nome_cliente', 'cpf_cliente', 'destino', etc.)
    
    RETORNO:
    - Dicionário da reserva encontrada ou None
    
    IMPLEMENTAÇÃO SUGERIDA:
    return database.buscar(value, lista, by)
    """
    # TODO: Implementar usando database.buscar()
    pass


# TODO: TASK 6 - IMPLEMENTAR LISTAR RESERVAS
def listar_reservas(lista):
    """
    TASK 6 - LISTAR RESERVAS (PRIORIDADE: ALTA)
    
    Exibe todas as reservas de forma formatada e organizada.
    
    FORMATO SUGERIDO:
    ==========================================
    RESERVA #1
    ==========================================
    Cliente: João Silva (CPF: 123.456.789-01)
    Email: joao.silva@email.com
    Telefone: (11) 99999-9999
    
    Destino: Rio de Janeiro, RJ
    Hotel: Hotel Copacabana Palace
    Tipo de Quarto: Standard
    
    Check-in: 20/06/2025
    Check-out: 25/06/2025
    Valor Total: R$ 1.250,00
    
    Status da Reserva: Confirmada
    Status do Pagamento: Pendente
    Data de Criação: 17/06/2025
    ==========================================
    
    TRATAMENTOS:
    - Lista vazia: "Nenhuma reserva encontrada."
    - Formatar CPF: XXX.XXX.XXX-XX
    - Formatar datas: DD/MM/AAAA
    - Formatar valores: R$ X.XXX,XX
    - Capitalizar status
    """
    if not lista:
        print("Nenhuma reserva encontrada.")
        return
    for i, reserva in enumerate(lista, start=1):
        print("=" * 42)
        print(f"RESERVA #{i}")
        print("=" * 42)

        # Cliente
        nome = reserva.get("cliente", {}).get("nome", "N/A")
        cpf = reserva.get("cliente", {}).get("cpf", "")
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if len(cpf) == 11 else cpf
        email = reserva.get("cliente", {}).get("email", "N/A")
        telefone = reserva.get("cliente", {}).get("telefone", "N/A")
        
        # Destino
        destino = reserva.get("destino", "N/A")
        hotel = reserva.get("hotel", "N/A")
        tipo_quarto = reserva.get("quarto", "N/A")

        # Datas
        checkin = reserva.get("checkin", "N/A")
        checkout = reserva.get("checkout", "N/A")
        criacao = reserva.get("data_criacao", "N/A")
        # Assume strings no formato AAAA-MM-DD, transforma em DD/MM/AAAA
        def formatar_data(data):
            return f"{data[8:10]}/{data[5:7]}/{data[:4]}" if len(data) == 10 else data
        checkin = formatar_data(checkin)
        checkout = formatar_data(checkout)
        criacao = formatar_data(criacao)

        # Valor
        valor = reserva.get("valor", 0)
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
    # TODO: Implementar formatação e exibição das reservas
    pass


# TODO: TASK 7 - IMPLEMENTAR CRIAR RESERVA
def criar_reserva(dicionario, lista):
    """
    TASK 7 - CRIAR RESERVA (PRIORIDADE: ALTA)
    
    Cria uma nova reserva com validações completas.
    
    VALIDAÇÕES OBRIGATÓRIAS:
    - Data de entrada >= data atual
    - Data de saída > data de entrada
    - CPF deve ter 11 dígitos
    - Nome não pode estar vazio
    - Email deve ter formato válido (@)
    - Destino e hotel não podem estar vazios
    - Preço deve ser > 0
    
    CAMPOS OBRIGATÓRIOS:
    - destino: string
    - hotel: string
    - tipo_quarto: string ('Standard', 'Deluxe', 'Suite')
    - data_entrada: string 'YYYY-MM-DD'
    - data_saida: string 'YYYY-MM-DD'
    - preco_total: float
    - nome_cliente: string
    - cpf_cliente: string (11 dígitos)
    - telefone: string
    - email: string
    
    CAMPOS AUTOMÁTICOS:
    - status_pagamento: 'pendente'
    - status_reserva: 'confirmada'
    - data_criacao: data atual ('YYYY-MM-DD')
    
    EXEMPLO DE USO:
    nova_reserva = {
        "destino": "Florianópolis, SC",
        "hotel": "Hotel Majestic Palace",
        "tipo_quarto": "Deluxe",
        "data_entrada": "2025-07-10",
        "data_saida": "2025-07-15",
        "preco_total": 1800.00,
        "nome_cliente": "Ana Costa",
        "cpf_cliente": "11122233344",
        "telefone": "(48) 77777-7777",
        "email": "ana.costa@email.com"
    }
    """
    # TODO: Implementar com todas as validações usando database.criar()
    pass


# TODO: TASK 8 - IMPLEMENTAR ATUALIZAR RESERVA
def atualizar_reserva(dicionario, lista, id):
    """
    TASK 8 - ATUALIZAR RESERVA (PRIORIDADE: ALTA)
    
    Atualiza uma reserva existente com validações.
    
    CAMPOS ATUALIZÁVEIS:
    - destino, hotel, tipo_quarto
    - data_entrada, data_saida (validar datas)
    - preco_total (deve ser > 0)
    - nome_cliente, telefone, email
    - status_pagamento ('pendente', 'pago', 'cancelado')
    - status_reserva ('confirmada', 'cancelada', 'finalizada')
    
    VALIDAÇÕES:
    - Se alterar datas, validar que entrada >= hoje e saida > entrada
    - Email deve ter @ se fornecido
    - Preço deve ser > 0 se fornecido
    - Não permitir alterar reserva finalizada
    - CPF não pode ser alterado (regra de negócio)
    """
    # TODO: Implementar com validações usando database.atualizar()
    pass


# TODO: TASK 9 - IMPLEMENTAR DELETAR RESERVA
def deletar_reserva(lista, id):
    """
    TASK 9 - DELETAR RESERVA (PRIORIDADE: ALTA)
    
    Deleta uma reserva com verificações de segurança.
    
    REGRAS DE NEGÓCIO:
    - Verificar se a reserva existe antes de deletar
    - Reservas com status 'finalizada' não podem ser deletadas
    - Reservas 'confirmadas' podem ser deletadas (cancelamento)
    - Perguntar confirmação antes de deletar
    
    IMPLEMENTAÇÃO SUGERIDA:
    - Primeiro buscar a reserva
    - Verificar se pode ser deletada
    - Usar database.deletar() para remover
    """
    # TODO: Implementar com verificações de segurança usando database.deletar()
    pass


# TODO: TASK 10 - IMPLEMENTAR BUSCAR POR FILTROS
def buscar_por_filtros(lista, **filtros):
    """
    TASK 10 - BUSCAR POR FILTROS (PRIORIDADE: MÉDIA)
    
    Busca reservas aplicando múltiplos filtros simultaneamente.
    
    FILTROS DISPONÍVEIS:
    - destino: string (busca parcial, case-insensitive)
    - status_reserva: string exata
    - status_pagamento: string exata
    - data_entrada_inicio: reservas a partir desta data
    - data_entrada_fim: reservas até esta data
    - nome_cliente: string (busca parcial, case-insensitive)
    
    PARÂMETROS:
    - lista: lista de reservas
    - **filtros: filtros a serem aplicados
    
    RETORNO:
    - Lista de reservas que atendem a todos os filtros
    
    EXEMPLO DE USO:
    reservas_rio = buscar_por_filtros(lista, destino="Rio", status_pagamento="pago")
    reservas_pendentes = buscar_por_filtros(lista, status_reserva="confirmada", status_pagamento="pendente")
    """
    # TODO: Implementar busca com múltiplos filtros
    pass

