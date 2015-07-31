# -*- coding:utf-8 -*-
import math

def eh_palindromo(texto):
    texto = texto.replace(" ", "")
    letras = list(texto)

    # string vazia ou com 1 caracter
    if len(letras) in [0, 1]:
        return True

    # Mais de 1 caracter
    crescente = 0
    decrescente = len(texto) -1

    while True:
        if texto[crescente] != texto[decrescente]:
            return False

        crescente = crescente + 1
        decrescente = decrescente - 1

        if (crescente == decrescente):
            # Texto com numero par de caracteres. Ex: 1221
            break

        if math.fabs(decrescente - crescente) == 1:
            # Texto com numero ímpar de caracteres. Ex: 12321
            break
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