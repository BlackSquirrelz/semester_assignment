from parseboard.parsers import spacyparser, stanford
import pandas as pd

# Import Parsers
import stanza
import spacy


# https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c
def evaulate_parsers(article_de, article_en, article_fr):

    # Get all articles from the database
    # print(f"German Article to parse: {article_de}")
    # print(f"English Article to parse: {article_en}")
    # print(f"French Article to parse: {article_fr}")


    # TODO Create AllenNLP Parsing Function, and call the proper values....
    allen_scores = []
    allen_scores.append(50)
    allen_scores.append(60)
    allen_scores.append(70)

    # Stanford Parser Baseline CODE
    """
    The Stanford Parser is the Baseline for this Application, we compare every other parser to the output of the Stanford Parser.
    Define Models, Assign Dataframe to List
    """
    nlp_en = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse')
    nlp_de = stanza.Pipeline(lang='de', processors='tokenize,pos,lemma,depparse')
    nlp_fr = stanza.Pipeline(lang='fr', processors='tokenize,pos,lemma,depparse')

    df_stanford_en = stanford.parse_stan(article_en, nlp_en)
    df_stanford_de = stanford.parse_stan(article_de, nlp_de)
    df_stanford_fr = stanford.parse_stan(article_fr, nlp_fr)
    
    """
    Spacy Parser:
    Define Spacy Models, Assign Dataframe to List
    """

    # Load Spacy Models
    spacy_nlp_en = spacy.load('en_core_web_sm')
    spacy_nlp_fr = spacy.load('fr_core_news_sm')
    spacy_nlp_de = spacy.load('de_core_news_sm')

    df_spacy_de = spacyparser.parse_spacy(article_de, spacy_nlp_de)
    df_spacy_en = spacyparser.parse_spacy(article_en, spacy_nlp_en)
    df_spacy_fr = spacyparser.parse_spacy(article_fr, spacy_nlp_fr)

    # TODO
    # Evaluate Parsers against each other....
    df_complete_de = pd.concat([df_stanford_de, df_spacy_de], axis=1, sort=False)
    df_complete_en = pd.concat([df_stanford_en, df_spacy_en], axis=1, sort=False)
    df_complete_fr = pd.concat([df_stanford_fr, df_spacy_fr], axis=1, sort=False)

    # print("German Dataframe Combined")
    df_complete_de['spacy_eval_upos'] = df_complete_de['upos'].str.lower() == df_complete_de['sp_upos'].str.lower()
    df_complete_de['spacy_eval_deprel'] = df_complete_de['deprel'].str.lower() == df_complete_de['sp_deprel'].str.lower()
    df_complete_de['spacy_eval'] = df_complete_de['spacy_eval_upos'] == df_complete_de['spacy_eval_deprel']

    # print("English Dataframe Combined")
    df_complete_en['spacy_eval_upos'] = df_complete_en['upos'].str.lower() == df_complete_en['sp_upos'].str.lower()
    df_complete_en['spacy_eval_deprel'] = df_complete_en['deprel'].str.lower() == df_complete_en['sp_deprel'].str.lower()
    df_complete_en['spacy_eval'] = df_complete_en['spacy_eval_upos'] == df_complete_en['spacy_eval_deprel']

    # print("French Dataframe Combined")
    df_complete_fr['spacy_eval_upos'] = df_complete_fr['upos'].str.lower() == df_complete_fr['sp_upos'].str.lower()
    df_complete_fr['spacy_eval_deprel'] = df_complete_fr['deprel'].str.lower() == df_complete_fr['sp_deprel'].str.lower()
    df_complete_fr['spacy_eval'] = df_complete_fr['spacy_eval_upos'] == df_complete_fr['spacy_eval_deprel']

    # Evaluate the Parsers Against the Stanford Parse
    # print(df_stanford_de.equals(df_spacy_de))

    print(df_complete_de.spacy_eval.value_counts())
    print(df_complete_en.spacy_eval.value_counts())
    print(df_complete_fr.spacy_eval.value_counts())


    report_data = {'de_stan': 1, 'en_stan': 1, 'fr_stan': 1, 'de_spacy': 1, 'en_spacy': 1, 'fr_spacy': 1, 'de_allen': allen_scores[0], 'en_allen': allen_scores[1], 'fr_allen': allen_scores[2]}

    return(report_data)


def calculate_recall(tp, fn):
    rec = tp / (tp + fn)
    return rec


# True Positive, False Positive, True Negative, False Negative
# data[0], data[1], data[2], data[3]
def calculate_accuracy(tp, fp):
    prec = tp / (tp + fp)
    return prec


# Calculate FSCORE
def calculate_fscore(data):
    # LANG,PAR,TP,FN,TN,FP
    # De-list confusion matrix
    tp = data['TP']
    fp = data['FP']
    tn = data['TN']
    fn = data['FN']

    # Caclulate precsion and recall for the fscore calculation
    precision = calculate_accuracy(tp, fn)
    recall = calculate_recall(tp, fp)

    # print(f"\tcalculating F-Score on {precision}, {recall}")
    # data['f_score'] = 2 * (precision * recall) / (precision + recall)

    data = {
        'en': {'f_score': '1'},
        'fr': {'f_score': '0'},
        'de': {'f_score': '0.5'}
    }

    return data
