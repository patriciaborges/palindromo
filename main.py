# -*- coding:utf-8 -*-


def eh_palindromo(texto):
    texto = list(texto.replace(" ", ""))
    return texto[::-1] == texto


if __name__ == "__main__":
    print eh_palindromo("12321"), True
    print eh_palindromo("123321"), True
    print eh_palindromo("1234567"), False
    print eh_palindromo(""), True
    print eh_palindromo("subi no onibus"), True
    print eh_palindromo("1"), True
    print eh_palindromo("12"), False
    print eh_palindromo("11"), True