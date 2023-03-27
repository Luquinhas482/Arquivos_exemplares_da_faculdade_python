print('')
    
print('===============BEM-VINDO A MINHA CALCULADORA!===============')
print('')
print('')
print('')


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
    
#===============================================================================================    
    prossseguir = input("Digite (parar) para sair ou pressione enter para permanecer: ")
    if prossseguir == "parar":
        break

    else:
        
        continue    #A mudança feita neste loop, se trata de uma maneira de saida ou finalização de seu laço de repetição,
                    #a finalização do laço foi uma contribuiçãode um aluno na faculdade.
    
    print('')
    print('')
    
#===============================================================================================