1- Faça um programa que leia 6 números inteiros e apresente:
- para cada número a informação se é positivo, negativo ou igual a zero;
- a quantidade de zeros digitados;
- a soma dos números positivos;
- a média de números negativos;

cont=0
qtd_zero=0
soma=0
media_negativo=0
qtd_negativo=0

while cont<6:
      num=int(input("Digite o número: "))
      
      if num>0:
         soma=soma+num
         print("Positivo")   
      elif num<0:
           media_negativo=media_negativo+num
           qtd_negativo=qtd_negativo+1
           print("Negativo")  
      else:
           qtd_zero=qtd_zero+1
           
      cont=cont+1
      
print("Quantidade de zero:", qtd_zero)
print("Soma positivos:", soma)

if media_negativo !=0:
   print("Média negativa:", media_negativo/qtd_negativo)
else:
   print("Não podemos fazer divisão por 0")
   
#eu boto o último if pq se eu fizesse um código sem um número 0 ou um número negativo, não ia dar certo


2- Faça um programa que leia o preço de compra e o preço de venda de 5 esculturas que serão expostas em uma galeria, 
calcule e apresente o lucro de cada escultura e a média dos lucros.

cont=0
media=0

while cont<5:
      compra=float(input("Digite o preço de compra: "))
      venda=float(input("Digite o preço de venda: "))
      lucro=venda-compra
      
      print("Escultura:", cont, "Obteve o lucro de: ", lucro, "reais")
      
      media=media+lucro
      cont=cont+1
      
print("Média:", media/5)


3- Faça um programa que leia a idade, a nacionalidade e o sexo de 15 pessoas, calcule e apresente:
a. a quantidade de mulheres maiores de idade;
b. a quantidade de homens brasileiros (nacionalidade brasileira) que têm entre 20 e 30 anos;
c. a média das idades.

cont=0
mulher_maior_18=0
homem_br=0
soma_idade=0

while cont<15:
      idade=int(input("Digite a idade: "))
      nacionalidade=input("Digite a nacionalidade: ")
      sexo=input("Digite o sexo: ")
      if sexo=="feminino" and idade>=18:
         mulher_maior_18=mulher_maior_18+1
      if sexo=="masculino" and nacionalidade=="brasileiro" and 20<=idade<=30:
         homem_br=homem_br+1
      soma_idade=soma_idade+idade
      cont=cont+1
      
print("Quantidade de mulheres maiores de idade: ", mulher_maior_18)
print("Quantidade de homens brasileiros entre 20 e 30 anos: ", homem_br)
print("Média:", soma_idade/15)


4- Construa um programa que permita fazer um levantamento do estoque de vinhos de uma adega,
que possui 50 garrafas, tendo como dados de entrada o tipo de cada vinho (B - Branco, T - Tinto e R - Rosé).
O programa deve fazer a leitura e especificar a porcentagem de cada tipo de vinho. 

cont=0
branco=0
tinto=0
rosé=0

while cont<50:
      vinho=input("Digite o tipo de vinho: ")
      if vinho=="B":
         branco=branco+1
      elif vinho=="T":
           tinto=tinto+1
      elif vinho=="R":
           rosé=rosé+1
      else:
          print("Opção inválida")
          
      cont=cont+1
      
print("Brancos: ", (branco*100/50))
print("Tinto:", (tinto*100/50))
print("Rosé:", (rosé*100/50))


5- Faça um programa que leia a idade e o sexo (“feminino” ou “masculino”) de 10 alunos de uma turma, calcule e apresente as seguintes informações:
a. há mais mulheres, mais homens ou a mesma quantidade de homens e mulheres na turma?
b. a média das idades dos alunos da turma do sexo masculino.
c. a média geral da idade dos alunos.

cont = 0
qtd_homem = 0
qtd_mulher = 0
soma_idade_homem = 0
soma_idade_geral = 0

while cont<10:
  idade = int(input("Digite a idade do aluno: "))
  sexo = input("Digite o sexo do aluno: ")

  if sexo == "feminino":
    qtd_mulher = qtd_mulher + 1
  elif sexo == "masculino":
    qtd_homem = qtd_homem + 1
    soma_idade_homem = idade + soma_idade_homem
    
  cont = cont + 1

  soma_idade_geral = idade + soma_idade_geral
  
if qtd_homem > 0:
  media_idade_homem = soma_idade_homem / qtd_homem
else:
  media_idade_homem = 0

if qtd_mulher > qtd_homem:
  print("Há mais mulheres na turma.")
elif qtd_homem > qtd_mulher:
  print("Há mais homens na turma.")
else:
  print("Há a mesma quantidade de homens e mulheres na turma.")

media_idade_geral = soma_idade_geral / 10
print("A média das idades dos alunos do sexo masculino é:", media_idade_homem)
print("A média geral das idades dos alunos é de:", media_idade_geral)

  
  
6- Faça um programa que leia o preço de compra e o preço de venda de 5 esculturas que serão expostas em uma galeria, calcule e apresente:
a. o lucro de cada escultura;
b. quantidade de esculturas com preço entre R$ 20.00 e R$ 50.00;
c. a somatória dos lucros.

cont=0
qtd_escultura=0
soma_lucro=0

while cont<5:
    compra=float(input("Digite o preço de compra: "))
    venda=float(input("Digite o preço de venda: "))
    lucro=venda-compra
    print("O lucro da escultura foi: " lucro)
    
    if 20<venda<50:
        qtd_escultura=qtd_escultura+1
    
    soma_lucro=soma_lucro+lucro
    
    cont=cont+1
    
    print("A quantidade de escultura com o preço entre 20R$ e 50R$ foi: ", qtd_escultura)
    print("A somatória dos lucros foram: ", soma_lucro)
    
    
7- Faça um programa que leia a idade, a nacionalidade e o sexo de 6 pessoas, calcule e apresente:
a. a quantidade de homens brasileiros (nacionalidade brasileira) que têm entre 20 e 30
anos;
b. a quantidade de idosos (>= 65 anos) que são brasileiros, italianos ou franceses.
c. a média das idades.

cont=0
qtd_homem_br=0
qtd_idosos=0
soma_idade=0

while cont<6:
    idade=int(input("Digite sua idade: "))
    nacionalidade=input("Digite sua nacionalidade: ")
    sexo=input("Digite seu sexo: ")
    
    if nacionalidade=="Brasileiro" and sexo=="Masculino" and 20<idade<30:
        qtd_homem_br=qtd_homem_br+1
        
    if (nacionalidade=="Brasileiro" or nacionalidade=="Italiano" or nacionalidade=="Francês") and idade>=65:
        qtd_idosos=qtd_idosos+1
        
    soma_idade=soma_idade+idade
    cont=cont+1
        
    soma_idade=soma_idade+idade
    
print("Quantidade de homens brasileiros que têm entre 20 e 30 anos: ", qtd_homem_br)
print("A quantidade de idosos com 65 anos ou mais que são brasileiros, italianos ou franceses: ", qtd_idosos)
print("Média das idades:", soma_idade/6)


8- Você precisa implementar um programa que leia duas notas de 30 pessoas, calcule e, para cada uma delas:
a. informe se as notas digitadas são válidas ou inválidas, ou seja, estão entre 0 e 10;
b. se forem válidas:
i. apresente a média;
ii. Informe se a pessoa foi classificada (media >= 6.0) ou desclassificada.

cont=0

while cont<30:
    nota1=float(input("Insira o valor da primeira nota: "))
    nota2=float(input("Insira o valor da segunda nota: "))
    
    if 0<=nota1<=10 and 0<=nota2<=10:
        media=(nota1+nota2)/2
        print("Sua média foi: ", media)
        
        if media>=6:
            print("Parabéns, classificado!")
        else:
            print("Desclassificado.")
    
    else: 
        print("Insira uma nota válida")
        
    cont=cont+1
        
