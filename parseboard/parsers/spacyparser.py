"""
NLP Pipeline spaCy: Tokenizer, Lemmatiser, PoS-Tagger, Dependency Parsing + Visualization
"""

from typing import List, Tuple
from argparse import ArgumentParser, FileType

import spacy

nlp = spacy.load('en')


def parse_spacy(article):
    article = "This is a test article"
    article_tokenized = tokenize(article)
    article_lemmatized = lemmatise(article_tokenized)
    result = article_lemmatized
    return result


def tokenize(article: str) -> List[Tuple[str, str]]:
    """Textfile to Doc, tokenize"""
    with open(article, 'r', encoding='utf-8') as f:
        for line in f:
            word = nlp(f)
    for token in word:
        print(token)
    return token


def lemmatise(article: str) -> List[Tuple[str, str]]:
    """
    Lemmatise an article.

    :param article: The article to be lemmatised.
    :return: A list of (token, lemma) tuples.
    """

    token_lemma_tuples = []
    for token in nlp(article):
        token_lemma_tuples.append((token.text, token.lemma_))
    return token_lemma_tuples


""" def main():
    parser = ArgumentParser(description="Lemmatise an English article.")
    parser.add_argument('article', type=FileType('r'), help="The article to lemmatise.")
    args = parser.parse_args()
    for token in tokenize(args.article):
        print(token)
#    for token, lemma in lemmatise(args.article):
#        print(f'{token}\t{lemma}') """


def evaluation():
    pass
