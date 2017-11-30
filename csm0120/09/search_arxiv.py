import requests
import bs4

def search_arxiv(term):
    url = "http://export.arxiv.org/api/query"
    payload = {"search_query":"all:"+term,
               "start":0,
               "max_results":10
               }
    response = requests.get(url, params=payload)
    
    if response.status_code == 200:
        return response.text
    else:
        return None
    
def print_tag_text(xml_text, tag_name):
    soup = bs4.BeautifulSoup(xml_text, "xml")
    tags = soup.select("feed > entry > "+tag_name)
    for tag in tags:
        print(tag.text)
        
def main():
    xml_response = search_arxiv("exomars")
    if xml_response is None:
        print("bad response from arxiv")
    else:
        print_tag_text(xml_response, "title")
        
if __name__ == "__main__":
    main()
    
'''    
import time
url = make_url(some_data)
payloads = make_payloads(some_more_data)
for payload in payloads:
    resp = requests.get(url, params=payload)
    process(resp)
    time.sleep(1) # wait for 1 second
'''