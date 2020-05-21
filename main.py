import sqlite3
from sqlite3 import Error
import pandas as pd
from Article import Article
import database

DATABASE = r"articles.db"

# TODO make it so that the user can select any file.
def read_data(file_name):
    f = open(file_name, "r")
    print(f"\t {file_name}")
    text = f.read()
    
    #data = pd.DataFrame(text)
    #data.columns = ["text"]
    f.close()
    return text

def write_data_toDB(test_file):
    
    conn = database.create_connection(DATABASE)
    with conn:
        # create a new article
        # (issue, article_number, language, title, author, body):
        article = ('issue_TEST', 'article_aTest','de', "Test Article", "Tobias Weisskopf", "Lorem Ipsum" );
        article_id = database.create_article(conn, article)
        print(article_id)


# Create an instance of Article -> '(self, issue, article_number, language, title, author, body):'
    test_case =  Article('issue_TEST', 'article_aTest','de', "Test Article", "Tobias Weisskopf", test_file) 
    print(test_case.author)

def parser_compare(text):
    pass

# The Main Function just calls the read data for now
def main():

    database.make_database()

    file_name = './data/original_data/text-files/issue_109/article_a1/de.txt'
    print(file_name)
    test_file_name = './data/test_data/horizons_test.txt'

    # Reading the file section
    print("Reading the Data...")
    test_file = read_data(test_file_name)
    
    # Create an instance of Article -> '(self, issue, article_number, language, title, author, body):'
    test_case =  Article('issue_TEST', 'article_aTest','de', "Test Article", "Tobias Weisskopf", test_file) 
    print(test_case.author)

    write_data_toDB(test_file)
    
    print("Finished Reading the Data... \n")
    print("------------------------------")

    # Text Statistics
    print("Printing stats... \n")
    test_case.stats()
    print("------------------------------")

    # TODO Store each of the sentences in a pandas dataframe for easy access
    # df = pd.DataFrame(data, index=[0], columns=["raw"])
    
    # Pre-Processing Section
    print("Starting Pre-Processing...")
    #test_case.text_preProcessing()

    print("Finished Pre-Processing...\n")
    print("------------------------------")
    
    print("Finished Program")

if __name__ == "__main__":
    main()