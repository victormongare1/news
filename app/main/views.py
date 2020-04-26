from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_article
from ..models import ARTICLE
#views
@main.route('/')
def index():
  '''
  view root that returns the index page and various news sources 
  '''
  title = 'NEWS SITES'
  sources=get_source()
  return render_template('index.html',title=title,sources=sources)
@main.route('/article/<id>')
def article(id):
  '''
  view articles page function that returns articles from a particular movie source
  '''
  
  articles=get_article(id)
  
  return render_template('articles.html',articles=articles)