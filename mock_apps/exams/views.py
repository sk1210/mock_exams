from django.shortcuts import render
from django.http import HttpResponse
from exams import models

# Create your views here.

# home
def index(request):
    objects = models.QuestionBank.objects.all()
    sections = models.QuestionType.objects.all()
    print (sections)
    #sections = []
    context = { "sections":sections }
    return render(request, 'index.html', context)

def test(request):
    context = {}
    if request.method == 'GET':
        section_id = request.GET.get('section_id')
        all_questions = models.QuestionBank.objects.filter(questiontype__id=section_id)
        section_name = models.QuestionType.objects.get(id=section_id).name
        context = { "section_name":section_name, "all_questions":all_questions }
    return render (request, 'test.html', context)

