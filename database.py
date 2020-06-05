import sqlite3
from sqlite3 import Error

DATABASE = r"articles.db"

def make_database():
    sql_create_articles_table = """ CREATE TABLE IF NOT EXISTS articles (
                                        id integer PRIMARY KEY,
                                        issue text NOT NULL,
                                        article text NOT NULL,
                                        language text NOT NULL,
                                        author text NOT NULL,
                                        title text NOT NULL,
                                        body text NOT NULL

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
        conn = sqlite3.connect(db_file)
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
    sql = ''' INSERT INTO articles(issue, article, language, author, title, body)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, article)
    return cur.lastrowid
    


def write_data_toDB(test_file):

    split_file = test_file.split('\n',2)

    title = split_file[0].replace('Title: ', "")
    author = split_file[1].replace('Author: ', "")
    body = split_file[2].replace('Abstract: ', "")

    conn = create_connection(DATABASE)
    with conn:
        # create a new article
        # (issue, article_number, language, title, author, body):
        article = ('issue_TEST', 'article_aTest','de', author, title, body )
        article_id = create_article(conn, article)
	# print(article_id, title, author, body)

def get_articles():
    pass