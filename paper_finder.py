import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import requests
import urllib.request
from bs4 import BeautifulSoup
import re
from requests.exceptions import ConnectionError

def paper_finder(page_number):
  url = 'https://www.ncbi.nlm.nih.gov/pubmed/' + str(page_number)
  try:
      response_1 = requests.get(url)
      r = True
  except ConnectionError as e:    # This is the correct syntax
      r = False
      print(1)
      return [False]
  if(r):
      paper = BeautifulSoup(response_1.text, "html.parser")
      links = paper.findAll("div", {"class": "resc"})
      link_numbers =[]
      if (len(links)>0):
          link_numbers = re.findall(r'href=[\'"]?([^\'" >]+)',str(links[0]))
      
          if (len(link_numbers)>0):
              
              for link_num in link_numbers:
                  unpaywall_link="http://api.unpaywall.org/"+link_num+"?email=graham28292@gmail.com"

                  try:
                      response_2 = requests.get(unpaywall_link)
                      g = True
                  except ConnectionError as e:    # This is the correct syntax
                      g = False
                      print(2)
                      return [False]
                      
                  if(g):
                      search = BeautifulSoup(response_2.text, "html.parser")

                      if(re.search("free_fulltext_url",str(search))):
                          split_list = re.split("\s", str(search))

                          for item in range(len(split_list)-1):
                              if(re.search("free_fulltext_url",split_list[item])):
                                  paper_url = split_list[item+1]
                                  paper_url = paper_url[1:-2]
                          
                          try:
                            if paper_url == "ul":
                              print(3)
                              return [False]
                            else:
                              return [True, paper_url,url]
                          except NameError as e:
                            print(4)
                            return [False]
                              
          else:
              print(5)
              return [False]




      else:
        print(6)
        return [False]
          
        