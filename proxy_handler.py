import urllib.request

def create_proxy_handler():
  
  url = "https://en.wikipedia.org/wiki/Adriana_Lima"
  # add proxy
  proxy = {
    # free version : "http":"120.77.249.46:8080"
    # paid version : "http":"username:pwd@192.168.12.11:8080"
    "http":""
 
  }
  # proxy handler
  proxy_handler = urllib.request.ProxyHandler(proxy)
  # create opener
  opener = urllib.request.build_opener(proxy_handler)
  # get response with proxy ip
  response = opener.open(url)
  
  data = response.read().decode("utf-8")
  
  with open("proxy_handler.html", "w", encoding="utf-8") as f:
    f.write(data)
    
create_proxy_handler()
    
