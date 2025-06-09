import database, functions, menus


database = database.Database('database.json')


def main():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Quartos")
        print("2. Gerenciar Reservas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menus.menu_quartos()
        elif opcao == '2':
            menus.menu_reservas()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")
        database.save_data()