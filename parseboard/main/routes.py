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


@main.route('/_report', methods=['GET', 'POST'])
def reporting():
    issue_id = request.args('issue', 0, type=int)
    article_id = request.args('article', 0, type=int)

    issue = Issue.query.get(issue_id)
    article = Article.query.get(article_id)
    return jsonify({'isu': issue.serialize(), 'art': article.serialize()})
