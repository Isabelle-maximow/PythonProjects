
def loop(cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais): 
    while True:
        try:
            menu=input("""Menu:
                Escolha a opção desejada de câmbio.
                1-Dólar(USD)
                2-Euro(EUR)
                3-Bitcoin(BTC)
                4-Etherium(ETH)
                0-Sair
                Escolha uma opção: """)

            if menu=="0":
                print("Saindo do sistema......")
                break
            elif menu=="1":
                #conversão
                dolar=quantidade_reais/cotacao_dolar
                #resultado
                print(f"O valor em dólares é: $ {dolar:.2f}")
            elif menu=="2":
                #conversão
                euro=quantidade_reais/cotacao_euro
                #resultado
                print(f"O valor em euro é: ${euro:.2f}")
            elif menu=="3":
                #conversão
                bit_c=quantidade_reais/cotacao_bitcoin
                #resultado
                print(f"O valor em bitcoin é: ${(bit_c)}")
            elif menu=="4":
                #conversão
                etherium=quantidade_reais/cotacao_etherium
                #resultado
                print(f"O valor em etherium é: ${(etherium)}")
            else:
                print("Opção inválida! Tente novamente....")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    return 