from django.db.models import F
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponse,HttpResponseRedirect
from django.views import View
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """
        Return the last five published questions.
        """
        # return Question.objects.order_by("pub_date")[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"
    def get_queryset(self):
         return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model=Question
    template_name = "polls/results.html"
    
def votes(request,question_id):
        question = get_object_or_404(Question,pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError,Choice.DoesNotExist):
            return render(
                request,
                'polls/details.html',
                {
                    "question":question,
                    "error_message":"You didnt select a choice.",
                }
            )
        else:
            selected_choice.votes = F("votes")+1
            selected_choice.save()
            return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))
        
    

















# def index(request):
#     return HttpResponse("Hello")

# class Hello_Nepal(View):
#     def get(self,request):
#         return HttpResponse("Hello from class!")
    
# # def detail(request,question_id):
# #     return HttpResponse("You are looking at question %s."% question_id)

# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,"results.html",{"question":question})

# def vote(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError,Choice.DoesNotExist):
#         return render(
#             request,
#             'details.html',
#             {
#                 "question":question,
#                 "error_message":"You didnt select a choice.",
#             }
#         )
#     else:
#         selected_choice.votes = F("votes")+1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))

# def index(request):
#     latest_question_list = Question.objects.order_by("pub_date")[:5]
#     # template = loader.get_template("index.html")
#     context = {"latest_question_list":latest_question_list}
#     # return HttpResponse(template.render(context,request))
#     return render(request,"index.html",context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "details.html", {"question": question})


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,'details.html',{'question':question})