from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from .forms import QuestionForm
from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # latest_question_list = QuestionForm(request.POST or None)
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello you are now poll index.")
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNoteExist:
    #     raise Http404("Question does not exists.")
    question = get_object_or_404(Question, pk=question_id)
    # response = "You are looking for question %s."
    # return HttpResponse(response % question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
    # response = "You are looking for the result of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/result.html', {'question':question})

# def vote(request, question_id):
#     response = "You are voting on question %s."
#     return HttpResponse(response % question_id)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))