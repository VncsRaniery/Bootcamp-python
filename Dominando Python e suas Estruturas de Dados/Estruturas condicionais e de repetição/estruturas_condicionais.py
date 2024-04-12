MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Digite sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você é maior de idade e pode tirar sua CNH!')

if idade < MAIOR_IDADE:
    print('Você é menor de idade e não pode tirar sua CNH!')    



if idade >= MAIOR_IDADE:
    print('Você é maior de idade e pode tirar sua CNH!')
else:
    print('Você é menor de idade e não pode tirar sua CNH!')    




if idade >= MAIOR_IDADE:
    print('Você é maior de idade e pode tirar sua CNH!')
elif idade == IDADE_ESPECIAL:
    print('Você é menor de idade, porém pode fazer aulas teóricas!')
else:
    print('Você é menor de idade e não pode tirar sua CNH!') 


   