from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from .models import Paper

# Create your views here.
def index(request):
  """index"""
  return render(request,'index.html')

 
 # Create your views here.
def topic(request):
  """index"""
  queryset = Paper.objects.all()
  context = {
    'object_list': queryset,
    }
  return render(request,'topic_page.html', context)


def search(request, mystring="medicine"):
  """index"""
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(mystring)
  filtered_search = [w for w in word_tokens if not w in stop_words]

  q1 = Paper.objects.filter(title__icontains=filtered_search[0])
  q2 = q1
  for word in filtered_search[1:]:
    q1 = q1.filter(title__icontains=word)
    q2 = q2 | Paper.objects.filter(title__icontains=word)
  
  
  

  context = {
    'top_results': q1,
    'next_results': q2,
    }
  return render(request,'search_page.html',context)

  
