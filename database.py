import sqlite3 as sql
from sqlite3 import Error

# System stuff
import os
import os.path
from os import path

import hashlib

DATABASE = r"articles.db"

def make_database():
    print("Called make_database")
    sql_create_articles_table = """ CREATE TABLE IF NOT EXISTS articles (
                                        id integer PRIMARY KEY,
                                        issue text NOT NULL,
                                        article text NOT NULL,
                                        language text NOT NULL,
                                        author text NOT NULL,
                                        title text NOT NULL,
                                        body text NOT NULL,
                                        hash text NOT NUll

                                    ); """

    # create a database connection
    conn = create_connection(DATABASE)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_articles_table)
    else:
        print("Error! cannot create the database connection.")


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_article(conn, article):
    """
    Create a new article into the articles table
    :param conn:
    :param article:
    :return: article id
    """
    sql = ''' INSERT INTO articles(issue, article, language, author, title, body, hash)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, article)
    return cur.lastrowid
    

# Initially this function is used to create all the articles in the database,
#  after initialization this serves no more purpose

def write_data_toDB(metadata, f):
    
    # Extract Metadata
    issue = metadata[0]
    article_number = metadata[1]
    language = metadata[2]

    split_file = f.split('\n',2)

    title = split_file[0].replace('Title: ', "")
    author = split_file[1].replace('Author: ', "")
    body = split_file[2].replace('Abstract: ', "")

    entry = str(body)

    # Hash Entry to prevent duplicates
    hash_value = hashlib.md5(entry.encode())

    conn = create_connection(DATABASE)
    with conn:
        # create a new article
        # (issue, article_number, language, title, author, body):
        article = (issue, article_number,language, author, title, body, hash_value.hexdigest() )
        if checkArticleExistance(conn, hash_value.hexdigest()):
            print(f"\tarticle {hash_value.hexdigest()} already exists")
        else:
            article_id = create_article(conn, article)
            print(f"\tcreated Article: {hash_value.hexdigest()} !")
    
        

def store_articles():
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
    
    print(f'Found {len(issues)} issues in {basepath}!')
    issues.sort()
    
    available_languages =  ['DE', 'EN', 'FR']

    # With the issues list, look through all the articles directories, basepath and issue list, check if the specific language file exsits and write it to the database.
    for issue in issues:
        print(issue)
        articlepath = basepath + "/" + issue
        article_entries = os.scandir(articlepath)
        for article in article_entries:
            articles.append(article.name)
            for language in available_languages:
                full_filePath = str(articlepath + '/' + article.name + '/' + language +'.txt')
                if os.path.isfile(full_filePath):
                    test_metadata = [issue, article.name, language]
                    print(f"{language} file exsist")
                    write_data_toDB(test_metadata, read_data(full_filePath))
                else:
                    print(f"{language} file does not exist!")
                print(f"\t\t found article {article.name} in {articlepath}.")
    articles.sort()
    print(f'Found: {len(articles)} articles in {len(issues)} issues!' )
    

# TODO make it so that the user can select any file.
def read_data(file_name):
    f = open(file_name, "r")
    print(f"\t {file_name}")
    text = f.read()
    f.close()
    return text

# This Function makes sure that no duplicate articles are being uploaded to the database
def checkArticleExistance(conn, hash_value):
    c = conn.cursor()
    article_exists = False
    query = "SELECT EXISTS(SELECT 1 FROM articles WHERE hash=?)"
    c.execute(query, (hash_value,))

    if c.fetchone():
        article_exists =  True

    return article_exists

def get_articles():
    con = sql.connect("articles.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select distinct(article) from articles Order By article ASC")
    rows = cur.fetchall()
    return rows

def get_issues():
    con = sql.connect("articles.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select distinct(issue) from articles Order By issue ASC")
    rows = cur.fetchall()
    return rows

def get_article_text():
    con = sql.connect("articles.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from articles where article='article_a1'")
    rows = cur.fetchall()
    return rows
