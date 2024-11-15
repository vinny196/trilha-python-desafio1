agencia = 1212
conta = 1234
cliente = 'Vinicius Rodrigues Soares Nery'
sobrenome = "Soares Nery"
saldo_inicial = 3000.00
saldo_final = saldo_inicial
qntidade_saque_diario = 0
LIMITE_SAQUE = 500.00
menu = """
Escolha sua opção

[d] Depositar
[s] Sacar
[e] Extrato
[f] Finalizar Operações

"""





while True:
    ag = int(input("digite agencia: "))
    if ag == agencia: 
        
        #print(f"Agencia encontrada") #Teste de funcionalidade
        break
    else:
        print("Agencia nao encontrada")

while True:
    id = int(input("Digite sua conta: ")) 
    if id == conta:
        print("".center(50,"*"))
        print(f"Seja bem vindo, Sr[a].{sobrenome}".center(50,"."))
        print("".center(50,"*"))
        break
    else:
        print("""
Conta nao identificada.

Tente novamente.
              """)
print("Menu".center(50,"-"))

while True: 
    print(menu)
    operacao = str(input(""))

    if operacao == "d":
        depoisto = float(input("Quanto vc quer depoistar: R$"))
        saldo_final = saldo_final + depoisto
        print(saldo_final)

    elif operacao == "e":
        print(f"{saldo_final:.2f}")
    elif operacao == "s":

        saque = float(input("Quanto vc quer sacar: R$"))

        if saldo_final < saque or saque > LIMITE_SAQUE :
            print(f"""
Transação nao realizada!

Quantidade de saques ou
Valor maximo por saque excedido.
    Limite maximo por saque é de R${LIMITE_SAQUE:.2f}

Seu saldo atual é de {saldo_final:.2f}.
                  """)
        else:
            qntidade_saque_diario += 1
            if qntidade_saque_diario >3:
                print("Numero de saques diarios atingidos")
            else:
                saldo_final = saldo_final - saque
                print(f"""
Você sacou R${saque}.

 Seu saldo atual é de R${saldo_final:.2f}
                  """)
    elif operacao == "f":
        print("Agradecemos a prefrencia".center(50," "))
        print("Até breve".center(50,"-"))
        print("".center(50,"*"))
        break

    else:
        print("tente novamente")