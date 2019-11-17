import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import requests
import urllib.request
from bs4 import BeautifulSoup
import re
from requests.exceptions import *

def return_paper(url):
  try:
    response = requests.get(url)
    search = BeautifulSoup(response.text, "html.parser")
  except ConnectionError as e:
    return ['','']
  title = ""
  content=""
  year =""
  try:  
    title = search.find("div", {"class": "rprt_all"})
    title= title.find('h1')
    title=title.get_text()
  except AttributeError as e:
    pass
  try:  
    year = search.find("div", {"class": "cit"})
    year = year.get_text()
    year = re.search(r'\d+', year).group()
    year = int(year)
  except AttributeError as e:
    pass
  try:
    content = search.find("div", {"class": "abstr"})
    content=content.find('p')
    content=content.get_text()

    parser = PlaintextParser.from_string(content,Tokenizer("english"))
    # Using LexRank
    summarizer = LexRankSummarizer()
    #Summarize the document with 2 sentences
    summary = summarizer(parser.document, 2)
    sum_abstract=" "
    for i in summary:
        sum_abstract+=str(i)
    content = sum_abstract
    

  except AttributeError as e:
    pass

  return[title,content,year,url]