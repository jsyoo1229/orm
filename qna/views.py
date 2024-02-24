from django.shortcuts import render

def qna(request):
    return render(request, "qna/qna.html")


def qna_detail(request):
    return render(request, "qna/qna_detail.html")


