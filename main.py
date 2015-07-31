# -*- coding:utf-8 -*-
import math

def calc_delta_meio(texto):
    return (len(texto) - 1) / 2

def eh_palindromo(texto):
    texto = texto.replace(" ", "")
    letras = list(texto)
    tam = len(letras)

    # string vazia ou com 1 caracter
    if tam in [0, 1]:
        return True

    # Mais de 1 caracter
    delta = 0
    meio = calc_delta_meio(texto)

    while delta <= meio:
        if texto[delta] != texto[tam - 1 - delta]:
            return False

        delta = delta + 1

    return True


if __name__ == "__main__":
    print eh_palindromo("12321"), True
    print eh_palindromo("123321"), True
    print eh_palindromo("1234567"), False
    print eh_palindromo(""), True
    print eh_palindromo("subi no onibus"), True
    print eh_palindromo("1"), True
    print eh_palindromo("12"), False
    print eh_palindromo("11"), True
    #print calc_delta_meio("121"), 1
    #print calc_delta_meio("1221"), 1
    #print calc_delta_meio("12"), 0
    #print calc_delta_meio("12321"), 2