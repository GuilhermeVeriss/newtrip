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
        """Inicializa o banco de dados com dados de teste se estiver vazio."""
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

    def buscar(self, value, lista_nome, by='id'):
        """Busca um item em uma lista pelo valor de uma chave específica."""
        lista = self.data.get(lista_nome, [])

        for item in lista:
            if item.get(by) == value:
                return item
        return None

    def criar(self, dicionario, lista_nome):
        """Cria um novo item com o dicionário fornecido e adiciona à lista."""
        lista = self.data.get(lista_nome, [])

        novo_id = max(item.get('id', 0) for item in lista) + 1 if lista else 1
        novo_item = dicionario.copy()
        novo_item['id'] = novo_id   
        lista.append(novo_item) 
        
        self.data[lista_nome] = lista
        self.save_data()

        return novo_item 

    def atualizar(self, dicionario, lista_nome, id):
        """Atualiza um item existente na lista com os valores fornecidos."""
        lista = self.data.get(lista_nome, [])

        for item in lista:
            if item.get("id") == id:
                item.update(dicionario)
                self.save_data()
                return item
            
        return None

    def deletar(self, lista_nome, id):
        """Deleta um item da lista pelo ID fornecido."""
        lista = self.data.get(lista_nome, [])

        for i, reserva in enumerate(lista):
            if reserva.get("id") == id:
                removido = lista.pop(i)
                self.save_data()
                return removido
        print(f"Reserva com ID {id} não encontrada.")
        return None

