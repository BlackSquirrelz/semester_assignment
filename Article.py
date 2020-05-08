from nltk.tokenize import sent_tokenize as st

class Article:
    kind =  "text"
    
    def __init__(self, text, lang):
        self.text =  text
        self.language = lang

# def text_preProcessing(self, text):
# # Convert Everything to Lower Case
# print("\t converting to lower case...")
# text_lower = text.lower()
# #print(text_lower)

# # Sentence Parsing
# print("Text stats:\n")
# sentences = st(text_lower)
# number_sentences = len(sentences)
# print(f"\t number of sentences: {number_sentences}")
# print(sentences[0:1])

# # TODO Store each of the sentences in a pandas dataframe for easy access
# # df = pd.DataFrame(data, index=[0], columns=["raw"])
