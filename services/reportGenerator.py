# https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c

def write_report(data):
    report_data = calculate_fscore(data)
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
    tn = data['TN'] # Not required?
    fn = data['FN']

    # Caclulate precsion and recall for the fscore calculation
    precision = calculate_accuracy(tp, fn)
    recall = calculate_recall(tp, fp)

    #print(f"\tcalculating F-Score on {precision}, {recall}")
    data['f_score'] = 2 * (precision * recall) / (precision + recall)

    return data
    