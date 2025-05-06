
import os
import time
os.system("cls || clear")

login_cadastrado ="miguel"
senha_cadastrada = "1234"
login=str(input("digite o usuario: "))
senha=str(input("digite a senha: "))
os.system("cls || clear")
if login_cadastrado == login and senha_cadastrada == senha:
    salarioBase=float(input("digite o seu salario: "))
    os.system("cls || clear")
    dependentes= int(input("quantos dependentes á em sua casa (exceto de você): "))
    planoDeSaude= 150*dependentes
    os.system("cls || clear")
    valeRefeicao=int(input("digite o valor do seu vale refeição da empresa: "))
    os.system("cls || clear")
    while True:
     opcao = str(input("possui vale transposte?: ")).lower()
     if opcao == "s" or opcao == "sim":
        opcao = "possui vale transporte"
        descValeTransporte= salarioBase*0.06
        break
     elif opcao == "n" or opcao == "nao":
        opcao = " não possui vale transporte"
        break
     else:
        print("Opção Invalida \nEspere 2 segundos")
        time.sleep(2)
        os.system("cls || clear")