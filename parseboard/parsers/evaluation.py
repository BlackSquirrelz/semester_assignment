from parseboard.parsers import spacyparser

# https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c
def evaulate_parsers(article_de, article_en, article_fr):

    # Get all articles from the database
    print(f"German Article to parse: {article_de.body}")
    print(f"English Article to parse: {article_en.body}")
    print(f"French Article to parse: {article_fr.body}")

    # report_data = calculate_fscore()

    # TODO Call Spacy
    spacy_scores = []
    spacy_scores.append(spacyparser.parse_spacy_de(article_de.body))
    spacy_scores.append(spacyparser.parse_spacy_en(article_en.body))
    spacy_scores.append(spacyparser.parse_spacy_fr(article_fr.body))

    # TODO Call Allen
    
    # TODO Call Stanford
    report_data = {'de': spacy_scores[0], 'en': spacy_scores[1], 'fr': spacy_scores[2]}

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
