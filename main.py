import pandas as pd
from Article import Article

# TODO make it so that the user can select any file.
def read_data(file_name):
    f = open(file_name, "r")
    print(f"\t {file_name}")
    text = f.read()
    
    #data = pd.DataFrame(text)
    #data.columns = ["text"]
    f.close()
    return text

def write_data():
    pass

def parser_compare(text):
    pass

# The Main Function just calls the read data for now
def main():

    file_name = './data/horizons_test.txt'

    # Reading the file section
    print("Reading the Data...")
    test_file = read_data(file_name)
    test_case =  Article(test_file)
    print(test_case.text)
    
    print("Finished Reading the Data... \n")
    print("------------------------------")
    
    # Pre-Processing Section
    print("Starting Pre-Processing...")
    #test_case.text_preProcessing()

    print("Finished Pre-Processing...\n")
    print("------------------------------")
    
    print("Finished Program")

if __name__ == "__main__":
    main()