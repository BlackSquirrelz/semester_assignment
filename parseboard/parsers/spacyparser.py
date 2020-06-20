"""
NLP Pipeline spaCy: Tokenizer, Lemmatiser, PoS-Tagger, Dependency Parsing + Visualization

https://spacy.io/

"""
import pandas as pd


def parse_spacy(article, model):
    text = []
    upos = []
    deprel = []

    doc = model(article)

    for token in doc:
        text.append(token)
        upos.append(token.pos_)
        deprel.append(token.dep_)

    data = {
        'sp_text': text,
        'sp_upos': upos,
        'sp_deprel': deprel
      }
    result = pd.DataFrame(data=data)
    # print(result)
    return result
