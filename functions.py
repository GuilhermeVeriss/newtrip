import database
from datetime import datetime


## FUNÇÕES PARA MANIPULAÇÃO DE QUARTOS

# TODO: TASK 5 - IMPLEMENTAR BUSCAR QUARTO
def buscar_quarto(value, lista, by='id'):
    """
    TASK 5 - BUSCAR QUARTO (PRIORIDADE: MÉDIA)
    
    Wrapper da função database.buscar() específica para quartos.
    
    PARÂMETROS:
    - value: valor a ser buscado
    - lista: lista de quartos
    - by: campo para busca ('id', 'numero', 'tipo', etc.)
    
    RETORNO:
    - Dicionário do quarto encontrado ou None
    
    IMPLEMENTAÇÃO SUGERIDA:
    return database.buscar(value, lista, by)
    """
    # TODO: Implementar usando database.buscar()
    pass


# TODO: TASK 6 - IMPLEMENTAR CRIAR QUARTO
def criar_quarto(dicionario, lista):
    """
    TASK 6 - CRIAR QUARTO (PRIORIDADE: MÉDIA)
    
    Cria um novo quarto com validações específicas.
    
    VALIDAÇÕES OBRIGATÓRIAS:
    - Número do quarto deve ser único
    - Tipo deve ser válido ('Standard', 'Deluxe', 'Suite')
    - Capacidade deve ser > 0
    - Preço deve ser > 0
    - Status padrão: 'disponivel'
    
    CAMPOS OBRIGATÓRIOS:
    - numero: string
    - tipo: string
    - capacidade: int
    - preco_diaria: float
    - descricao: string (opcional)
    
    EXEMPLO DE USO:
    novo_quarto = {
        "numero": "103",
        "tipo": "Standard",
        "capacidade": 2,
        "preco_diaria": 180.00,
        "descricao": "Quarto standard renovado"
    }
    """
    # TODO: Implementar com validações
    pass


# TODO: TASK 7 - IMPLEMENTAR ATUALIZAR QUARTO
def atualizar_quarto(dicionario, lista, id):
    """
    TASK 7 - ATUALIZAR QUARTO (PRIORIDADE: MÉDIA)
        
    VALIDAÇÕES:
    - Se número for alterado, deve ser único
    - Tipo deve ser válido se fornecido
    - Valores numéricos devem ser > 0
    - Não permitir alterar para status inválido
    
    STATUS VÁLIDOS: 'disponivel', 'ocupado'
    """
    # TODO: Implementar com validações usando database.atualizar()
    pass


# TODO: TASK 8 - IMPLEMENTAR DELETAR QUARTO
def deletar_quarto(lista, id):
    """
    TASK 8 - DELETAR QUARTO (PRIORIDADE: MÉDIA)
    
    Deleta um quarto com verificações de segurança.
    
    REGRAS DE NEGÓCIO:
    - Não permitir deletar quarto com reservas ativas
    - Verificar se existe no sistema antes de deletar
    
    PARÂMETROS:
    - lista: lista de quartos
    - id: ID do quarto a ser deletado
    
    NOTA: Para verificar reservas ativas, você precisará acessar
    a lista de reservas do banco de dados.
    """
    # TODO: Implementar com verificações de segurança
    pass


## FUNÇÕES PARA MANIPULAÇÃO DE RESERVAS

# TODO: TASK 9 - IMPLEMENTAR BUSCAR RESERVA
def buscar_reserva(value, lista, by='id'):
    """
    TASK 9 - BUSCAR RESERVA (PRIORIDADE: MÉDIA)
    
    Wrapper da função database.buscar() específica para reservas.
    
    CAMPOS COMUNS PARA BUSCA:
    - id, quarto_id, nome_cliente, cpf_cliente, status_reserva
    
    IMPLEMENTAÇÃO SUGERIDA:
    return database.buscar(value, lista, by)
    """
    # TODO: Implementar usando database.buscar()
    pass


# TODO: TASK 10 - IMPLEMENTAR VERIFICAR DISPONIBILIDADE
def verificar_disponibilidade(quarto_id, lista_reservas, data_inicio, data_fim):
    """
    TASK 10 - VERIFICAR DISPONIBILIDADE (PRIORIDADE: ALTA)
    
    Verifica se um quarto está disponível em um período específico.
    
    REGRAS:
    - Verificar conflitos de datas com reservas existentes
    - Considerar apenas reservas confirmadas
    - Data de entrada < Data de saída
    - Formato de data: 'YYYY-MM-DD'
    
    LÓGICA DE CONFLITO:
    Há conflito se:
    - Nova entrada < reserva_saida E nova_saida > reserva_entrada
    
    PARÂMETROS:
    - quarto_id: ID do quarto a verificar
    - lista_reservas: lista de todas as reservas
    - data_inicio: data de entrada (string 'YYYY-MM-DD')
    - data_fim: data de saída (string 'YYYY-MM-DD')
    
    RETORNO:
    - True se disponível, False se não disponível
    
    EXEMPLO DE USO:
    disponivel = verificar_disponibilidade(1, reservas, '2025-06-30', '2025-07-05')
    
    """
    # TODO: Implementar lógica de verificação de disponibilidade
    pass


# TODO: TASK 11 - IMPLEMENTAR MOSTRAR RESERVAS
def mostrar_reservas(lista):
    """
    TASK 11 - MOSTRAR RESERVAS (PRIORIDADE: BAIXA)
    
    Exibe todas as reservas de forma formatada.
    
    FORMATO SUGERIDO:
    ==========================================
    RESERVA #1
    ==========================================
    Cliente: João Silva (CPF: 123.456.789-01)
    Quarto: 101 (ID: 1)
    Período: 20/06/2025 a 25/06/2025
    Valor Total: R$ 750,00
    Status Pagamento: Pendente
    Status Reserva: Confirmada
    Telefone: (11) 99999-9999
    ==========================================
    
    TRATAMENTOS:
    - Lista vazia: "Nenhuma reserva encontrada."
    - Formatar CPF: XXX.XXX.XXX-XX
    - Formatar datas: DD/MM/AAAA
    - Formatar valores: R$ X.XXX,XX
    
    """
    if not lista:
        print("Nenhuma reserva encontrada.")
        return
    
    # TODO: Implementar formatação e exibição das reservas
    pass


# TODO: TASK 12 - IMPLEMENTAR CRIAR RESERVA
def criar_reserva(dicionario, lista):
    """
    TASK 12 - CRIAR RESERVA (PRIORIDADE: ALTA)
    
    Cria uma nova reserva com validações completas.
    
    VALIDAÇÕES OBRIGATÓRIAS:
    - Quarto deve existir
    - Quarto deve estar disponível no período
    - Data de entrada >= data atual
    - Data de saída > data de entrada
    - CPF deve ter 11 dígitos
    - Nome não pode estar vazio
    - Calcular preço total automaticamente
    
    CAMPOS OBRIGATÓRIOS:
    - quarto_id: int
    - data_entrada: string 'YYYY-MM-DD'
    - data_saida: string 'YYYY-MM-DD'
    - nome_cliente: string
    - cpf_cliente: string (11 dígitos)
    - telefone: string (opcional)
    
    CAMPOS AUTOMÁTICOS:
    - numero_quarto: buscar pelo quarto_id
    - preco_total: (dias * preco_diaria)
    - status_pagamento: 'pendente'
    - status_reserva: 'confirmada'
    
    EXEMPLO DE USO:
    nova_reserva = {
        "quarto_id": 1,
        "data_entrada": "2025-07-10",
        "data_saida": "2025-07-15",
        "nome_cliente": "Ana Costa",
        "cpf_cliente": "11122233344",
        "telefone": "(11) 77777-7777"
    }
    """
    # TODO: Implementar com todas as validações
    pass


# TODO: TASK 13 - IMPLEMENTAR ATUALIZAR RESERVA
def atualizar_reserva(dicionario, lista, id):
    """
    TASK 13 - ATUALIZAR RESERVA (PRIORIDADE: MÉDIA)
    
    Atualiza uma reserva existente com validações.
    
    CAMPOS ATUALIZÁVEIS:
    - data_entrada, data_saida (verificar disponibilidade)
    - nome_cliente, telefone
    - status_pagamento ('pendente', 'pago', 'cancelado')
    - status_reserva ('confirmada', 'cancelada', 'finalizada')
    
    VALIDAÇÕES:
    - Se alterar datas, verificar disponibilidade
    - Não permitir alterar reserva finalizada
    - Recalcular preço se alterar datas
    """
    # TODO: Implementar com validações
    pass


# TODO: TASK 14 - IMPLEMENTAR DELETAR/CANCELAR RESERVA
def deletar_reserva(lista, id):
    """
    TASK 14 - DELETAR/CANCELAR RESERVA (PRIORIDADE: MÉDIA)
    
    Cancela uma reserva (ao invés de deletar fisicamente).
    
    REGRAS DE NEGÓCIO:
    - Reservas confirmadas: alterar status para 'cancelada'
    - Reservas já finalizadas: não permitir cancelamento
    - Manter histórico (não deletar fisicamente)
    
    IMPLEMENTAÇÃO SUGERIDA:
    - Usar atualizar_reserva() para alterar status
    - Só deletar fisicamente se explicitamente solicitado
    """
    # TODO: Implementar cancelamento (não deleção física)
    pass


# TODO: TASK 15 - IMPLEMENTAR FUNÇÕES AUXILIARES
def calcular_preco_total(data_entrada, data_saida, preco_diaria):
    """
    TASK 15 - CALCULAR PREÇO TOTAL (PRIORIDADE: BAIXA)
    
    Calcula o preço total da reserva baseado no período e preço da diária.
    
    FÓRMULA:
    dias = (data_saida - data_entrada).days
    preco_total = dias * preco_diaria
    
    PARÂMETROS:
    - data_entrada: string 'YYYY-MM-DD'
    - data_saida: string 'YYYY-MM-DD'
    - preco_diaria: float
    
    RETORNO:
    - float: preço total calculado
    
    DICA: Use datetime.strptime() para converter strings em dates
    """
    # TODO: Implementar cálculo de preço
    pass
