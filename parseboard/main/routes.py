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


# TODO: The user is unable to get the text back to the website...
@main.route('/_report', methods=['GET', 'POST'])
def reporting():
    issue_id = request.args.get('issue', 0, type=int)
    article_id = request.args.get('article', 0, type=int)
    issue = Issue.query.get(issue_id)

    # Based on order in database... not ideal but ok for now
    article_de = Article.query.get(article_id)
    article_en = Article.query.get(article_id + 1)
    article_fr = Article.query.get(article_id + 2)

    print(article_de.title, article_en.title, article_fr.title)

    return jsonify({'de': article_de.serialize(), 'en': article_en.serialize(), 'fr': article_fr.serialize()})
