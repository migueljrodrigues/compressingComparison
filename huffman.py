from heapq import heappush, heappop, heapify
from collections import defaultdict
from nltk.corpus import gutenberg
import os,sys

def decode(ciphered, frequencies):
	#troca k por value para aceder mais facilmente
    decoded = {value:key for key, value in frequencies.items()}
    code = ''
    plain = ''
    listPlain = []
    #percorre o 'array'. se encontrar alguma palavra:
    #1 - da a mesma
    #2 - limpa o code
    #3 - segue para a proxima
    for i in range(len(ciphered)):
        code += ciphered[i]
        if code in decoded:
            #print type(plain),plain
            #print type(decoded[code]),decoded[code]
            try:
                plain += decoded[code]
            except:
                listPlain.append(decoded[code])

            code = ''
    return plain if len(plain) != 0 else listPlain

#melhorar
def encode(frequencies):
    #print frequencies
	#cria a stack
    stack = [[w, [sm, ""]] for sm, w in frequencies.items()]
    #transforma numa heap, para ir tirando os valores mais acima
    heapify(stack)
    while len(stack) > 1:
    	#retira os dois valores menos frequentes
        left = heappop(stack)
        right = heappop(stack)
        #ao(s) da esquerda acrescenta 0
        for par in left[1:]:
            par[1] = '0' + par[1]
        #ao(s) da direita acrescenta 1
        for par in right[1:]:
            par[1] = '1' + par[1]
        #soma as frequencias [0] e mete os elementos respectivos [1]
        heappush(stack, [left[0] + right[0]] + left[1:] + right[1:])
    #retorna resultado ordenado
    #print stack
    return sorted(heappop(stack)[1:], key=lambda p: (len(p[-1]), p))

def makeFrequencies(txt):

    freqs = defaultdict(int)

    #frequencias dos caracteres
    for ch in txt:
        freqs[ch] += 1

    huff = encode(freqs)

    response = {}
    #tentar sem este 
    for p in huff:
        response[p[0]] = p[1]

    print 'Dict Size:' + str(sys.getsizeof(response))

    return response

