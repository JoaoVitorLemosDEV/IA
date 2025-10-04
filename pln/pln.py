from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

LINGUAGEM = 'portuguese'

def iniciar():
    classificacoes, palavras_de_parada = None, None

    palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))

    classificacoes = {}
    for palavra, classificacao in floresta.tagged_words():
        classificacoes[palavra] = classificacao

    return classificacoes, palavras_de_parada

def tokenizar(texto):
    tokens = word_tokenize(texto, language=LINGUAGEM)

    return tokens

def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_filtrados = []

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

def classificar_tokens(tokens, classificacoes):
    tokens_classificados = {}

    for token in tokens:
        if token in classificacoes.keys():
            classificacao = classificacoes[token]
            tokens_classificados[token] = classificacao
        else:
            tokens_classificados[token] = "Sem classificação"

    return tokens_classificados

def estemizar(tokens):
    estemizador = RSLPStemmer()
    tokens_estemizados = {}

    for token in tokens:
        tokens_estemizados[token] = estemizador.stem(token)

    return tokens_estemizados

if __name__ == '__main__':
    texto = "A verdadeira generosidade para com o futuro consiste em dar tudo ao presente e para o betinha não sobra nada, só o osso."

    classificacoes, palavras_de_parada = iniciar()

    tokens = tokenizar(texto.lower())
    print(tokens)

    tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
    print(tokens)

    tokens = classificar_tokens(tokens, classificacoes)
    print(tokens)

    tokens_estemizados = estemizar(tokens)
    print(tokens_estemizados)
