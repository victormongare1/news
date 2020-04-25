from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source
#views
@main.route('/')
def index():
  '''
  view root that returns the index page and various news sources 
  '''
  title = 'MY CURRENT NEWS'
  sources=get_source()
  return render_template('index.html',title=title,sources=sources)