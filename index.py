from adicao import adicao
from sub import sub
from mult import mult
from div import div

OPERATIONS = ['+', '-', 'x', '÷']
isExit: bool = False
result: int or bool = False


while isExit == False:
    operation: str = input('Digite a operação que você quer fazer \nOu para sair, digite "sair" \n').lower().strip()
    
    if operation == 'sair':
        isExit = True
        break
    
    if operation in OPERATIONS:
        if operation == '+':
            number1Input: int = int(input('\nInsira o número a ser somado: \n'))
            
            if result:
                result = adicao(result, number1Input)
                
            else:
                number2Input: int = int(input('\nInsira outro número a ser somado: \n'))
                
                result = adicao(number1Input, number2Input)
                
                
        elif operation == '-':
            number1Input: int = int(input('\nInsira o número a ser subtraído: \n'))
            
            if result:
                result = sub(result, number1Input)
                
            else:
                number2Input: int = int(input('\nInsira outro número a ser somado: \n'))
                
                result = sub(number1Input, number2Input)
                
        elif operation == 'x':
            number1Input: int = int(input('\nInsira o número a ser multiplicado: \n'))
            
            if result:
                result = mult(result, number1Input)
                
            else:
                number2Input: int = int(input('\nInsira outro número a ser somado: \n'))
                
                result = mult(number1Input, number2Input)
                
        else:
            number1Input: int = int(input('\nInsira o número a ser dividido: \n'))
            
            if result:
                result = div(result, number1Input)
                
            else:
                number2Input: int = int(input('\nInsira outro número a ser somado: \n'))
                
                result = div(number1Input, number2Input)
                
            
        print('\nO resultado foi: %s \n' %(int(result)))
        operation = ''
    else:
        print('\nEssa operação não existe. Digite: + para adição, - para subtração, x para multiplicação ou ÷ para divisão')
        break