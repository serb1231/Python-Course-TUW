import wikipedia
import random
import urllib
def cuv_cautate_k(lista,k = 10):
    etc = []
    for i in range(k):
        etc.append(lista[len(lista)-i-1])
    return etc

def numarare_cuvinte(lista):
    dictionar = dict([])
    for i in lista:
        if i in dictionar:
            dictionar[i]+=1
        else:
            dictionar[i] = 1
    dictionar_sortat = sorted(dictionar.items(), key = lambda x:x[1])
    lista = []
    for i in dictionar_sortat:
        lista.append(i)
    return dictionar_sortat
        
def get_corpus_word_frequencies(corpus =10000):
    letters = "aeioubcdfglj"
    world_length = [2,3,4,5,6,7]
    pages = []
    attempts = 200
    txt = ""
    wikipedia.set_lang('hi')
    for i in range(attempts):
        wrld_lenth = random.choice(world_length)
        new_world = ""
        for j in range(wrld_lenth):
            new_world = new_world+random.choice(letters)
        results = wikipedia.search(new_world, results = 5)
        for j in results:
            if wikipedia.suggest(j)==None:
                try:
                    txt = txt + wikipedia.page(j).content
                except wikipedia.DisambiguationError as e:
                    s = random.choice(e.options)
                    txt = txt + wikipedia.page(s).content
                pages.append(j)
            if len(txt) > corpus:
                break
        if len(txt) > corpus:
            break
    lista = txt.split()
    lista_buna = numarare_cuvinte(lista)
    final_aproape = cuv_cautate_k(lista_buna,30)
    return final_aproape
top_words_and_freqs = get_corpus_word_frequencies(10000)
for i,j in top_words_and_freqs:
    print(i,"   ",j)
#print(top_words_and_freqs)
