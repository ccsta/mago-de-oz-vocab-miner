import re
from collections import Counter
letra = """ 
¡Ponte en pie! alza el puño y ven
A la fiesta pagana, donde el niño, el
viejo y el hombre
pueblo el reino de la alegría.
Bebe, danza, sueña, siente que el
viento
Ha sido hecho para ti.
"""
def minerar_espanhol(texto):
    texto_limpo = re.sub(r'[¡!¿?.,;]', '', texto.lower())
    palavras = texto_limpo.split()

    stopwords = ['a', 'la', 'el', 'y', 'de', 'que', 'en', 'para', 'los', 'un', 'una', 'al', 'con', 'mi', 'tu', 'su']
    vocabulario_util = [p for p in palavras if p not in stopwords]
    ranking = Counter(vocabulario_util)

    print("--- RANKING DE VOCABULÁRIO ---")
    for palavra, frequencia in ranking.most_common(10):
        print(f"{palavra.upper()}:{frequencia}")
minerar_espanhol(letra)