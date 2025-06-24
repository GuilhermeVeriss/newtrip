# NewTrip - Sistema de Gestão de Reservas

Sistema para gerenciar reservas de viagem desenvolvido em Python.

## Como executar

Execute o programa principal:
```
python main.py
```

## Funcionalidades

O sistema apresenta um menu com as seguintes opções:

1. **Listar reservas** - Exibe todas as reservas cadastradas
2. **Buscar reserva** - Localiza uma reserva por ID, nome, CPF ou destino  
3. **Criar reserva** - Adiciona uma nova reserva ao sistema
4. **Atualizar reserva** - Modifica dados de uma reserva existente
5. **Deletar reserva** - Remove uma reserva do sistema
6. **Marcar como paga** - Altera o status de pagamento para "pago"
7. **Buscar por filtros** - (funcionalidade em desenvolvimento)
0. **Sair** - Encerra o programa

## Como criar uma reserva

Para criar uma nova reserva é necessário informar:

**Dados do cliente:**
- Nome completo
- CPF (apenas números, 11 dígitos)
- Telefone
- Email

**Dados da viagem:**
- Destino
- Hotel
- Tipo de quarto (Standard, Deluxe ou Suite)
- Data de entrada (formato: AAAA-MM-DD)
- Data de saída (formato: AAAA-MM-DD)
- Preço total

## Como atualizar uma reserva

Para atualizar uma reserva existente:

1. Selecione a opção "4" no menu principal
2. Digite o ID da reserva que deseja modificar
3. O sistema exibirá os dados atuais da reserva
4. Para cada campo, digite o novo valor ou pressione Enter para manter o atual

**Restrições importantes:**
- O CPF do cliente não pode ser alterado
- Reservas com status "finalizada" não podem ser modificadas
- As novas datas devem seguir as mesmas regras de validação

## Sistema de status

### Status da reserva

**Confirmada:** A reserva foi aceita e está ativa
- Reserva pode ser alterada se necessário

**Cancelada:** A reserva foi cancelada
- Pode ser alterada para outros status se necessário

**Finalizada:** A estadia foi concluída
- Reserva não pode mais ser alterada ou deletada

### Status do pagamento

**Pendente:** Pagamento ainda não foi realizado
- Status padrão para novas reservas
- Cliente deve efetuar o pagamento

**Pago:** Pagamento foi confirmado
- Reserva está quitada
- Pode ser alterado para "cancelado" se houver estorno

**Cancelado:** Pagamento foi cancelado ou estornado

## Marcar reserva como paga

Esta funcionalidade permite alterar rapidamente o status de pagamento:

1. Selecione a opção "6" no menu principal
2. Digite o ID da reserva
3. Confirme a operação

**Quando usar:**
- Após receber confirmação de pagamento
- Para atualizar reservas que foram pagas externamente

**Validações:**
- A reserva deve existir no sistema
- Não é possível marcar como paga uma reserva já cancelada
- Se a reserva já estiver paga, o sistema informará

## Buscar reservas

O sistema oferece diferentes formas de localizar reservas:

**Por ID:** Digite o número único da reserva
**Por nome do cliente:** Digite o nome completo ou parcial
**Por CPF:** Digite os 11 dígitos do CPF
**Por destino:** Digite o destino da viagem

## Deletar reservas

Para remover uma reserva do sistema:

1. Selecione a opção "5" no menu principal
2. Digite o ID da reserva
3. O sistema mostrará os dados da reserva
4. Confirme digitando "s" para sim

**Restrições:**
- Reservas finalizadas não podem ser deletadas
- A operação não pode ser desfeita
- Sempre confirme os dados antes de deletar

## Regras de validação

- As datas devem seguir o formato AAAA-MM-DD
- A data de entrada não pode ser anterior à data atual
- A data de saída deve ser posterior à data de entrada
- O CPF deve conter exatamente 11 dígitos numéricos
- O email deve conter o símbolo @
- O CPF não pode ser alterado após a criação da reserva
- Reservas com status "finalizada" não podem ser alteradas ou deletadas

## Exemplo de cadastro

--- DADOS DO CLIENTE ---
Nome: João Silva
CPF: 12345678901
Telefone: (11) 99999-9999
Email: joao@email.com

--- DADOS DA RESERVA ---
Destino: Rio de Janeiro
Hotel: Hotel Copacabana
Tipo de quarto: Standard
Data entrada: 2025-07-10
Data saída: 2025-07-15
Preço: 1200.00

## Estrutura do projeto

- `main.py` - arquivo principal para execução
- `menus.py` - interface do usuário e navegação
- `functions.py` - funções para manipulação de reservas
- `database.py` - operações do banco de dados
- `database.json` - arquivo de armazenamento das reservas



