'''The views module is the font end of the polls application.'''
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


# using class based views and also generic views for short and simple code.
class IndexView(generic.ListView):  
    '''The indexView is home page of polls application'''
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Get the all questions based on date'''
        return Question.objects.order_by('-Pub_date')[:5]


class DetailView(generic.DetailView):
    '''More deatils'''
    model = Question
    # context_object_name = 'question_choice_list'
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    '''Poll results'''
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    '''Poll the vote'''
    question = get_object_or_404(Question, pk=question_id)
    try:
        keys = request.POST.keys()
        ck = [k for k in keys if k[0:6] == "choice"]
        selected_choice = question.choice_set.get(pk=request.POST[ck[0]])
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', 
                      {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def owner(request):
    '''Admin request'''
    return HttpResponse(f"Hello, world. a8c5a734 is the polls owner. {request}")
