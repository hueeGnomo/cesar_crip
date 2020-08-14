#!/bin/python


'''
Description :: Simple Caesar Cipher Program
Author :: Gnomo
Version :: 1.0
'''
'''
Lista de argumentos

    -t
        texto para criptografar

    -f
        arquivo contendoo texto a ser criptgrafado

    -d
        descriptografar arquivo ou texto com a chave

    -k
        chave para criptografar ou descriptografar o texto

    -h
        mostra o texto de ajuda
'''
import sys

args = sys.argv

def usage():
    print('caesar_cipher.py [OPTION] [FILE/TEXT]\n\nOPTIONS\n-t\n\ttexto para criptografar\n\n-f\n\tarquivo contendo o texto a ser criptgrafado\n\n-d\n\tdescriptografar arquivo ou texto com a chave\n\n-k\n\tchave para criptografar ou descriptografar o texto\n\n-h\n\tmostra este texto')

def bad_usage():
    print('Bad usage')
    usage()

def encode(txt, key):

    #Var para receber o resultado
    result = ''

    #Var para saber se a letra atual e maiuscula(True) ou minuscula(False)
    isup = False

    for letter in txt:

        #Identificar se e uma letra do alfabeto
        if ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122:

            #Identificar se a letra e maiuscula ou nao
            if letter.isupper():
                isup = True
            else:
                isup = False

            #Magica da rotacao das letras
            if ord(letter.lower()) + key > 122:
                letter = chr((96-(122-ord(letter)))+key)

            else:
                letter = chr(ord(letter)+key)

            #Concatenar a letra atual com o texto final
            if isup:
                result += letter.upper()
            else:
                result += letter.lower()

        else:
            result += letter

    return result

def main():

    txt = None
    key = None

    #Lista de argumentos validos
    args_lst = ['-t', '-f', '-k', '-d', '-h']

    #Variavel para indicar se o argumento e um metodo(True) ou um valor de metodo(False).
    method = True

    #Variavel para indicar se objeto sera codificado(False) ou decodificado(True).
    dec = False



    #Inicio do bloco que processa os argumentos ==========

    #Verifica se existem argumentos
    if len(args) == 1:
        bad_usage()
        return 1

    #Argumento por argumento
    for arg in args[1::]:
        if method:
            next_arg = args[args.index(arg)+1]

            #Verifica se o argumento atual e valido
            if arg in args_lst:

                #Verifica argumentos duplicados 
                if args.count(arg) > 1:
                    bad_usage()
                    return 1

                #Identifica os argumentos
                else:
                    if arg == '-k':

                        if not next_arg.isdigit():
                            bad_usage()
                            return 4

                        key = int(next_arg)
                        method = False

                    #elif arg == '-f':
                        #print('coming soon ;)')
                        #txt = read_file(next_arg)
                        #method = False

                    elif arg == '-t':
                        txt = next_arg
                        method = False

                    elif arg == '-d':
                        dec = True

                    elif arg == '-h':
                        usage()
                        return 0
            else:
                bad_usage()
                return 1

        else:
            method = True

    #Fim do bloco que processa os argumentos ==============

    #Verifica se as variaveis estao certas
    if key == None or txt == None:
        bad_usage()
        return 2


    #Chamada da funcao que codifica/decodifica os objetos =
    if dec:
        print('coming soon ;)')
        #result = (decode(txt, key))
    else:
        result = (encode(txt, key))


    print(result)













if __name__ == '__main__':
    main()

