def parsed_data(precision, recall):
    print(f"\tcalculating F-Score on {precision}, {recall}")
    f_score = 2 * (precision * recall) / (precision + recall)

    data = {
        "Precision" : precision,
        "Recall" : recall,
        "FScore" : f_score
    }

    return data