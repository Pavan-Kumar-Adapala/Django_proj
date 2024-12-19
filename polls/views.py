#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader

#from django.shortcuts import render   # used in index,detail functions
#from django.http import Http404       # used in detail function to raise exception

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

"""
def index(request):
    new_que_list = Question.objects.order_by('-Pub_date')[:5]
    # the below "output" writen without template
    '''output = ' , '.join([q.question_tpy for q in new_que_list])  #question_tpy in models.py
    return HttpResponse(output)'''
    # here we are using template (the path is templates/polls/index.html)
    '''template = loader.get_template('polls/index.html')
    context = {
        'new_que_list': new_que_list,
    }
    return HttpResponse(template.render(context, request))'''

    # we can write in simple way by using only "render()"
    
    context = {'new_que_list': new_que_list,}
    return render(request, 'polls/index.html', context)    # for we need import render from django.shortcuts

def detail(request, question_id): 
    '''
    try:
        question = Question.objects.get(pk=question_id)    
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request, 'polls/detail.html', {'question': question})'''

    # the above code writen in simple way by using "get_object_or_404()"

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question} 
"""

# using class based views and also generic views for short and simple code.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-Pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    #context_object_name = 'question_choice_list'
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        keys = request.POST.keys()
        ck = [k for k in keys if k[0:6]=="choice"]
        selected_choice = question.choice_set.get(pk=request.POST[ck[0]])
        #selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def owner(request):
    return HttpResponse("Hello, world. a8c5a734 is the polls owner.")