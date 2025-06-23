# Sistema de Gestão de Reservas - NewTrip

Sistema simplificado para gerenciamento de reservas de viagem focado apenas nas operações básicas de CRUD (Create, Read, Update, Delete).

## 📋 Funcionalidades

- **Listar Reservas**: Visualizar todas as reservas cadastradas
- **Buscar Reservas**: Encontrar reservas por ID, nome, CPF ou destino
- **Criar Reservas**: Adicionar novas reservas com validações
- **Atualizar Reservas**: Modificar dados de reservas existentes
- **Deletar Reservas**: Remover reservas do sistema
- **Buscar por Filtros**: Filtros avançados para localizar reservas

## 🗂️ Estrutura do Projeto

```
newtrip/
├── database.py          # Funções básicas de CRUD e classe Database
├── functions.py         # Funções específicas para manipulação de reservas
├── menus.py            # Interface do usuário e menus
├── main.py             # Arquivo principal de execução
├── test_reservas.py    # Testes pytest para todas as funções
├── database.json       # Banco de dados em formato JSON
└── README.md           # Este arquivo
```

## 🚀 Como Executar

```bash
# Executar o sistema
python main.py

# Executar os testes
pytest test_reservas.py -v

# Executar testes com cobertura
pytest test_reservas.py --cov=database --cov=functions -v
```

## 📊 Dados de Teste

O sistema inicializa automaticamente com 4 reservas de exemplo:

1. **João Silva** - Rio de Janeiro, RJ (Hotel Copacabana Palace)
2. **Maria Santos** - São Paulo, SP (Hotel Unique) 
3. **Carlos Oliveira** - Salvador, BA (Hotel Fasano Salvador)
4. **Ana Costa** - Gramado, RS (Hotel Casa da Montanha)

## 🛠️ Tasks para Desenvolvedores

### Prioridade ALTA (Database - Tasks 1-4)
- **TASK 1**: Implementar função `buscar()` 
- **TASK 2**: Implementar função `criar()`
- **TASK 3**: Implementar função `atualizar()`
- **TASK 4**: Implementar função `deletar()`

### Prioridade ALTA (Functions - Tasks 5-9)
- **TASK 5**: Implementar `buscar_reserva()`
- **TASK 6**: Implementar `listar_reservas()` 
- **TASK 7**: Implementar `criar_reserva()`
- **TASK 8**: Implementar `atualizar_reserva()`
- **TASK 9**: Implementar `deletar_reserva()`

### Prioridade MÉDIA (Tasks 10, 16-22)
- **TASK 10**: Implementar `buscar_por_filtros()`
- **TASK 16-22**: Implementar menus e interface

### Prioridade BAIXA (Tasks 11-15, 23-27)
- **TASK 11-15**: Funções auxiliares (validação, formatação)
- **TASK 23-27**: Funções auxiliares dos menus

## 🧪 Testando o Desenvolvimento

Cada função possui testes específicos. Execute os testes para verificar se sua implementação está correta:

```bash
# Testar função específica
pytest test_reservas.py::test_buscar_id_existente -v

# Testar classe completa
pytest test_reservas.py::TestFuncoesCRUD -v

# Testar todas as funções de database
pytest test_reservas.py -k "database" -v
```

## 📝 Estrutura de uma Reserva

```json
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
}
```

## ✅ Validações Implementadas

### Para Criar/Atualizar Reservas:
- Data de entrada >= data atual
- Data de saída > data de entrada
- CPF com 11 dígitos numéricos
- Nome não pode estar vazio
- Email deve conter @
- Preço deve ser positivo
- Tipos de quarto: Standard, Deluxe, Suite
- Status válidos: confirmada, cancelada, finalizada
- Status pagamento: pendente, pago, cancelado

## 🎯 Exemplo de Uso das Funções

```python
import database
import functions

# Inicializar banco de dados
db = database.Database('database.json')

# Buscar reserva por ID
reserva = functions.buscar_reserva(1, db.data['reservas'])

# Criar nova reserva
nova_reserva = {
    "destino": "Brasília, DF",
    "hotel": "Hotel Nacional",
    "tipo_quarto": "Deluxe",
    "data_entrada": "2025-07-10",
    "data_saida": "2025-07-15",
    "preco_total": 1500.00,
    "nome_cliente": "Pedro Silva",
    "cpf_cliente": "98765432100",
    "telefone": "(61) 99999-9999",
    "email": "pedro@email.com"
}

reserva_criada = functions.criar_reserva(nova_reserva, db.data['reservas'])
db.save_data()

# Listar todas as reservas
functions.listar_reservas(db.data['reservas'])
```

## 📋 Checklist de Desenvolvimento

### Database.py
- [ ] TASK 1: buscar() - Busca item por chave/valor
- [✔] TASK 2: criar() - Cria novo item com ID automático
- [✔] TASK 3: atualizar() - Atualiza item existente
- [ ] TASK 4: deletar() - Remove item da lista

### Functions.py  
- [ ] TASK 5: buscar_reserva() - Wrapper de buscar()
- [ ] TASK 6: listar_reservas() - Formata e exibe reservas
- [✔] TASK 7: criar_reserva() - Cria com validações
- [✔] TASK 8: atualizar_reserva() - Atualiza com validações
- [ ] TASK 9: deletar_reserva() - Deleta com verificações
- [ ] TASK 10: buscar_por_filtros() - Busca com múltiplos filtros
- [ ] TASK 11-15: Funções auxiliares (CPF, email, formatação)

### Menus.py
- [ ] TASK 16: menu_principal() - Loop principal
- [ ] TASK 17-22: Menus específicos (listar, buscar, criar, etc.)
- [ ] TASK 23-27: Funções auxiliares dos menus

## 🏆 Critérios de Aceite

Para cada função implementada:

1. **Todos os testes devem passar** (`pytest test_reservas.py -v`)
2. **Documentação completa** (docstrings detalhadas)
3. **Tratamento de erros** adequado
4. **Validações** conforme especificado
5. **Compatibilidade** com a estrutura existente

## 💡 Dicas de Implementação

1. **Comece pelas funções de database**: São a base para tudo
2. **Use os testes como guia**: Eles mostram exatamente o que é esperado
3. **Implemente uma função de cada vez**: Teste antes de prosseguir
4. **Use as funções auxiliares**: Reutilize código quando possível
5. **Mantenha simplicidade**: O foco é funcionalidade, não complexidade

## 🐛 Solução de Problemas

- **Erro de import**: Verifique se está no diretório correto
- **Testes falhando**: Leia a mensagem de erro com atenção
- **Arquivo não encontrado**: Certifique-se que database.json existe
- **Encoding**: Use UTF-8 para caracteres especiais

---

**Versão**: 2.0 - Simplificada  
**Data**: Junho 2025  
**Desenvolvido por**: Equipe NewTrip
