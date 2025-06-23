import database
import functions


# TODO: TASK 16 - IMPLEMENTAR MENU PRINCIPAL
def menu_principal(db):
    """
    TASK 16 - MENU PRINCIPAL (PRIORIDADE: ALTA)
    
    Exibe o menu principal do sistema de reservas.
    
    OPÇÕES DO MENU:
    1. Listar todas as reservas
    2. Buscar reserva
    3. Criar nova reserva
    4. Atualizar reserva
    5. Deletar reserva
    6. Buscar por filtros
    0. Sair
    
    FUNCIONAMENTO:
    - Exibir menu em loop até usuário escolher sair
    - Validar entrada do usuário
    - Chamar função correspondente
    - Tratar erros de entrada inválida
    """
    print("\n" + "="*50)
    print("       SISTEMA DE GESTÃO DE RESERVAS")
    print("="*50)
    
    # TODO: Implementar loop do menu principal
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Listar reservas")
        print("2. Criar nova reserva")
        print("3. Atualizar reserva")
        print("0. Sair")
        print("--------------------")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            functions.listar_reservas(db.data.get('reservas', []))
        elif escolha == '2':
            menu_criar_reserva(db)
        elif escolha == '0':
            break
        elif escolha == '3': 
            menu_atualizar_reserva(db)
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")


# TODO: TASK 17 - IMPLEMENTAR MENU LISTAR
def menu_listar_reservas(db):
    """
    TASK 17 - MENU LISTAR RESERVAS (PRIORIDADE: ALTA)
    
    Exibe todas as reservas do sistema.
    
    FUNCIONAMENTO:
    - Acessar lista de reservas do banco de dados
    - Chamar functions.listar_reservas()
    - Aguardar usuário pressionar Enter para continuar
    """
    print("\n" + "="*50)
    print("           TODAS AS RESERVAS")
    print("="*50)
    
    # TODO: Implementar listagem usando functions.listar_reservas()
    pass


# TODO: TASK 18 - IMPLEMENTAR MENU BUSCAR
def menu_buscar_reserva(db):
    """
    TASK 18 - MENU BUSCAR RESERVA (PRIORIDADE: ALTA)
    
    Permite buscar uma reserva específica.
    
    OPÇÕES DE BUSCA:
    1. Buscar por ID
    2. Buscar por nome do cliente
    3. Buscar por CPF
    4. Buscar por destino
    
    FUNCIONAMENTO:
    - Exibir submenu de opções
    - Solicitar valor de busca
    - Usar functions.buscar_reserva()
    - Exibir resultado ou mensagem de não encontrado
    """
    print("\n" + "="*50)
    print("           BUSCAR RESERVA")
    print("="*50)
    print("1. Buscar por ID")
    print("2. Buscar por Nome do Cliente")
    print("3. Buscar por CPF")
    print("4. Buscar por Destino")
    print("0. Voltar")
    
    # TODO: Implementar submenu e busca usando functions.buscar_reserva()
    pass


# TODO: TASK 19 - IMPLEMENTAR MENU CRIAR
def menu_criar_reserva(db):
    """
    TASK 19 - MENU CRIAR RESERVA (PRIORIDADE: ALTA)
    
    Coleta dados do usuário e cria uma nova reserva.
    
    DADOS A COLETAR:
    - Destino
    - Hotel
    - Tipo de quarto (Standard/Deluxe/Suite)
    - Data de entrada (formato: DD/MM/AAAA)
    - Data de saída (formato: DD/MM/AAAA)
    - Preço total
    - Nome do cliente
    - CPF do cliente
    - Telefone
    - Email
    
    FUNCIONAMENTO:
    - Solicitar cada campo com input()
    - Converter datas para formato YYYY-MM-DD
    - Validar dados básicos
    - Usar functions.criar_reserva()
    - Salvar no banco de dados
    - Exibir confirmação
    
    TRATAMENTO DE ERROS:
    - Capturar erros de validação
    - Permitir tentar novamente
    - Exibir mensagens claras de erro
    """
    print("\n" + "="*50)
    print("           CRIAR NOVA RESERVA")
    print("="*50)
    
    # TODO: Implementar coleta de dados e criação usando functions.criar_reserva()
    dados = {
        "destino": input("Destino: "),
        "hotel": input("Hotel: "),
        "tipo_quarto": input("Tipo de Quarto (Standard, Deluxe, Suite): "),
        "data_entrada": input("Data de Entrada (AAAA-MM-DD): "),
        "data_saida": input("Data de Saída (AAAA-MM-DD): "),
        "nome_cliente": input("Nome do cliente: "),
        "cpf_cliente": input("CPF do cliente (11 dígitos): "),
        "telefone": input("Telefone: "),
        "email": input("Email: ")
    }
    try:
        dados["preco_total"] = float(input("Preço Total: "))
    except ValueError:
        print("Erro: Preço inválido.")
        return
    
    reserva_criada = functions.criar_reserva(dados, db.data.get('reservas', []))    
    
    if reserva_criada:
        db.save_data() # Salva o estado atual da lista no arquivo
        print("\nSUCESSO: Reserva criada e salva no banco de dados.")
    else:
        print("\nFALHA: Não foi possível criar a reserva. Verifique os erros.")


# TODO: TASK 20 - IMPLEMENTAR MENU ATUALIZAR
def menu_atualizar_reserva(db):
    """
    TASK 20 - MENU ATUALIZAR RESERVA (PRIORIDADE: ALTA)
    
    Permite atualizar uma reserva existente.
    
    FUNCIONAMENTO:
    - Solicitar ID da reserva
    - Buscar e exibir dados atuais
    - Perguntar quais campos atualizar
    - Coletar novos valores (Enter = manter atual)
    - Usar functions.atualizar_reserva()
    - Salvar no banco de dados
    - Exibir confirmação
    
    CAMPOS ATUALIZÁVEIS:
    - Destino, Hotel, Tipo de quarto
    - Datas (entrada e saída)
    - Preço total
    - Nome, Telefone, Email
    - Status da reserva
    - Status do pagamento
    """
    print("\n" + "="*50)
    print("           ATUALIZAR RESERVA")
    print("="*50)
    
    # TODO: Implementar busca e atualização usando functions.atualizar_reserva()
    """Interface para o usuário atualizar uma reserva."""
    try:
        id_reserva = int(input("Digite o ID da reserva que deseja atualizar: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    lista_reservas = db.data.get('reservas', [])
    
    # Busca a reserva para mostrar os dados atuais e verificar se existe
    reserva_existente = next((r for r in lista_reservas if r.get("id") == id_reserva), None)
    if not reserva_existente:
        print(f"Erro: Reserva com ID {id_reserva} não encontrada.")
        return
        
    print(f"\nAtualizando Reserva #{id_reserva}. Pressione Enter para manter o valor atual.")
    print("-" * 50)
    
    dados_para_atualizar = {}
    
    # --- DADOS DA VIAGEM ---
    campos_viagem = ['destino', 'hotel', 'tipo_quarto', 'data_entrada', 'data_saida']
    for campo in campos_viagem:
        valor_atual = reserva_existente.get(campo, 'N/A')
        novo_valor = input(f"{campo.replace('_', ' ').capitalize()} ({valor_atual}): ")
        if novo_valor:
            dados_para_atualizar[campo] = novo_valor
            
    # --- PREÇO TOTAL (com validação) ---
    preco_atual = reserva_existente.get('preco_total', 0.0)
    novo_preco_str = input(f"Preço total ({preco_atual}): ")
    if novo_preco_str:
        try:
            dados_para_atualizar['preco_total'] = float(novo_preco_str)
        except ValueError:
            print(f"Aviso: Formato de preço inválido. O valor do preço não será alterado.")

    print("-" * 50)
    # --- DADOS DO CLIENTE ---
    campos_cliente = ['nome_cliente', 'telefone', 'email']
    for campo in campos_cliente:
        valor_atual = reserva_existente.get(campo, 'N/A')
        novo_valor = input(f"{campo.replace('_', ' ').capitalize()} ({valor_atual}): ")
        if novo_valor:
            dados_para_atualizar[campo] = novo_valor

    print("-" * 50)
    # --- STATUS ---
    campos_status = ['status_reserva', 'status_pagamento']
    for campo in campos_status:
        valor_atual = reserva_existente.get(campo, 'N/A')
        novo_valor = input(f"{campo.replace('_', ' ').capitalize()} ({valor_atual}): ")
        if novo_valor:
            dados_para_atualizar[campo] = novo_valor

    if not dados_para_atualizar:
        print("\nNenhum dado foi alterado.")
        return

    # Chama a função de alto nível que faz as validações
    reserva_atualizada = functions.atualizar_reserva(dados_para_atualizar, lista_reservas, id_reserva)
    
    if reserva_atualizada:
        db.save_data() 
        print("\nSUCESSO: Reserva atualizada.")
    else:
        print("\nFALHA: Não foi possível atualizar a reserva. Verifique os erros de validação.")


# TODO: TASK 21 - IMPLEMENTAR MENU DELETAR
def menu_deletar_reserva(db):
    """
    TASK 21 - MENU DELETAR RESERVA (PRIORIDADE: ALTA)
    
    Permite deletar uma reserva do sistema.
    
    FUNCIONAMENTO:
    - Solicitar ID da reserva
    - Buscar e exibir dados da reserva
    - Confirmar se realmente deseja deletar
    - Usar functions.deletar_reserva()
    - Salvar no banco de dados
    - Exibir confirmação
    
    SEGURANÇA:
    - Sempre pedir confirmação
    - Mostrar dados antes de deletar
    - Permitir cancelar operação
    - Verificar regras de negócio
    """
    print("\n" + "="*50)
    print("           DELETAR RESERVA")
    print("="*50)
    
    # TODO: Implementar busca, confirmação e deleção usando functions.deletar_reserva()
    pass


# TODO: TASK 22 - IMPLEMENTAR MENU FILTROS
def menu_buscar_por_filtros(db):
    """
    TASK 22 - MENU BUSCAR POR FILTROS (PRIORIDADE: MÉDIA)
    
    Permite buscar reservas usando múltiplos filtros.
    
    FILTROS DISPONÍVEIS:
    - Destino (busca parcial)
    - Status da reserva
    - Status do pagamento
    - Período de entrada (data início e fim)
    - Nome do cliente (busca parcial)
    
    FUNCIONAMENTO:
    - Exibir opções de filtros
    - Coletar valores (Enter = não filtrar)
    - Usar functions.buscar_por_filtros()
    - Exibir resultados formatados
    
    INTERFACE:
    - Deixar claro que Enter pula o filtro
    - Mostrar quantos resultados foram encontrados
    - Exibir resultados usando listar_reservas()
    """
    print("\n" + "="*50)
    print("           BUSCAR POR FILTROS")
    print("="*50)
    print("Deixe em branco (Enter) para não filtrar por esse critério")
    
    # TODO: Implementar coleta de filtros e busca usando functions.buscar_por_filtros()
    pass


# TODO: TASK 23 - IMPLEMENTAR FUNÇÕES AUXILIARES DOS MENUS
def obter_escolha(prompt, opcoes_validas):
    """
    TASK 23 - OBTER ESCOLHA (PRIORIDADE: BAIXA)
    
    Solicita uma escolha do usuário e valida se está entre as opções válidas.
    
    PARÂMETROS:
    - prompt: mensagem a exibir
    - opcoes_validas: lista de opções válidas
    
    RETORNO:
    - Opção escolhida (validada)
    
    FUNCIONAMENTO:
    - Loop até entrada válida
    - Exibir erro para entrada inválida
    - Permitir opções numéricas e de texto
    
    EXEMPLO:
    escolha = obter_escolha("Escolha uma opção: ", ['1', '2', '3', '0'])
    """
    # TODO: Implementar validação de entrada
    pass


def obter_data(prompt):
    """
    TASK 24 - OBTER DATA (PRIORIDADE: BAIXA)
    
    Solicita uma data do usuário e valida o formato.
    
    FORMATO ACEITO: DD/MM/AAAA
    CONVERSÃO: para YYYY-MM-DD
    
    VALIDAÇÕES:
    - Formato correto
    - Data válida (não pode ser 30/02, por exemplo)
    - Data não pode ser no passado (para entrada)
    
    RETORNO:
    - String no formato YYYY-MM-DD
    
    TRATAMENTO DE ERROS:
    - Loop até data válida
    - Mensagens de erro claras
    """
    # TODO: Implementar validação de data
    pass


def confirmar_operacao(mensagem):
    """
    TASK 25 - CONFIRMAR OPERAÇÃO (PRIORIDADE: BAIXA)
    
    Solicita confirmação do usuário para operações importantes.
    
    FUNCIONAMENTO:
    - Exibir mensagem
    - Aceitar S/s/Y/y para sim
    - Aceitar N/n para não
    - Repetir até entrada válida
    
    RETORNO:
    - True para confirmado
    - False para cancelado
    """
    # TODO: Implementar confirmação
    pass


def pausar():
    """
    TASK 26 - PAUSAR (PRIORIDADE: BAIXA)
    
    Pausa a execução aguardando o usuário pressionar Enter.
    Útil para permitir que o usuário leia mensagens antes de continuar.
    """
    input("\nPressione Enter para continuar...")


def limpar_tela():
    """
    TASK 27 - LIMPAR TELA (PRIORIDADE: BAIXA)
    
    Limpa a tela do terminal.
    Funciona em Windows e Linux/Mac.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


