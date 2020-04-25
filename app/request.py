import urllib.request,json
from .models import SOURCE,ARTICLE
apikey='d87c1c4fe09d43568c5366531dbdfa30'
source_base_url=None
def configure_request(app):
  global api_key,source_base_url
  apikey = app.config['NEWS_API_KEY']
  source_base_url = app.config['SOURCE_BASE_URL']
def get_source():
  '''
  function that the json response to our url request
  '''
  get_source_url = source_base_url
  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    get_source_response = json.loads(get_source_data)

    source_results = None

    if get_source_response['sources']:
      source_results_list = get_source_response['sources']
      source_results = process_results(source_results_list)


  return source_results
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
    
    name = source_item.get('name')
    description= source_item.get('url')
    url= source_item.get('url')
    category = source_item.get('vote_average')
    

    if name:
      source_object = SOURCE(name,description,url,category)
      source_results.append(source_object)

  return source_results 