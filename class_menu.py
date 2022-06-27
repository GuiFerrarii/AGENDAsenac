from class_agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()
        while True:
            entrada=input(('1 - Novo Cadastro\n2 - Listar Contatos\n0 - Sair\n3 - Mudar contato  :'))
            if entrada == '1':
                agenda.salvar_contatos()
            elif entrada == '2':
                agenda.listar_contatos()
            elif entrada == '3':
                agenda.Mudar_contatos()
            elif entrada == '0':
                break
            else:
                print('Leia as opções burrão!!')