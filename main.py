import random
import string
import keyboard

asciiArt = '''

██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗           
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗          
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║          
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║          
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝          
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝           
                                                                             
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                        

'''

print(asciiArt)

def gerar_senha(comprimento, incluir_maisculas: True, incluir_minusculas: True, incluir_numeros: True,
                incluir_especiais: True):
    caracteres = ''

    if incluir_maisculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        return 'Nenhum caractere selecionado. Escolha pelo menos um tipo de caractere.'

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():

    dominio = input('Digite o nome do site: ')
    comprimento_senha = int(input('Digite a quantidade de digitos desejada: '))
    usar_maiuscula = input('Incluir letras maiúsculas? (S/N): ') == 's'
    usar_minusculas = input('Incluir letras minúsculas? (S/N): ') == 's'
    usar_numeros = input('Incluir números? (S/N): ') == 's'
    usar_especiais = input('Incluir caracteres especiais? (S/N): ') == 's'


    if usar_maiuscula or usar_minusculas or usar_numeros or usar_especiais:
        senha_gerada = gerar_senha(comprimento_senha, usar_maiuscula, usar_minusculas, usar_numeros, usar_especiais)
        with open('password.txt', 'a') as file:
            file.write(f'{senha_gerada} - {dominio}')
        print(f'Sua senha segura gerada é: {senha_gerada} - {dominio}')
        print('Senha salva em "password.txt"')
        print('')
        print('Pressione ENTER para fechar o programa.')
        keyboard.wait('enter')
    else:
        print('Nenhum caractere selecionado. Escolha pelo menos um tipo de caractere.')
        print('Pressione ENTER para fechar o programa.')
        keyboard.wait('enter')

if __name__ == '__main__':
    main()