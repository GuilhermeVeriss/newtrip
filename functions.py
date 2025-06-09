import database


## Funções para manipulação de quartos
def buscar_quarto(value, lista, by='id'):
    """
    Busca um quarto em uma lista de dicionários pelo valor de uma chave específica.
    Se o valor não for encontrado, retorna None.
    """
    # Seu código aqui
    pass

def criar_quarto(dicionario, lista):
    """
    Cria um novo dicionário com o valor fornecido e o adiciona à lista.
    ID: busca o maior ID existente e incrementa.
    Se a lista estiver vazia, inicia o ID em 1.
    Retorna o dicionário criado.
    """
    # Seu código aqui
    pass

def atualizar_quarto(dicionario, lista, id):
    """
    Atualiza um dicionário existente na lista com os valores fornecidos.
    Se o ID não for encontrado, retorna None.
    Retorna o dicionário atualizado.
    """
    # Seu código aqui
    pass

def deletar_quarto(lista, id):
    """
    Deleta um dicionário da lista pelo ID fornecido.
    Se o ID não for encontrado, retorna None.
    Retorna o dicionário deletado.
    """
    # Seu código aqui
    pass

## Funções para manipulação de reservas
def buscar_reserva(value, lista, by='id'):
    """
    Busca uma reserva em uma lista de dicionários pelo valor de uma chave específica.
    Se o valor não for encontrado, retorna None.
    """
    # Seu código aqui
    pass

def verificar_disponibilidade(quarto, lista_reservas, data_inicio, data_fim):
    """
    Verifica a disponibilidade de um quarto em um intervalo de datas.
    Retorna True se o quarto estiver disponível, False caso contrário.
    """
    # Seu código aqui
    pass

def mostrar_reservas(lista):
    """
    Exibe todas as reservas na lista.
    Se a lista estiver vazia, exibe uma mensagem informando.
    """
    if not lista:
        print("Nenhuma reserva encontrada.")
    else:
        for reserva in lista:
            # Exibe os detalhes da reserva
            # Seu código aqui
            pass

def criar_reserva(dicionario, lista):
    """
    Cria uma nova reserva com o valor fornecido e a adiciona à lista.
    ID: busca o maior ID existente e incrementa.
    Se a lista estiver vazia, inicia o ID em 1.
    Retorna o dicionário criado.
    """
    # Seu código aqui
    pass

def atualizar_reserva(dicionario, lista, id):
    """
    Atualiza uma reserva existente na lista com os valores fornecidos.
    Se o ID não for encontrado, retorna None.
    Retorna o dicionário atualizado.
    """
    # Seu código aqui
    pass

def deletar_reserva(lista, id):
    """
    Deleta uma reserva da lista pelo ID fornecido.
    Se o ID não for encontrado, retorna None.
    Retorna o dicionário deletado.
    """
    # Seu código aqui
    pass


