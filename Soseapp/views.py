from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


registeredStucode = 'HIK113'
scores = ''
myMBTI = ''

# Create your views here.
def codeInput(request):

    return render(request, "Soseapp/codeInputPage.html")

def serviceAgreePage(request):

        studentCode = request.POST['stuCode']
        global registeredStucode

        if studentCode != registeredStucode:
            message = 'No Such Information'
            return render(request, "Soseapp/codeInputPage.html", {'message' : message})
        else:
            return render(request, "Soseapp/serviceAgreement.html")

def surveyPage(request):

        return render(request, "Soseapp/survey.html")

@csrf_exempt
def mbtiSelect(request):
    if request.is_ajax():
        #do something
        data = request.POST
        global scores
        scores = data
        print(scores)

    mbtiList = ["ISTJ","ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]
    return render(request, "Soseapp/mbtiSelect.html", {"mbtiList":mbtiList})

def mainPage(request):
    if request.method == 'GET':
        return render(request, "Soseapp/mainPage.html")
    else:
        mbti = request.POST['slct']
        global myMBTI
        myMBTI = mbti

    return render(request, "Soseapp/mainPage.html", {"mbti":myMBTI})

def videoPage(request):
    return render(request, "Soseapp/video.html")

def toQuest1(request):
    return render(request, "Soseapp/quest1.html")

def toQuest2(request):
    return render(request, "Soseapp/quest2.html")

def toResult(request):
    return render(request, "Soseapp/resultPage.html")

def video2Page(request):

    if request.method == 'GET':
        answer = 'A'
        text = 'Talk to [Jun] and ask what he needs to finish the work on time.'
        return render(request, "Soseapp/video2.html", {"answer":answer, "text": text})

    text = ''
    answer = request.POST["hidden"]
    if answer == 'A':
        text = 'Talk to [Jun] and ask what he needs to finish the work on time.'
    elif answer == 'B':
        text = 'Understand the burden of [Jun], and provide as much help as possible.'
    elif answer == 'C':
        text = 'Tell [Han] to fire [Jun] and hire a new one as soon as possible.'
    elif answer == 'D':
        text = 'Decide to give up on the current project and start a new one.'

    return render(request, "Soseapp/video2.html", {"answer":answer, "text": text})

def video3Page(request):

    if request.method == 'GET':
        answer = 'A'
        text = 'Scold [Seo] for making a stupid mistake.'
        return render(request, "Soseapp/video3.html", {"answer":answer, "text": text})

    text = ''
    answer = request.POST["hidden"]
    if answer == 'A':
        text = 'Scold [Seo] for making a stupid mistake.'
    elif answer == 'B':
        text = 'Scold [Lyn] for not saving the files.'
    elif answer == 'C':
        text = 'Let the two people talk to each other and share their thoughts/make peace.'
    elif answer == 'D':
        text = 'Try to come up with a way to restore the design files.'

    return render(request, "Soseapp/video3.html", {"answer":answer, "text": text})
