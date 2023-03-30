1- Uma loja de roupas está realizando uma promoção para seus clientes, oferecendo descontos
em diferentes categorias de produtos.

Crie um programa que leia para 100 clientes o nome, o valor total da compra e a categoria
dos produtos que o cliente comprou (sendo elas: "Roupas", "Calçados" e "Acessórios").

As regras de desconto para cada categoria de produto são as seguintes:
● Roupas: desconto de 10% no valor total da compra, caso o valor da compra seja
superior a R$ 100,00.
● Calçados: desconto de 5% no valor total da compra, caso o valor da compra seja
superior a R$ 150,00.
● Acessórios: desconto de 3% no valor total da compra, caso o valor da compra seja
superior a R$ 50,00.
● Se o cliente não comprou nenhum dos produtos das categorias acima ou se o valor
total da compra não atingir o valor mínimo para o desconto, o programa deve exibir
uma mensagem informando que o cliente não tem direito a nenhum desconto.

Calcule e apresente:
● para cada cliente apresente o nome do cliente, o valor total da compra sem
desconto, o valor do desconto e o valor total da compra com desconto;
● a quantidade de clientes que compraram “Roupas”;
● a quantidade de clientes que compraram “Acessórios” com preço entre R$ 65.00 e
R$ 80.00;
● a quantidade de pessoas que compraram “Calçados”.
● a quantidade de clientes que não ganharam desconto;
● o total arrecadado pela loja.

* use o while;
* não utilize fórmulas prontas.


# Inicío das variáveis
cont=0
qtd_roupas = 0
qtd_acessorios = 0
qtd_calcados = 0
sem_desconto = 0
valor_total = 0
valor_com_desconto = 0
desconto = 0

# Leitura dos primeiros dados 
while cont<100:
      nome=input("Digite seu nome: ")
      valor=float(input("Digite o valor total da compra: "))
      categoria=input("Digite a categoria do produto: ")
    
     # Definição dos descontos
    if categoria=="Roupas":
        if valor>100:
            desconto = 0.1
        else:
            sem_desconto = sem_desconto + 1
            print("Valor insuficiente para o desconto.")
        qtd_roupas = qtd_roupas+1
        
    elif categoria=="Calçados":
        if valor>150:
            desconto=0.05
        else:
            sem_desconto = sem_desconto + 1
            print("Valor insuficiente para o desconto.")
        qtd_calcados = qtd_calcados + 1
        
    elif categoria=="Acessórios":
        if valor>50:
            desconto=0.03
            if 65<valor<80:
                qtd_acessorios = qtd_acessorios+1
        else:
            sem_desconto = sem_desconto + 1
            print("Valor insuficiente para o desconto.")
    else:
        print("Categoria não aceita.")
        
    # Atualização das variáveis 
    valor_com_desconto = valor-(valor*desconto)
    valor_total = valor_total + valor_com_desconto
    cont = cont + 1
    
    # Prints finais
    print("Nome:", nome)
    print("Valor total sem desconto:", valor, "reais")
    print("Valor do desconto:", valor*desconto, "reais")
    print("Valor com desconto:", valor_com_desconto, "reais")
    print("Quantidade de pessoas que compraram roupa:", qtd_roupas)
    print("Quantidade de clientes que compraram  acessórios com preço entre 65R$ e 80R$", qtd_acessorios)
    print("Quantidade de pessoas que compraram calçados:", qtd_calcados)
    print("Valor arrecadado", valor_total, "reais")
    desconto = 0
