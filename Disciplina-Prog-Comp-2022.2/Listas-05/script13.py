"""
Crie um programa que tenha uma constante chamada senha_padrao com um valor pré-definido (atribuir
o valor swordfish a essa constante). O programa deverá solicitar uma senha ao usuário. Caso o usuário
não informe a senha correta (definida na constante senha_padrao), o programa deverá solicitar
novamente o valor. O programa só deverá parar de solicitar a senha quanto o usuário informar um valor
igual ao valor definido na constante senha_padrao.

"""
senha_padrao = 'swordfish'

for verificador in senha_padrao:
    verificador = input('informe um senha: ')
    if verificador == senha_padrao:
        print('PARABÉNS: <<SENHA CORRETA>>')
        break
    else:
        print('SENHA INCORRETA: <<tente novamente>>')