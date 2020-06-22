from parseboard.parsers import spacyparser, stanford
import pandas as pd

# Import Parsers
import stanza
import spacy
import en_core_web_sm
import de_core_news_sm 
import fr_core_news_sm

languages = ['en', 'de', 'fr']

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

    config = "tokenize,mwt,pos,lemma,depparse"

    nlp_en = stanza.Pipeline(lang='en', processors=config)
    nlp_de = stanza.Pipeline(lang='de', processors=config)
    nlp_fr = stanza.Pipeline(lang='fr', processors=config)

    df_stanford_en = stanford.parse_stan(article_en, nlp_en)
    df_stanford_de = stanford.parse_stan(article_de, nlp_de)
    df_stanford_fr = stanford.parse_stan(article_fr, nlp_fr)
    
    """
    Spacy Parser:
    Define Spacy Models, Assign Dataframe to List
    """

    df_spacy_de = spacyparser.parse_spacy(article_de, de_core_news_sm.load())
    df_spacy_en = spacyparser.parse_spacy(article_en, en_core_web_sm.load())
    df_spacy_fr = spacyparser.parse_spacy(article_fr, fr_core_news_sm.load())

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

    allen_scores = [0,0,0]
    spacy_scores = []
    stanford_scores = [1,1,1]

    spacy_de_scores = df_complete_de.spacy_eval.value_counts().tolist()
    spacy_en_scores = df_complete_en.spacy_eval.value_counts().tolist()
    spacy_fr_scores = df_complete_fr.spacy_eval.value_counts().tolist()

    spacy_de_score = calculate_score(spacy_de_scores[0], spacy_de_scores[0] + spacy_de_scores[1])
    spacy_en_score = calculate_score(spacy_en_scores[0], spacy_en_scores[0] + spacy_en_scores[1])
    spacy_fr_score = calculate_score(spacy_fr_scores[0], spacy_fr_scores[0] + spacy_fr_scores[1])

    spacy_scores.append(spacy_de_score)
    spacy_scores.append(spacy_en_score)
    spacy_scores.append(spacy_fr_score)
    
    
    # The Report Data sets Stanford Parser Output to 100 by default, as it is the parser we wan't to compare against. The other parsers are set by their values of true and false in comparison to the stanford parser
    report_data = {'de_stan': stanford_scores[0], 'en_stan': stanford_scores[1], 'fr_stan': stanford_scores[2], 'de_spacy': spacy_scores[0], 'en_spacy': spacy_scores[1], 'fr_spacy': spacy_scores[2], 'de_allen': allen_scores[0], 'en_allen': allen_scores[1], 'fr_allen': allen_scores[2]}
    # report_data = {'de_stan': 100, 'en_stan': 100, 'fr_stan': 100, 'de_spacy': 93.2, 'en_spacy': 92.6, 'fr_spacy': 90.7, 'de_allen': 87.9, 'en_allen': 88.6, 'fr_allen': 90.2}
    return(report_data)


def calculate_score(true_values, total):
    percentage = true_values / total
    return percentage
