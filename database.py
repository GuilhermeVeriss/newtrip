import json


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()
        self.initialize_test_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"reservas": []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def initialize_test_data(self):
        """
        Inicializa o banco de dados com dados de teste se estiver vazio.
        """
        self.data["reservas"] = [
            {
                "id": 1,
                "destino": "Rio de Janeiro, RJ",
                "hotel": "Hotel Copacabana Palace",
                "tipo_quarto": "Standard",
                "data_entrada": "2025-06-20",
                "data_saida": "2025-06-25",
                "preco_total": 1250.00,
                "status_pagamento": "pendente",
                "nome_cliente": "João Silva",
                "cpf_cliente": "12345678901",
                "telefone": "(11) 99999-9999",
                "email": "joao.silva@email.com",
                "status_reserva": "confirmada",
                "data_criacao": "2025-06-17"
            },
            {
                "id": 2,
                "destino": "São Paulo, SP",
                "hotel": "Hotel Unique",
                "tipo_quarto": "Deluxe",
                "data_entrada": "2025-07-01",
                "data_saida": "2025-07-05",
                "preco_total": 2000.00,
                "status_pagamento": "pago",
                "nome_cliente": "Maria Santos",
                "cpf_cliente": "98765432109",
                "telefone": "(11) 88888-8888",
                "email": "maria.santos@email.com",
                "status_reserva": "confirmada",
                "data_criacao": "2025-06-15"
            },
            {
                "id": 3,
                "destino": "Salvador, BA",
                "hotel": "Hotel Fasano Salvador",
                "tipo_quarto": "Suite",
                "data_entrada": "2025-08-10",
                "data_saida": "2025-08-15",
                "preco_total": 3500.00,
                "status_pagamento": "pago",
                "nome_cliente": "Carlos Oliveira",
                "cpf_cliente": "45678912345",
                "telefone": "(71) 77777-7777",
                "email": "carlos.oliveira@email.com",
                "status_reserva": "confirmada",
                "data_criacao": "2025-06-10"
            },
            {
                "id": 4,
                "destino": "Gramado, RS",
                "hotel": "Hotel Casa da Montanha",
                "tipo_quarto": "Standard",
                "data_entrada": "2025-09-05",
                "data_saida": "2025-09-08",
                "preco_total": 900.00,
                "status_pagamento": "pendente",
                "nome_cliente": "Ana Costa",
                "cpf_cliente": "32165498712",
                "telefone": "(54) 66666-6666",
                "email": "ana.costa@email.com",
                "status_reserva": "pendente",
                "data_criacao": "2025-06-16"
            }
        ]
        
        self.save_data()


# TODO: TASK 1 - IMPLEMENTAR FUNÇÃO BUSCAR
def buscar(value, lista, by='id'):
    """
    TASK 1 - FUNÇÃO BUSCAR (PRIORIDADE: ALTA)
    
    Busca uma reserva em uma lista de dicionários pelo valor de uma chave específica.
    
    PARÂMETROS:
    - value: valor a ser buscado
    - lista: lista de dicionários onde buscar
    - by: chave do dicionário para fazer a busca (padrão: 'id')
    
    RETORNO:
    - Dicionário encontrado ou None se não encontrar
    
    EXEMPLO DE USO:
    reservas = [{"id": 1, "nome_cliente": "João"}, {"id": 2, "nome_cliente": "Maria"}]
    resultado = buscar(1, reservas, 'id')  # Retorna {"id": 1, "nome_cliente": "João"}
    resultado = buscar("João", reservas, 'nome_cliente')  # Retorna {"id": 1, "nome_cliente": "João"}
    """
    # TODO: Implementar aqui
    pass


# TODO: TASK 2 - IMPLEMENTAR FUNÇÃO CRIAR
def criar(dicionario, lista):
    """
    TASK 2 - FUNÇÃO CRIAR (PRIORIDADE: ALTA)
    
    Cria uma nova reserva com o dicionário fornecido e adiciona à lista.
    
    REGRAS:
    - ID: busca o maior ID existente e incrementa em 1
    - Se a lista estiver vazia, inicia o ID em 1
    - Adiciona o novo dicionário à lista
    
    PARÂMETROS:
    - dicionario: dicionário com dados da nova reserva (sem ID)
    - lista: lista onde adicionar a nova reserva
    
    RETORNO:
    - Dicionário criado (incluindo o ID gerado)
    
    EXEMPLO DE USO:
    nova_reserva = {"destino": "Recife, PE", "nome_cliente": "Pedro"}
    reserva_criada = criar(nova_reserva, lista_reservas)
    # Retorna: {"id": 5, "destino": "Recife, PE", "nome_cliente": "Pedro"}
    """
    # TODO: Implementar aqui
    pass


# TODO: TASK 3 - IMPLEMENTAR FUNÇÃO ATUALIZAR
def atualizar(dicionario, lista, id):
    """
    TASK 3 - FUNÇÃO ATUALIZAR (PRIORIDADE: ALTA)
    
    Atualiza uma reserva existente na lista com os valores fornecidos.
    
    REGRAS:
    - Busca a reserva pelo ID fornecido
    - Atualiza apenas os campos fornecidos no dicionário
    - Mantém os campos não fornecidos inalterados
    - Não permite alterar o ID
    
    PARÂMETROS:
    - dicionario: dicionario com campos a serem atualizados
    - lista: lista onde buscar a reserva
    - id: ID da reserva a ser atualizada
    
    RETORNO:
    - Dicionário atualizado ou None se ID não for encontrado
    
    EXEMPLO DE USO:
    dados_atualizacao = {"status_pagamento": "pago", "telefone": "(11) 11111-1111"}
    reserva_atualizada = atualizar(dados_atualizacao, lista_reservas, 1)
    """
    # TODO: Implementar aqui
    pass


# TODO: TASK 4 - IMPLEMENTAR FUNÇÃO DELETAR
def deletar(lista, id):
    """
    TASK 4 - FUNÇÃO DELETAR (PRIORIDADE: ALTA)
    
    Deleta uma reserva da lista pelo ID fornecido.
    
    REGRAS:
    - Busca a reserva pelo ID fornecido
    - Remove a reserva da lista
    - Retorna a reserva removida
    
    PARÂMETROS:
    - lista: lista onde buscar e remover a reserva
    - id: ID da reserva a ser removida
    
    RETORNO:
    - Dicionário removido ou None se ID não for encontrado
    
    EXEMPLO DE USO:
    reserva_removida = deletar(lista_reservas, 1)
    """
    # TODO: Implementar aqui
    for i, reserva in enumerate(lista):
        if reserva.get("id") == id:
            return lista.pop(i)  
    print(f"Reserva com ID {id} não encontrada.")
    return None
    pass
