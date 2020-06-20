"""
NLP Pipeline spaCy: Tokenizer, Lemmatiser, PoS-Tagger, Dependency Parsing + Visualization
"""

# TODO Replace result with something useful...
import spacy

# Load Spacy Models
nlp_en = spacy.load('en_core_web_sm')
nlp_fr = spacy.load('fr_core_news_sm')
nlp_de = spacy.load('de_core_news_sm')


def parse_spacy_en(article):
    doc = nlp_en(article)
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
        
    result = 1
    return result


def parse_spacy_de(article):
    doc = nlp_de(article)
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
    result = 7
    return result


def parse_spacy_fr(article):
    doc = nlp_fr(article)
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
    result = 3
    return result
