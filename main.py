import pandas as pd
from nltk.tokenize import sent_tokenize as st

# TODO make it so that the user can select any file.
def read_data():
    f = open('./data/horizons_test.txt', "r")
    text = f.read()
    
    #data = pd.DataFrame(text)
    #data.columns = ["text"]
    f.close()
    return text

def write_data():
    pass

def text_preProcessing(text):
    print("\t converting to lower case...")
    text_lower = text.lower()
    #print(text_lower)
    sentences = st(text_lower)
    number_sentences = len(sentences)
    print(f"\t number of sentences: {number_sentences}")
    print(sentences[0:5])


# The Main Function just calls the read data for now
def main():
    data = read_data()


    #print(f"Data: {data}")

    print("------------------------------")
    print("Finished Reading the Data... \n")

    print("Starting Pre-Processing...")
    text_preProcessing(data)

if __name__ == "__main__":
    main()