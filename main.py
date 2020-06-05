# Database requirements
import sqlite3
from sqlite3 import Error
import database as db
import services.reportGenerator as rg
import pandas as pd


# Authorship information
__author__ = "Tobias Weisskopf"
__copyright__ = "Copyright 2020, Semester Assignment"
__credits__ = ["Tobias Weisskopf", "Adriana Dragusha", 'Rodolfo Chavez']
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Tobias Weisskopf"
__status__ = "Dev"

# Load Sample Data
sample_data = pd.read_csv('sample_data.csv',delimiter=',')

# This part is for the GUI
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    test = rg.write_report(sample_data)
    return render_template('home.html', tables=[test.to_html()])

#Define tha Database File as a Static File
DATABASE = r"articles.db"

# The Main Function just calls the read data for now
def main():

    db.make_database()
        
    # Reading the file section
    print("Writing Data to DB...")
    
    db.store_articles()
    
    print("Finished Writing the Data... \n")
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
    

    print("Finished Pre-Processing...\n")
    print("------------------------------")
    print("Generating Report...\n")
    print(report)
    print("------------------------------")
    print("Finished Program")

if __name__ == "__main__":
    main()
    app.run(debug=True)