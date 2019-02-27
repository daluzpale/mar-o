import sys
print("Qual é o seu nome?")
nome = input()
if (len(nome) <=6 ) or (len(nome) >=30):
   print("Nome menor que 6 caracteres ou maior que 30 caracteres")
   sys.exit(1)
 
print("Qual é o seu apelido?")
apelido = input()
if  (len(apelido) <=2 ) or (len(apelido) >=20):
    print("Apelido inválido")
    sys.exit(1)

print("Qual é a sua idade?")
idade = int(input())
if (idade <=0 ) or (idade >=150):
   print("Idade menor que o ou maior que 150")
   sys.exit(1)
   
print("Qual é o seu peso?")
peso = float(input())
if  peso <=0:
    print("Peso menor que zero")
    sys.exit(1)
    
print("Qual é a sua altura?")
altura = float(input())
if  altura <=0:
     print("Altura menor que zero")
     sys.exit(1)
     
print("Qual é o seu sexo?")
sexo = str(input())
if  (sexo  != "M") and (sexo  != "F"):
    print("Sexo diferente de M ou F")
    sys.exit(1)
    
print("Nome: ",nome)
print("Apelido: ",apelido)
print("Idade: ",idade)
print("Peso: ",peso)
print("Altura: ",altura)
print("Sexo: ",sexo)




