import urllib.request,json
from .models import SOURCE,ARTICLE
apikey=None
source_base_url=None
article_base_url=None

def configure_request(app):
  global apikey,source_base_url,article_base_url
  apikey = app.config['NEWS_API_KEY']
  source_base_url = app.config['SOURCE_BASE_URL']
  article_base_url=app.config['ARTICLE_BASE_URL']
def get_source():
  '''
  function that the json response to our url request
  '''
  get_source_url = source_base_url.format(apikey)
  print(get_source_url)
  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    get_source_response = json.loads(get_source_data)

    source_results = None

    if get_source_response['sources']:
      source_results_list = get_source_response['sources']
      source_results = process_results(source_results_list)


  return source_results
def get_article(id):
  '''
  function that returns a json response to the url request
  '''

  get_article_url=article_base_url.format(id,apikey)
  print(get_article_url)
  with urllib.request.urlopen(get_article_url) as url:
    get_article_data=url.read()
    get_article_response= json.loads(get_article_data)

    article_results=None
    if get_article_response['articles']:
      article_results_list = get_article_response['articles']
      article_results = process_results(article_results_list)
  

def process_results(source_list):
  '''
  Function  that processes the source result and transform them to a list of Objects

  Args:
    source: A list of dictionaries that contain source details

  Returns :
    source_results: A list of movie objects
  '''
  source_results = []
  for source_item in source_list:
    id=source_item.get('id')
    name = source_item.get('name')
    description= source_item.get('description')
    url= source_item.get('url')
    category = source_item.get('category')
    

    if name:
      source_object = SOURCE(id,name,description,url,category)
      source_results.append(source_object)

  return source_results

def process_articles(article_list):
  '''
  Function  that processes the article result and transform them to a list of Objects

  Args:
    article: A list of dictionaries that contain article details

  Returns :
    article_results: A list of movie objects
  '''
  article_results = []
  for article_item in article_list:
    author=article_item.get('author')
    title= article_item.get('title')
    publishedAt= article_item.get('publishedAt')
    content = article_item.get('content')
    

    if title:
      article_object = ARTICLE(author,title,publishedAt,content)
      article_results.append(article_object)
  return article_results