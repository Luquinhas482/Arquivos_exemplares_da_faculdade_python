#Arquivo contendo um loop simples e sem uma saida da chave while
#A formula que esta em loop em questão se trata de uma questão de bascara


print('')
    
print('===============BEM-VINDO A MINHA CALCULADORA!===============')
print('')
print('')
print('')

import time #o import time serve para trazer uma linha temporal para o codigo, desta maneira, utilizando o time.sleep 
            #é possivel estabelecer um intervalo em algum momento de sua execução, comumento usado para loops como o desta formula. 


while True:
        
    a = input('Digite o seu valor primeiro(A): ')
    a = float(a)        
    print('')

    b = input('Digite o seu valor secundo(B): ')
    b = float(b)
    print('')
    
    c = input ('Digite seu valor terceiro(C): ')
    c = float(c)
    print('')

    x = (b*(-1)) + (b**2 - 4*a*c)**1/2
            
    x2 = (b*(-1)) - (b**2 - 4*a*c)**1/2

    print('O valor de -X é: ',x,' e o valor de +X é: ',x2)
    print('')
        

    print('===============CONTA FINALIZADA COM SUCESSO!===============')
    print('')
        
    print('Aguarde alguns instantes para realizar outro calculo!')
    print('')
        
    time.sleep(2)
