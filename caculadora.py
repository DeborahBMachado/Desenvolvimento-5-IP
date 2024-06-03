#função para desenvolvimento de uma calculadora
def calculadora():
  fechar = False
  while(fechar == False):
    a = float(input("Digite o primeiro numero: \n"))
    b = float(input("Digite o segundo numero: \n"))
  #instruções para definição das operações
    operacao = input("""Digite a operação desejada conforme abaixo:
1 para adicao
2 para subtracao
3 para multiplicacao
4 para divisao
0 para sair\n""")
    #estruturas condicionais para os cálculos dependendo da operação escolhida
    if operacao == "1":
      print("{} + {} = ".format(a, b))
      print(a + b)

    elif operacao == "2":
      print("{} - {} = ". format(a, b))
      print(a - b)
    
    elif operacao == "3":
      print("{} * {} = ". format(a, b))
      print(a * b)

    elif operacao == "4":
      print("{} / {} = ". format(a, b))
      print(a / b)
  
    elif operacao == "0":
      print("Fechando o sistema....")
      fechar = True
  
    else:
      print("Operacao invalida")
 
calculadora() # chamada da função
