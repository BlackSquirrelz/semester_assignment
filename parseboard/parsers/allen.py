from nltk import word_tokenize
import nltk
from allennlp.predictors.predictor import Predictor

"""
https://github.com/allenai/allennlp
Known Issues: This part doesn't seem to be working properly annymore.
"""


def parse_allen(article, model):

    tokens = word_tokenize(article)
    
    predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/biaffine-dependency-parser-ptb-2018.08.23.tar.gz")
    instance = predictor._dataset_reader.text_to_instance(tokens, nltk.pos_tag(tokens))

    result = predictor.predict_instance(instance)

    print(result)
    return result

