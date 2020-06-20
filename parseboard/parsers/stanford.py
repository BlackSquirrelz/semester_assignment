"""
Stanford Parser to do the baseline parsing.
https://github.com/stanfordnlp/stanza/
"""

import stanza

# Load Models
stanza.download('en')
stanza.download('de')
stanza.download('fr')

nlp_en = stanza.Pipeline('en')
nlp_de = stanza.Pipeline('de')
nlp_fr = stanza.Pipeline('fr')


def parse_stan_en(article):
    doc = nlp_en(article)
    doc.sentences[0].print_dependencies()
    result = 10
    print(doc)
    return result


def parse_stan_de(article):
    doc = nlp_de(article)
    doc.sentences[0].print_dependencies()
    result = 20
    print(doc)
    return result


def parse_stan_fr(article):
    doc = nlp_fr(article)
    doc.sentences[0].print_dependencies()
    result = 30
    print(doc)
    return result
