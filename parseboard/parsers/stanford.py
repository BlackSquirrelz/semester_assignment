"""
Stanford Parser to do the baseline parsing.

https://github.com/stanfordnlp/stanza/

"""

import pandas as pd


def parse_stan(article, model):
    doc = model(article)
    text = [word.text for sent in doc.sentences for word in sent.words]
    upos = [word.upos for sent in doc.sentences for word in sent.words]
    deprel = [word.deprel for sent in doc.sentences for word in sent.words]

    data = {
        'text': text,
        'upos': upos,
        'deprel': deprel
      }

    result = pd.DataFrame(data=data)
    # print(result)
    return result
