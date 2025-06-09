import json


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)


def buscar(value, lista, by='id'):
    """
    Busca um elemento em uma lista de dicionários pelo valor de uma chave específica.
    Se o valor não for encontrado, retorna None.
    """
    # Seu código aqui
    pass

def criar(dicionario, lista):
    """
    Cria um novo dicionário com o valor fornecido e o adiciona à lista.
    ID: busca o maior ID existente e incrementa.
    Se a lista estiver vazia, inicia o ID em 1.
    Retorna o dicionário criado.
    """
    # Seu código aqui
    pass

def atualizar(dicionario, lista, id):
    """
    Atualiza um dicionário existente na lista com os valores fornecidos.
    Se o ID não for encontrado, retorna None.
    Retorna o dicionário atualizado.
    """
    # Seu código aqui
    pass

def deletar(lista, id):
    """
    Deleta um dicionário da lista pelo ID fornecido.
    Se o ID não for encontrado, retorna None.
    Retorna o dicionário deletado.
    """
    # Seu código aqui
    pass