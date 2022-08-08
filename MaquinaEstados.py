# Gabriel Antonio Gomes de Farias

'''
ENUNCIADO
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá determinar se uma string de
entrada
faz
parte
da
linguagem
𝐿
definida
por
𝐿 = {𝑥 | 𝑥 ∈
{𝑎, 𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto Σ = {𝑎, 𝑏, 𝑐}.
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que
podem existir em um arquivo de testes para o programa que você irá desenvolver:
3
abbaba
abababb
bbabbaaab
Neste exemplo temos 3 strings de entrada. O número de strings em cada arquivo será
representado por um número inteiro positivo. A resposta do seu programa deverá conter uma, e
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
da validação conforme o formato indicado a seguir:
abbaba: não pertence.
A saída poderá ser enviada para um arquivo de textos, ou para o terminal padrão e será
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
'''


def verifica_string(string):
    string = string.lower()  # deixa texto de entrada minisculo caso esteja maiusculo

    alfabeto = ['a', 'b', 'c']  # alfabeto possivel utilizado no enunciado
    tamanho_str = len(string)  # tamanho da string

    resultado = False  # verifica o resultado da checagem

    for l in range(0, tamanho_str):
        # percorre cada simbolo da string

        letra = string[l]

        if letra not in alfabeto:
            # se n estiver no alfabeto ent ñ é valido
            return False
        elif letra == "a":
            '''
            no caso a se as duas proximas n forem b deve ser falso
            '''
            if l == tamanho_str - 1 or l == tamanho_str - 2:
                return False
            if string[l + 1] == "b" and string[l + 2] == "b":
                resultado = True
            else:
                return False
    return resultado

def verificar_arquivo(arquivo):
    with open(arquivo) as texto:
        strings = texto.readlines()
        try:
            qtd_strings = int(strings[0])
            if len(strings) == qtd_strings + 1:
                cont = 1

                while cont <= qtd_strings:
                    string = strings[cont].strip('\n')
                    verificao = verifica_string(string)

                    if verificao:
                        print(f'{string}: pertence.')
                    else:
                        print(f'{string}: não pertence.')
                    cont += 1
            else:
                print("Não possui palavras")
        except:
            print("Arquivo não indicou número de strings.")


arquivo = "teste1.txt"  # nome do arquivo txt deve pertencer no diretório do código
verificar_arquivo(arquivo)
