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
    
    #Var para saber se a letra atual é maiuscula(True) ou minuscula(False)
    isup = False

    for letter in txt:
        if letter.isupper():
            isup = True
        else:
            isup = False

        if ord(letter.lower())+key > 122:
            letter = chr(ord(letter)-key)

    

def main():
    
    txt = None
    key = None
    
    #Lista de argumentos válidos
    args_lst = ['-t', '-f', '-k', '-d']
    
    #Variável para indicar se o argumento é um metodo ou um valor de metodo. Se True é um metodo, se False é um valor
    method = True
    
    #Variável para indicar se objeto será codificado ou decodificado. Se True sera codificado, se False será decodificado
    encode = True
    


    #Início do bloco que processa os argumentos ==========

    #Verifica se existem argumentos
    if len(args) == 1:
        bad_usage()
        return 1
    
    #Argumento por argumento
    for arg in args[1::]:
        if method:
            next_arg = args[args.index(arg)+1]

            #Verifica se o argumento atual é válido
            if arg in args_lst:
                
                #Verifica argumentos duplicados 
                if args.count(arg) > 1:     
                    bad_usage()
                    return 1
                
                #Identifica os argumentos
                else:
                    if arg == '-k':
                        print('arg is k =>',arg)#@@@@@@@@@@@
                        if not next_arg.isdigit():
                            bad_usage()
                            return 4

                        key = next_arg
                        method = False

                    #elif arg == '-f':
                        #txt = read_file(next_arg)
                        #method = False

                    elif arg == '-t':
                        print('arg is t =>',arg)#@@@@@@@@@@@
                        txt = next_arg
                        method = False

                    elif arg == '-d':
                        encode = False
                
            else:
                bad_usage()
                return 1
 
        else:
            method = True
    
    #Fim do bloco que processa os argumentos ==============

    #Verifica se as variáveis estão certas
    if key == None or txt == None:
        print(key, txt)
        bad_usage()
        return 2

    print('key:',key,'\ntxt:',txt)
    
    #Chamada da função que codifica/decodifica os objetos =
    #result = rotate(txt, key, encode)
    rotate(txt, key, encode)


        
        

                

            






if __name__ == '__main__':
    main()

