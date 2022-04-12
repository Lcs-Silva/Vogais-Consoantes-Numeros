#Declaro uma lista com todas as vogais e outra com todos os números para usar de comparação
vogais = ['a','á','à','ã','â','e','é','i','í','o','ó','ô','õ','u','ú']
numeros = ['1','2','3','4','5','6','7','8','9']
#Declaro 5 contadores para armazenarem a quantidade de vogais, consoantes, números e espaços
contVogais = 0;
contConsoantes = 0;
contNumeros = 0;
contEspacos = 0;

#Peço para o usuário digitar uma frase de 30 caracteres no máximo
frase = input("Digite uma frase de no máximo 200 caracteres: ")

#Verifico se a frase digitada é maior do que 30 caracteres, se for, exibe a mensagem abaixo e fecha o programa
if len(frase) > 200:
    print("\n\nA frase possui mais que 500 caracteres!")
    input()
    exit()

#Realizo uma iteração em cada caractere da frase digitada, forço todas as letras ficarem minúsculas com a função lower()
for letra in frase.lower():

    #Verifico se a letra está contida na lsta de vogais declarada no início do programa e adiciono +1 ao contador
    if letra  in vogais:
       contVogais = contVogais + 1
    #Verifico se o caractere é um espaço em branco e adiciono +1 ao contador
    elif letra == ' ':
        contEspacos = contEspacos + 1;
    #Verifico se o caractere é um número, caso ele esteja contido na lista de números declarada, adiciona +1 ao contador
    elif letra in numeros:
        contNumeros = contNumeros + 1
    #Verifico se a letra não está contida na lista de vogais, se não estiver, é consoante, e adiciono +1 ao contador
    elif letra not in vogais: 
        contConsoantes = contConsoantes + 1
    #Verifico se o caractere é um espaço em branco e adiciono +1 ao contador
    elif letra == ' ':
        contEspacos = contEspacos + 1
    
print(f'\n\nA frase contém {contVogais} vogais, {contConsoantes} consoantes, e {contNumeros} números.')
input()