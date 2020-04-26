class SOURCE:
  '''
  source class to define source objects
  '''
  def __init__(self,id,name,description,url,category):
    self.id=id
    self.name=name
    self.description=description
    self.url=url
    self.category=category
class ARTICLE:
  '''
  article class to define article objects
  '''
  def __init__(self,author,title,urlToImage,publishedAt,content):
    self.author=author
    self.title=title
    self.urlToImage=urlToImage
    self.publishedAt=publishedAt
    self.content=content