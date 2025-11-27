import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://github.com/jagratadeb',
    'https://docs.langchain.com/oss/python/langgraph/overview',
    'https://docs.langchain.com/oss/python/langchain/models'
]

def fetch_content(url):
    response= requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} from {url}')
    print(f'Text {soup.text} from {url}')


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All pages fetched!")