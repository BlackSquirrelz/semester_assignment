from flask import render_template, Blueprint
from parseboard.models import Issue, Article
from parseboard import db

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def home():
    all_issues = Issue.query.all()
    # issues = {'Issue 1', 'Issue 2'}
    articles = {'Test 1', 'Test 2', 'Test 3'}
    return render_template('home.html', articles=articles, issues=all_issues)


@main.route('/report', methods=['GET', 'POST'])
def reporting():
    return render_template('report.html')
