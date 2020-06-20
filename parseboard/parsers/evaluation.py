from parseboard.parsers import spacyparser, stanford


# https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c
def evaulate_parsers(article_de, article_en, article_fr):

    # Get all articles from the database
    print(f"German Article to parse: {article_de}")
    print(f"English Article to parse: {article_en}")
    print(f"French Article to parse: {article_fr}")

    # report_data = calculate_fscore()

    # TODO Call Spacy
    spacy_scores = []
    # spacy_scores.append(spacyparser.parse_spacy_de(article_de.body))
    # spacy_scores.append(spacyparser.parse_spacy_en(article_en.body))
    # spacy_scores.append(spacyparser.parse_spacy_fr(article_fr.body))

    spacy_scores.append(spacyparser.parse_spacy_de(article_de))
    spacy_scores.append(spacyparser.parse_spacy_en(article_en))
    spacy_scores.append(spacyparser.parse_spacy_fr(article_fr))

    # TODO Create AllenNLP Parsing Function, and call the proper values....
    allen_scores =[]
    allen_scores.append(50)
    allen_scores.append(60)
    allen_scores.append(70)

    
    # Stanford Calculations are the baseline for comparison.
    stanford_scores = []
    stanford_scores.append(stanford.parse_stan_de(article_de))
    stanford_scores.append(stanford.parse_stan_en(article_en))
    stanford_scores.append(stanford.parse_stan_fr(article_fr))

    report_data = {'de_stan': stanford_scores[0], 'en_stan': stanford_scores[1], 'fr_stan': stanford_scores[2], 'de_spacy': spacy_scores[0], 'en_spacy': spacy_scores[1], 'fr_spacy': spacy_scores[2], 'de_allen': allen_scores[0], 'en_allen': allen_scores[1], 'fr_allen': allen_scores[2]}

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
