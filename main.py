#!/bin/python

def helloWorld():
    print("Hello World")


def functionIMC(x,y):
    '''
    \'\'\' serve para abrir um comentário multilinha. Se estiver abaixo de uma funcao, classe ou metodo definidos, irao ser descritos por isso.
    Função para IMC    
    #x = altura em centimetros
    #y = peso
    '''
    return x**2 / y

def calculoArea(base, altura, tipo):
    tipo = tipo.lower()
    if type(altura) == "int" or type(altura) == "float":
        if tipo == "triangulo":
            return base * altura /2
        elif tipo == "quadrado" or tipo == "retangulo":
            return base * altura
        else:
            return "Não consigo entender o tipo"

def lista(x):
    '''Printa todos os elementos de uma lista
    separadamente'''
    for val in x:
        print(val)


if __name__ == "__main__":

    x = calculoArea(1, 1, "triangulo")
    print(x)