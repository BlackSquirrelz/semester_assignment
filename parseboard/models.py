# Migrated DB
from parseboard import db
# from flask import current_app
import hashlib


class Issue(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False)
    issue = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    hash = db.Column(db.String(255), unique=True, nullable=False)
    articles = db.relationship('Article', backref='article', lazy=True)

    def __init_(self, issue, hash, articles):
        self.issue = issue
        self.hash = hash
        self.articles = articles

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'isssue': self.issue,
            'hash': self.hash,
            'articles': self.articles
        }


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(10), unique=True, nullable=False)
    language = db.Column(db.String(2), unique=False, nullable=False)
    author = db.Column(db.String(50), unique=False, nullable=False)
    title = db.Column(db.String(100), unique=False, nullable=False)
    body = db.Column(db.String(5000), unique=False, nullable=False)
    hash = db.Column(db.String(250), unique=True, nullable=False)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.issue'), nullable=False)

    def __init__(self, article, language, author, title, body, hash, issue_id):
        self.article = article
        self.language = language
        self.author = author
        self.title = title
        self.body = body
        self.hash = hash
        self.issue_id = issue_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'language': self.language,
            'author': self.author,
            'title': self.title,
            'body': self.body,
            'hash': self.hash,
            'issue_id': self.issue_id
        }


def import_articles():
    hashlib.md5('Text')
    pass


def write_articles():
    pass
