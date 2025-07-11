from django.shortcuts import render,redirect
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
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            year = request.POST["year"],
            genre = request.POST["genre"],
            review_star = request.POST["review_star"],
            director = request.POST["director"],
            actors = request.POST["actors"],
            running_time = request.POST["running_time"],
            review_text = request.POST["review_text"],
        )
        return redirect("/review/")
    return render(request,"reviews_create.html")

def reviews_delete(request,pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect("/review/")
