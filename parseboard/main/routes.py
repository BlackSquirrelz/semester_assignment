from flask import render_template, Blueprint, jsonify, request
from parseboard.models import Issue, Article
from parseboard import db
from parseboard.parsers import evaluation

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def home():
    all_issues = Issue.query.all()
    # issues = {'Issue 1', 'Issue 2'}
    articles = Article.query.all()
    return render_template('home.html', articles=articles, issues=all_issues)


@main.route("/<int:article_id>")
def article(article_id):
    article = {
        "article": "1",
        "body": "LOREM",
        'language': 'en'
        }
    return jsonify(article)


@main.route('/_report', methods=['GET', 'POST'])
def reporting():
    # report = evaluation.evaulate_parsers()
    report = {
        "article": "1",
        "body": "LOREM",
        'language': 'en'
        }
    return jsonify(report)
