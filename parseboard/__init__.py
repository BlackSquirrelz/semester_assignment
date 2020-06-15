from flask import Flask, render_template, url_for

# Database requirements
import sqlite3
from sqlite3 import Error
import database as db
import services.reportGenerator as rg
import pandas as pd
import parsers.spacyparser as spr

app = Flask(__name__)
app.config['SECRET_KEY'] = "Q0FMUiBTZW1lc3Rlcl9Qcm9qZWN0IDIwMjAK"


# Load Sample Data
sample_data = pd.read_csv('sample_data.csv',delimiter=',')

@app.route('/', methods=['GET'])
def home():
    test = rg.write_report(sample_data)
    issues = db.get_issues()
    articles = db.get_articles()
    body = db.get_article_text()
    return render_template('home.html', tables=[test.to_html()], issues=issues, articles=articles, body=body)

#Define tha Database File as a Static File
DATABASE = r"articles.db"

db.make_database()
    
# Reading the file section
print("Writing Data to DB...")

db.store_articles()

print("Finished Writing the Data... \n")
print("------------------------------")
print("Starting Server")

