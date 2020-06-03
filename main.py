# Database requirements
import sqlite3
from sqlite3 import Error
import database as db
import reportGenerator as rg

# System stuff
import os

# Other requirements
from Article import Article

# Authorship information
__author__ = "Tobias Weisskopf"
__copyright__ = "Copyright 2020, Semester Assignment"
__credits__ = ["Tobias Weisskopf", "Adriana Dragusha", 'Rodolfo Chavez']
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Tobias Weisskopf"
__status__ = "Dev"

#Define tha Database File as a Static File
DATABASE = r"articles.db"

# TODO make it so that the user can select any file.
def read_data(file_name): # Put XARGS here
    f = open(file_name, "r")
    print(f"\t {file_name}")
    text = f.read()
    
    #data = pd.DataFrame(text)
    #data.columns = ["text"]
    f.close()
    return text

def parser_compare(text):
    pass

# The Main Function just calls the read data for now
def main():
    issues = []
    articles = []
    
    # List all files in a directory using os.listdir
    basepath = './data/original_data/text-files'
    entries = os.scandir(basepath)
    print(f"Looking in {basepath} for issues:")

    # TODO: This can probably be optimized a bit... but not today
    # From the base directory look for all issues of the magazine and append them to the issues list
    for issue in entries:
        if (issue.name != ".DS_Store"):
            issues.append(issue.name)
            #print(f"\t found issue named:  {issue.name}")
    
    print(f'Found {len(issues)} issues in {basepath}!')
    issues.sort()
    print(issues)
    # With the issues list, look through all the articles directories, basepath and issue list
    for issue in issues:
        print(issue)
        articlepath = basepath + "/" + issue
        article_entries = os.scandir(articlepath)
        for article in article_entries:
            articles.append(article.name)
            print(f"\t\t found article {article.name} in {articlepath}.")
    articles.sort()
    print(f'Found: {len(articles)} articles in {len(issues)} issues!' )
    db.make_database()
    
    file_name = './data/original_data/text-files/issue_109/article_a1/de.txt'
    print(file_name)
    # test_file_name = './data/test_data/horizons_test.txt'

    # Reading the file section
    print("Reading the Data...")
    test_file = read_data(file_name)
    
    db.write_data_toDB(test_file)
    
    print("Finished Reading the Data... \n")
    print("------------------------------")

    # Text Statistics
    #print("Printing stats... \n")
    #test_case.stats()
    #print("------------------------------")

    # TODO Store each of the sentences in a pandas dataframe for easy access
    # df = pd.DataFrame(data, index=[0], columns=["raw"])
    
    # Pre-Processing Section
    print("Starting Pre-Processing...")
    #test_case.text_preProcessing()

    #Create Confusion Matrix
    sample_data = [4, 3]



    print("Finished Pre-Processing...\n")
    print("------------------------------")
    
    print("Writing Report")
    rg.write_report(sample_data)

    print("Finished Program")

if __name__ == "__main__":
    main()