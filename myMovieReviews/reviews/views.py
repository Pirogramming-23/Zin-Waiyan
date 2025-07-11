from django.shortcuts import render
from .models import Review


# Create your views here.
def reviews_list(request):
    reviews = Review.objects.all() # 모든 object 가져오기
    context = {"reviews":reviews}
    return render(request,"reviews_list.html",context) #template으로 보내기

def reviews_detail(request,pk):
    review = Review.objects.get(id=pk)
    context = {"review":review}
    return render(request,"reviews_detail.html",context)

def reviews_create(request):
    if request == "POST":
        Review.objects.create(
            title = request.POST["title"],
            title = request.POST["title"],
            title = request.POST["title"],
            title = request.POST["title"],
            title = request.POST["title"],
            title = request.POST["title"],
            title = request.POST["title"],
            title = request.POST["title"],
            title = request.POST["title"],
        )
    return render(request,"reviews_create.html")