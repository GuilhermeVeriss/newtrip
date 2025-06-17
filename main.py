#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Gestão de Reservas - NewTrip
Versão simplificada focada apenas em reservas de viagem

Funcionalidades:
- Listar reservas
- Buscar reservas
- Criar novas reservas  
- Atualizar reservas existentes
- Deletar reservas
- Buscar por filtros múltiplos

Estrutura do projeto:
- database.py: Funções básicas de CRUD e classe Database
- functions.py: Funções específicas para manipulação de reservas
- menus.py: Interface do usuário e menus
- main.py: Arquivo principal de execução
"""

import database
import menus


def main():
    """
    Função principal do sistema.
    
    Inicializa o banco de dados e chama o menu principal.
    """
    print("Inicializando Sistema de Gestão de Reservas...")
    
    # Inicializar banco de dados
    db = database.Database('database.json')
    
    print("Banco de dados carregado com sucesso!")
    print(f"Reservas encontradas: {len(db.data.get('reservas', []))}")
    
    # Chamar menu principal
    try:
        menus.menu_principal()
    except KeyboardInterrupt:
        print("\n\nSistema encerrado pelo usuário.")
    except Exception as e:
        print(f"\nErro no sistema: {e}")
    finally:
        print("Obrigado por usar o Sistema de Gestão de Reservas!")


if __name__ == "__main__":
    main()