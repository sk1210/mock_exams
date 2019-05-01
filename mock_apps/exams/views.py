from django.shortcuts import render
from django.http import HttpResponse
from exams import models
import json
from django.views.decorators.csrf import csrf_exempt

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

        # convert question option into array
        question_id = []
        for question in all_questions:
            question.choices = question.choices.split(",")
            question_id.append(question.id)
        context = { "section_name":section_name, "all_questions":all_questions,
                    "question_id" : question_id}
    return render (request, 'test.html', context)

@csrf_exempt
def check_ans(request):
    response_data = {}
    if request.method == 'POST':
        answers = json.loads(request.body.decode("utf-8"))["answer"]
        answer_id = list( map(int, answers.keys()))
        print (answers)
        all_questions = models.QuestionBank.objects.filter(id__in=answer_id)
        #response_data["ans"] = answers

        # compare answers
        correct = 0
        response_data["resp"] = {}
        for  question_id in answers:
            response = answers[question_id]
            question = list(filter( lambda x:int(x.id) == int(question_id), all_questions))[0]
            right_answer = question.getCorrectAnswer()
            print (response, right_answer, question.text, question_id)
            if response.strip() == right_answer.strip():
                response_data["resp"][question_id] = "Correct"
                correct +=1
            else:
                response_data["resp"][question_id] = "Wrong"
        response_data["total"] = len(answers)
        response_data["correct"] = correct
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def result(request):
    context = {}
    if request.method == 'POST':
        print (request.POST.get('Total'))
        print(request.POST)
        total = request.POST.get('Total')
        correct = request.POST.get('Correct')
        attempted = request.POST.get('Attempted')

        context= {"total":total,
                "correct":correct,
                "attempted":attempted}

    return render(request, 'result.html', context)
