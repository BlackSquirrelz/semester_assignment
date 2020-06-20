"""
Stanford Parser to do the baseline parsing.
https://github.com/stanfordnlp/stanza/
"""

import stanza


def parse_stan_en(article):
    # stanza.download('en')
    result = []
    nlp_en = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse')
    doc = nlp_en(article)
    result = [{'text': word.text, 'upos': word.upos, 'deprel': word.deprel} for sent in doc.sentences for word in sent.words]
    return result


def parse_stan_de(article):
    result = []
    # stanza.download('de')
    nlp_de = stanza.Pipeline(lang='de', processors='tokenize,pos,lemma,depparse')
    doc = nlp_de(article)
    result = [{'text': word.text, 'upos': word.upos, 'deprel': word.deprel} for sent in doc.sentences for word in sent.words]
    #for word in doc:
    #    result.append({'text': word.text, 'upos': word.upos, 'deprel': word.deprel})
    return result


def parse_stan_fr(article):
    # stanza.download('fr')
    result = []
    nlp_fr = stanza.Pipeline(lang='fr', processors='tokenize,pos,lemma,depparse')
    doc = nlp_fr(article)
    result = [{'text': word.text, 'upos': word.upos, 'deprel': word.deprel} for sent in doc.sentences for word in sent.words]
    return result
