import configparser
from jina import Flow

def read_urls_from_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    urls = config['DEFAULT']['URLs'].split(',')
    return urls

def scrape_content(url: str):
    flow = Flow().add(uses='jinahub://SimpleCrawler')
    with flow:
        result = flow.index_lines(lines=[url], return_results=True)
    return result[0].text