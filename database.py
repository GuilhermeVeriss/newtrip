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
            return {"quartos": [], "reservas": []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def initialize_test_data(self):
        """
        Inicializa o banco de dados com dados de teste se estiver vazio.
        """
        if not self.data.get("quartos"):
            self.data["quartos"] = [
                {
                    "id": 1,
                    "numero": "101",
                    "tipo": "Standard",
                    "capacidade": 2,
                    "preco_diaria": 150.00,
                    "status": "disponivel",
                    "descricao": "Quarto standard com cama de casal"
                },
                {
                    "id": 2,
                    "numero": "102",
                    "tipo": "Deluxe",
                    "capacidade": 3,
                    "preco_diaria": 250.00,
                    "status": "disponivel",
                    "descricao": "Quarto deluxe com vista para o mar"
                },
                {
                    "id": 3,
                    "numero": "201",
                    "tipo": "Suite",
                    "capacidade": 4,
                    "preco_diaria": 400.00,
                    "status": "manutencao",
                    "descricao": "Suite presidencial com jacuzzi"
                }
            ]
        
        if not self.data.get("reservas"):
            self.data["reservas"] = [
                {
                    "id": 1,
                    "quarto_id": 1,
                    "numero_quarto": "101",
                    "data_entrada": "2025-06-20",
                    "data_saida": "2025-06-25",
                    "preco_total": 750.00,
                    "status_pagamento": "pendente",
                    "nome_cliente": "João Silva",
                    "cpf_cliente": "12345678901",
                    "telefone": "(11) 99999-9999",
                    "status_reserva": "confirmada"
                },
                {
                    "id": 2,
                    "quarto_id": 2,
                    "numero_quarto": "102",
                    "data_entrada": "2025-07-01",
                    "data_saida": "2025-07-05",
                    "preco_total": 1000.00,
                    "status_pagamento": "pago",
                    "nome_cliente": "Maria Santos",
                    "cpf_cliente": "98765432109",
                    "telefone": "(11) 88888-8888",
                    "status_reserva": "confirmada"
                }
            ]
        
        self.save_data()


# TODO: TASK 1 - IMPLEMENTAR FUNÇÃO BUSCAR
def buscar(value, lista, by='id'):
    """
    TASK 1 - FUNÇÃO BUSCAR (PRIORIDADE: ALTA)
    
    Busca um elemento em uma lista de dicionários pelo valor de uma chave específica.
    
    PARÂMETROS:
    - value: valor a ser buscado
    - lista: lista de dicionários onde buscar
    - by: chave do dicionário para fazer a busca (padrão: 'id')
    
    RETORNO:
    - Dicionário encontrado ou None se não encontrar
    
    EXEMPLO DE USO:
    quartos = [{"id": 1, "numero": "101"}, {"id": 2, "numero": "102"}]
    resultado = buscar(1, quartos, 'id')  # Retorna {"id": 1, "numero": "101"}
    resultado = buscar("101", quartos, 'numero')  # Retorna {"id": 1, "numero": "101"}
    
    """
    # TODO: Implementar aqui
    pass


# TODO: TASK 2 - IMPLEMENTAR FUNÇÃO CRIAR
def criar(dicionario, lista):
    """
    TASK 2 - FUNÇÃO CRIAR (PRIORIDADE: ALTA)
    
    Cria um novo dicionário com o valor fornecido e o adiciona à lista.
    
    REGRAS:
    - ID: busca o maior ID existente e incrementa em 1
    - Se a lista estiver vazia, inicia o ID em 1
    - Adiciona o novo dicionário à lista
    
    PARÂMETROS:
    - dicionario: dicionário com dados do novo item (sem ID)
    - lista: lista onde adicionar o novo item
    
    RETORNO:
    - Dicionário criado (incluindo o ID gerado)
    
    EXEMPLO DE USO:
    novo_quarto = {"numero": "103", "tipo": "Standard"}
    quarto_criado = criar(novo_quarto, lista_quartos)
    # Retorna: {"id": 3, "numero": "103", "tipo": "Standard"}
    """
    # TODO: Implementar aqui
    pass


# TODO: TASK 3 - IMPLEMENTAR FUNÇÃO ATUALIZAR
def atualizar(dicionario, lista, id):
    """
    TASK 3 - FUNÇÃO ATUALIZAR (PRIORIDADE: ALTA)
    
    Atualiza um dicionário existente na lista com os valores fornecidos.
    
    REGRAS:
    - Busca o item pelo ID fornecido
    - Atualiza apenas os campos fornecidos no dicionário
    - Mantém os campos não fornecidos inalterados
    - Não permite alterar o ID
    
    PARÂMETROS:
    - dicionario: dicionário com campos a serem atualizados
    - lista: lista onde buscar o item
    - id: ID do item a ser atualizado
    
    RETORNO:
    - Dicionário atualizado ou None se ID não for encontrado
    
    EXEMPLO DE USO:
    dados_atualizacao = {"preco_diaria": 200.00, "status": "ocupado"}
    item_atualizado = atualizar(dados_atualizacao, lista_quartos, 1)
    """
    # TODO: Implementar aqui
    pass


# TODO: TASK 4 - IMPLEMENTAR FUNÇÃO DELETAR
def deletar(lista, id):
    """
    TASK 4 - FUNÇÃO DELETAR (PRIORIDADE: ALTA)
    
    Deleta um dicionário da lista pelo ID fornecido.
    
    REGRAS:
    - Busca o item pelo ID fornecido
    - Remove o item da lista
    - Retorna o item removido
    
    PARÂMETROS:
    - lista: lista onde buscar e remover o item
    - id: ID do item a ser removido
    
    RETORNO:
    - Dicionário removido ou None se ID não for encontrado
    
    EXEMPLO DE USO:
    item_removido = deletar(lista_quartos, 1)
    """
    # TODO: Implementar aqui
    pass