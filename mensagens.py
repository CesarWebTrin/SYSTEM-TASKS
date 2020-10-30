import db

MENU_INICIAL = 99

def exibir_cabecalho():

    QTD_COLUNAS = 60
    print ("-" * QTD_COLUNAS)
    print("{:^60}".format("TAREFAS"))
    print("-"* QTD_COLUNAS)
    print("{:^60}".format("tecle 99 volta para o menu inicial, [CTRLC] sai"))
    print("-" * QTD_COLUNAS)

def exibir_tarefas():

    for tarefa in db.get_tarefas():

        check = u'\u2713' if tarefa[2] == 1 else ""

        t = "- [{:>4}] {:<47} {:^3}".format(tarefa[0], tarefa[1], check)
        print(t)
    print ("-" * 60)

def mostrar_opcao_nova_tarefa():
    texto_nova_tarefa = input("Descreva a Tarefa => ")
    print("adicionando tarefa ->" + str(texto_nova_tarefa))
    if texto_nova_tarefa != str(MENU_INICIAL):
        db.add_tarefa(texto_nova_tarefa)

def mostrar_opcao_concluir_tarefa():
    cd_tarefa = int(input("Qual tarefa quer concluir? digite o código = "))
    print("Concluindo tarefa tarefa ->"+ str(cd_tarefa))
    if cd_tarefa != MENU_INICIAL:
        db.concluir_tarefa(cd_tarefa)