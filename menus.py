import database
import functions


def menu_principal(db):
    """Exibe o menu principal do sistema de reservas."""
    print("\n" + "="*50)
    print("       SISTEMA DE GESTÃO DE RESERVAS")
    print("="*50)
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Listar todas as reservas")
        print("2. Buscar reserva")
        print("3. Criar nova reserva")
        print("4. Atualizar reserva")
        print("5. Deletar reserva")
        print("6. Marcar reserva como paga")
        print("7. Buscar por filtros")
        print("0. Sair")
        print("--------------------")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_listar_reservas(db)
        elif escolha == '2':
            menu_buscar_reserva(db)
        elif escolha == '3':
            menu_criar_reserva(db)
        elif escolha == '4': 
            menu_atualizar_reserva(db)
        elif escolha == '5':
            menu_deletar_reserva(db)
        elif escolha == '6':
            menu_marcar_como_paga(db)
        elif escolha == '7':
            menu_buscar_por_filtros(db)
        elif escolha == '0':
            print("\nSaindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def menu_listar_reservas(db):
    """Exibe todas as reservas do sistema."""
    while True:
        print("\n" + "="*50)
        print("           TODAS AS RESERVAS")
        print("="*50)
        
        functions.listar_reservas(db)
        
        print("\n--- OPÇÕES ---")
        print("1. Atualizar lista")
        print("0. Voltar ao menu principal")
        print("-" * 20)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            continue
        elif opcao == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")


def menu_buscar_reserva(db):
    """Menu para buscar uma reserva específica por ID, nome, CPF ou destino."""
    while True:
        print("\n" + "="*50)
        print("           BUSCAR RESERVA")
        print("="*50)
        
        print("\nEscolha o tipo de busca:")
        print("1. Buscar por ID")
        print("2. Buscar por Nome do Cliente")
        print("3. Buscar por CPF")
        print("4. Buscar por Destino")
        print("0. Voltar ao menu principal")
        print("-" * 20)
        
        opcao = input("Opção: ").strip()
        
        if opcao == '0':
            break
        elif opcao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue
        
        # Processar busca baseada na opção escolhida
        if opcao == '1':
            try:
                valor = int(input("Digite o ID da reserva: "))
                campo = 'id'
            except ValueError:
                print("ID deve ser um número!")
                continue
        elif opcao == '2':
            valor = input("Digite o nome do cliente: ").strip()
            if not valor:
                print("Nome não pode ser vazio!")
                continue
            campo = 'nome_cliente'
        elif opcao == '3':
            valor = input("Digite o CPF (apenas números): ").strip()
            if not valor:
                print("CPF não pode ser vazio!")
                continue
            campo = 'cpf_cliente'
        elif opcao == '4':
            valor = input("Digite o destino: ").strip()
            if not valor:
                print("Destino não pode ser vazio!")
                continue
            campo = 'destino'
        
        reserva = functions.buscar_reserva(valor, db, by=campo)
        
        if reserva:
            print("\n" + "="*42)
            print("RESERVA ENCONTRADA")
            print("="*42)
            print(f"ID: {reserva.get('id')}")
            print(f"Cliente: {reserva.get('nome_cliente')}")
            cpf = reserva.get('cpf_cliente', '')
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if len(cpf) == 11 else cpf
            print(f"CPF: {cpf_formatado}")
            print(f"Email: {reserva.get('email')}")
            print(f"Telefone: {reserva.get('telefone')}")
            print(f"Destino: {reserva.get('destino')}")
            print(f"Hotel: {reserva.get('hotel')}")
            print(f"Tipo de Quarto: {reserva.get('tipo_quarto')}")
            print(f"Check-in: {reserva.get('data_entrada')}")
            print(f"Check-out: {reserva.get('data_saida')}")
            print(f"Valor Total: R$ {reserva.get('preco_total', 0):,.2f}")
            print(f"Status da Reserva: {reserva.get('status_reserva', 'indefinido').capitalize()}")
            print(f"Status do Pagamento: {reserva.get('status_pagamento', 'indefinido').capitalize()}")
            print("="*42)
        else:
            print(f"\nReserva não encontrada para o {campo}: {valor}")
        
        input("\nPressione Enter para continuar...")


def menu_criar_reserva(db):
    """Menu para criar uma nova reserva com validações."""
    while True:
        print("\n" + "="*50)
        print("           CRIAR NOVA RESERVA")
        print("="*50)
        
        print("\n--- OPÇÕES ---")
        print("1. Criar nova reserva")
        print("0. Voltar ao menu principal")
        print("-" * 20)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '0':
            break
        elif opcao != '1':
            print("Opção inválida! Tente novamente.")
            continue
        
        try:
            print("\n--- DADOS DO CLIENTE ---")
            nome_cliente = input("Nome do cliente: ").strip()
            if not nome_cliente:
                print("Nome do cliente não pode ser vazio!")
                continue
                
            cpf_cliente = input("CPF (apenas números): ").strip()
            if not cpf_cliente:
                print("CPF não pode ser vazio!")
                continue
                
            telefone = input("Telefone: ").strip()
            email = input("Email: ").strip()
            
            print("\n--- DADOS DA RESERVA ---")
            destino = input("Destino: ").strip()
            if not destino:
                print("Destino não pode ser vazio!")
                continue
                
            hotel = input("Hotel: ").strip()
            if not hotel:
                print("Hotel não pode ser vazio!")
                continue
            
            print("\nTipos de quarto disponíveis: Standard, Deluxe, Suite")
            tipo_quarto = input("Tipo de quarto: ").strip()
            if not tipo_quarto:
                print("Tipo de quarto não pode ser vazio!")
                continue
            
            print("\n--- DATAS (formato: AAAA-MM-DD) ---")
            data_entrada = input("Data de entrada: ").strip()
            if not data_entrada:
                print("Data de entrada não pode ser vazia!")
                continue
                
            data_saida = input("Data de saída: ").strip()
            if not data_saida:
                print("Data de saída não pode ser vazia!")
                continue
            
            preco_input = input("Preço total: R$ ").strip()
            if not preco_input:
                print("Preço não pode ser vazio!")
                continue
                
            preco_total = float(preco_input)
            
            nova_reserva = {
                "destino": destino,
                "hotel": hotel,
                "tipo_quarto": tipo_quarto,
                "data_entrada": data_entrada,
                "data_saida": data_saida,
                "preco_total": preco_total,
                "nome_cliente": nome_cliente,
                "cpf_cliente": cpf_cliente,
                "telefone": telefone,
                "email": email
            }
            
            reserva_criada = functions.criar_reserva(nova_reserva, db)
            
            if reserva_criada:
                print(f"\n✓ Reserva criada com sucesso!")
                print(f"ID da reserva: {reserva_criada.get('id')}")
                print(f"Cliente: {reserva_criada.get('nome_cliente')}")
                print(f"Destino: {reserva_criada.get('destino')}")
            else:
                print("\n✗ Falha ao criar reserva. Verifique os dados e tente novamente.")
                
        except ValueError:
            print("\n✗ Erro: Preço deve ser um número válido!")
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")


def menu_atualizar_reserva(db):
    """Menu para atualizar uma reserva existente."""
    while True:
        print("\n" + "="*50)
        print("           ATUALIZAR RESERVA")
        print("="*50)
        
        print("\n--- OPÇÕES ---")
        print("1. Atualizar uma reserva")
        print("0. Voltar ao menu principal")
        print("-" * 20)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '0':
            break
        elif opcao != '1':
            print("Opção inválida! Tente novamente.")
            continue
        
        try:
            id_input = input("Digite o ID da reserva a ser atualizada: ").strip()
            if not id_input:
                print("ID não pode ser vazio!")
                continue
                
            id_reserva = int(id_input)
            
            reserva_atual = functions.buscar_reserva(id_reserva, db, by='id')
            
            if not reserva_atual:
                print(f"Reserva com ID {id_reserva} não encontrada!")
                input("\nPressione Enter para continuar...")
                continue
            
            print(f"\n--- DADOS ATUAIS DA RESERVA #{id_reserva} ---")
            print(f"Cliente: {reserva_atual.get('nome_cliente')}")
            print(f"Destino: {reserva_atual.get('destino')}")
            print(f"Hotel: {reserva_atual.get('hotel')}")
            print(f"Status: {reserva_atual.get('status_reserva')}")
            
            print(f"\n--- NOVOS DADOS (Enter para manter atual) ---")
            
            dados_atualizacao = {}
            
            novo_destino = input(f"Destino [{reserva_atual.get('destino')}]: ").strip()
            if novo_destino:
                dados_atualizacao['destino'] = novo_destino
                
            novo_hotel = input(f"Hotel [{reserva_atual.get('hotel')}]: ").strip()
            if novo_hotel:
                dados_atualizacao['hotel'] = novo_hotel
                
            novo_tipo_quarto = input(f"Tipo de quarto [{reserva_atual.get('tipo_quarto')}]: ").strip()
            if novo_tipo_quarto:
                dados_atualizacao['tipo_quarto'] = novo_tipo_quarto
                
            nova_data_entrada = input(f"Data entrada [{reserva_atual.get('data_entrada')}]: ").strip()
            if nova_data_entrada:
                dados_atualizacao['data_entrada'] = nova_data_entrada
                
            nova_data_saida = input(f"Data saída [{reserva_atual.get('data_saida')}]: ").strip()
            if nova_data_saida:
                dados_atualizacao['data_saida'] = nova_data_saida
                
            novo_preco = input(f"Preço total [{reserva_atual.get('preco_total')}]: ").strip()
            if novo_preco:
                try:
                    dados_atualizacao['preco_total'] = float(novo_preco)
                except ValueError:
                    print("Preço deve ser um número válido!")
                    input("\nPressione Enter para continuar...")
                    continue
                
            novo_nome = input(f"Nome cliente [{reserva_atual.get('nome_cliente')}]: ").strip()
            if novo_nome:
                dados_atualizacao['nome_cliente'] = novo_nome
                
            novo_telefone = input(f"Telefone [{reserva_atual.get('telefone')}]: ").strip()
            if novo_telefone:
                dados_atualizacao['telefone'] = novo_telefone
                
            novo_email = input(f"Email [{reserva_atual.get('email')}]: ").strip()
            if novo_email:
                dados_atualizacao['email'] = novo_email
                
            print("\nStatus de pagamento: pendente, pago, cancelado")
            novo_status_pagamento = input(f"Status pagamento [{reserva_atual.get('status_pagamento')}]: ").strip()
            if novo_status_pagamento:
                dados_atualizacao['status_pagamento'] = novo_status_pagamento
                
            print("Status de reserva: confirmada, cancelada, finalizada")
            novo_status_reserva = input(f"Status reserva [{reserva_atual.get('status_reserva')}]: ").strip()
            if novo_status_reserva:
                dados_atualizacao['status_reserva'] = novo_status_reserva
            
            if not dados_atualizacao:
                print("Nenhum campo foi alterado.")
                input("\nPressione Enter para continuar...")
                continue
                
            reserva_atualizada = functions.atualizar_reserva(dados_atualizacao, id_reserva, db)
            
            if reserva_atualizada:
                print(f"\n✓ Reserva {id_reserva} atualizada com sucesso!")
            else:
                print(f"\n✗ Falha ao atualizar reserva {id_reserva}.")
                
        except ValueError:
            print("\n✗ Erro: ID deve ser um número válido!")
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")


def menu_deletar_reserva(db):
    """Menu para deletar uma reserva com confirmação."""
    while True:
        print("\n" + "="*50)
        print("           DELETAR RESERVA")
        print("="*50)
        
        print("\n--- OPÇÕES ---")
        print("1. Deletar uma reserva")
        print("0. Voltar ao menu principal")
        print("-" * 20)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '0':
            break
        elif opcao != '1':
            print("Opção inválida! Tente novamente.")
            continue
        
        try:
            id_input = input("Digite o ID da reserva a ser deletada: ").strip()
            if not id_input:
                print("ID não pode ser vazio!")
                continue
                
            id_reserva = int(id_input)
            
            reserva = functions.buscar_reserva(id_reserva, db, by='id')
            
            if not reserva:
                print(f"Reserva com ID {id_reserva} não encontrada!")
                input("\nPressione Enter para continuar...")
                continue
            
            print(f"\n--- DADOS DA RESERVA #{id_reserva} ---")
            print(f"Cliente: {reserva.get('nome_cliente')}")
            print(f"Destino: {reserva.get('destino')}")
            print(f"Hotel: {reserva.get('hotel')}")
            print(f"Check-in: {reserva.get('data_entrada')}")
            print(f"Check-out: {reserva.get('data_saida')}")
            print(f"Status: {reserva.get('status_reserva')}")
            
            confirmacao = input(f"\nTem certeza que deseja deletar esta reserva? (s/N): ").strip().lower()
            
            if confirmacao == 's' or confirmacao == 'sim':
                reserva_deletada = functions.deletar_reserva(id_reserva, db)
                
                if reserva_deletada:
                    print(f"\n✓ Reserva {id_reserva} deletada com sucesso!")
                else:
                    print(f"\n✗ Falha ao deletar reserva {id_reserva}.")
            else:
                print("\nOperação cancelada.")
                
        except ValueError:
            print("\n✗ Erro: ID deve ser um número válido!")
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")


def menu_marcar_como_paga(db):
    """Menu para marcar uma reserva como paga."""
    while True:
        print("\n" + "="*50)
        print("     MARCAR RESERVA COMO PAGA")
        print("="*50)
        
        print("\n--- OPÇÕES ---")
        print("1. Marcar uma reserva como paga")
        print("0. Voltar ao menu principal")
        print("-" * 20)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '0':
            break
        elif opcao != '1':
            print("Opção inválida! Tente novamente.")
            continue
        
        try:
            id_input = input("Digite o ID da reserva a ser marcada como paga (ou '0' para voltar): ").strip()
            if id_input == '0':
                break
            if not id_input:
                print("ID não pode ser vazio!")
                continue
                
            id_reserva = int(id_input)
            
            reserva = functions.buscar_reserva(id_reserva, db, by='id')
            
            if not reserva:
                print(f"Reserva com ID {id_reserva} não encontrada!")
                input("\nPressione Enter para continuar...")
                continue
            
            if reserva.get('status_pagamento') == 'pago':
                print("Esta reserva já está marcada como paga.")
                input("\nPressione Enter para continuar...")
                continue
            
            confirmacao = input(f"Tem certeza que deseja marcar a reserva {id_reserva} como paga? (s/N): ").strip().lower()
            
            if confirmacao == 's' or confirmacao == 'sim':
                reserva_atualizada = functions.atualizar_reserva({"status_pagamento": "pago"}, id_reserva, db)
                
                if reserva_atualizada:
                    print(f"\n✓ Reserva {id_reserva} marcada como paga com sucesso!")
                else:
                    print(f"\n✗ Falha ao atualizar reserva {id_reserva}.")
            else:
                print("\nOperação cancelada.")
        
        except ValueError:
            print("\n✗ Erro: ID deve ser um número válido!")
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")


def menu_buscar_por_filtros(db):
    """Menu para buscar reservas usando múltiplos filtros (em desenvolvimento)."""
    while True:
        print("\n" + "="*50)
        print("           BUSCAR POR FILTROS")
        print("="*50)
        
        print("\n--- OPÇÕES ---")
        print("1. Buscar por filtros (em desenvolvimento)")
        print("0. Voltar ao menu principal")
        print("-" * 20)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '0':
            break
        elif opcao == '1':
            print("\nEsta funcionalidade ainda não foi implementada.")
            print("Em breve você poderá buscar por:")
            print("- Destino")
            print("- Status da reserva")
            print("- Status do pagamento") 
            print("- Intervalo de datas")
            print("- Nome do cliente")
            input("\nPressione Enter para continuar...")
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    db = database.Database('database.json')
    menu_principal(db)


