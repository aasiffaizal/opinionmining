# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse
import links
import polarity

from .forms import Search

# Create your views here.


def home(request):
	form = Search()
	ser=False
	positive=0
	negative=0
	neutral=0
	if request.method =='POST' :
		ser=True
		form=Search(request.POST)
		if form.is_valid():
			data = form.cleaned_data['search_text']
			data.replace(' ','+')
			raw = links.scrap(data)
			for i in raw:
				t=polarity.gsentiment(i)
				if  t > 0.5:
					positive+=1
				elif t<0.5:
					negative+=1
				else:
					neutral+=1

			a =positive*100/(positive+negative+neutral)
			b =negative*100/(positive+negative+neutral)
			c = neutral*100/(positive+negative+neutral)
		# data=" "	
		context = {'form':form,'data':data,'positive':a,'negative':b,'neutral':c,'ser':ser}
		return render(request,'index.html',context)
	else:	
		form = Search()
		context ={'form':form,'ser':ser}
	return render(request,'front.html',context)






