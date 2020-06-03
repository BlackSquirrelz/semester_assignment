import pseudo_parser as pp

def write_report(data):
    print(data)
    precision = data[0]
    recall = data[1]
    report_data = pp.parsed_data(precision, recall)
    print(report_data)


    