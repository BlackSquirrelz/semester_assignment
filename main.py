# Database requirements
import sqlite3
from sqlite3 import Error
import database as db
import services.reportGenerator as rg
import pandas as pd
import parsers.spacyparser as spr


# Authorship information
__author__ = "Tobias Weisskopf"
__copyright__ = "Copyright 2020, Semester Assignment"
__credits__ = ["Tobias Weisskopf", "Adriana Dragusha", 'Rodolfo Chavez']
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Tobias Weisskopf"
__status__ = "Dev"


""" # This part is for the GUI
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    test = rg.write_report(sample_data)
    issues = db.get_issues()
    articles = db.get_articles()
    body = db.get_article_text()
    return render_template('home.html', tables=[test.to_html()], issues=issues, articles=articles, body=body)

#Define tha Database File as a Static File
DATABASE = r"articles.db" """

# The Main Function just calls the read data for now
def main():

   

if __name__ == "__main__":
    main()
    app.run(debug=True)