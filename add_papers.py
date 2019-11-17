import paper_finder as pf
import paper_values as pv
from papers.models import Paper

def add_paper(number):
  paper_list=pf.paper_finder(number)
  try:
    if paper_list[0]:
      new_list = pv.return_paper(paper_list[2])
      Paper.objects.create(title=new_list[0], objective=new_list[1], result="new result", year=new_list[2],link=paper_list[1])
      print("paper added")
  except:
    pass
