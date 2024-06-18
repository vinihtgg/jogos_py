#LISTA DE PRODUTOS E VALORES
lista_de_produtos = []

#VARIAVEL QUE VAI CONTROLAR SE VAMOS ADICIONAR
#MAIS PRODUTOS
adicionar_produtos = True

#
print("Primeiro vamos cadastrar os produtos")

#ENQUANTO adicionar_produtos FOR True, vamos
#ADICONAR PRODUTOS  
while adicionar_produtos:
    #OBTER O NOME DO  PRODUTO
    produto = input("Adicione um produto:\n")
    #OBTER O VALOR DO PRODUTO
    valor = int(input("Qual o valor do produto?\n"))
    #ADICIONAR O PRODUTO E O VALOR A NOSSA LISTA
    lista_de_produtos.append([produto, valor])
    #PERGUNTAR SE DESEJA ADICIONAR MAIS PRODUTOS
    adicionar_mais = int(input("Adicionar mais produtos? (1) Sim (2) Não\n"))
    #SE O USUARIO DIGITAR NÃO, PARAR ESTE LOOP
    if(adicionar_mais == 2): adicionar_produtos = False

print("*************************************")
print("*************************************")
print("*********** ABRIR CAIXA *************")
print("*************************************")
print("*************************************")

#LISTA DE PRODUTOS COMPRADOS
produtos_comprados = []
#TOTAL A SER PAGO 
total = 0
#VARIAVEL QUE VAI CONTROLAR SE O USUARIO VAI CONTINUAR
#COMPRANDO OS PRODUTOS
continuar_comprando = True

#ENQUANTO continuar_comprando FOR True
#VAMOS FAZER COMPRAS
while continuar_comprando:
    print("Digite o número do produto...")
    #INDICE PARA SABER EM QUE POSIÇÃO ESTAMOS NA LISTA
    index = 0
    #NÚMERO DO ITEM COMPRADO
    item = 0
    #FOR PARA IMPRIMIR TODOS ELEMENTOS DA LISTA
    for produto in lista_de_produtos:
        print("{} corresponte à {}".format(index, produto[0]))
        index= index+1  
        
    #PEDIR PRO USUARIO DIGITAR O ITEM DO PRODUTO
    item = int(input("Digite o número do produto:\n"))    
    #ADICIONAR O VALOR DO PRODUTO AO TOTAL
    total = total + lista_de_produtos[item][1]
    #ADICIONAR O PRODUTO COMPRADO A LISTA
    produtos_comprados.append(lista_de_produtos[item][0])
    #PERGUNTAR SE DESEJA CONTINUAR COMPRANDO
    comprar_mais = int(input("Continuar compra? (1) Sim (2) Não"))
    #SE "NÃO", PARAR ESTE LOOP
    if (comprar_mais == 2): continuar_comprando = False
        
print("*************************************")
print("************** TOTAL ****************")
print("*************************************")

print("Produtos comprados:")

for produto in produtos_comprados:
    print(produto)

print("\nO valor total da compra é {}".format(total))