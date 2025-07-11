from django.shortcuts import render,redirect
from .models import Review


# Create your views here.
def reviews_list(request):
    # reviews = Review.objects.all() # 모든 object 가져오기
    reviews = Review.objects.order_by("-review_star")  # 별점 내림차순
    for review in reviews:
        hours = review.running_time // 60
        minutes = review.running_time % 60
        review.running_time_formatted = f"{hours}시간 {minutes}분"
    context = {"reviews":reviews}
    return render(request,"reviews_list.html",context) #template으로 보내기

def reviews_detail(request,pk):
    review = Review.objects.get(id=pk)
    hours = review.running_time // 60
    minutes = review.running_time % 60
    review.running_time_formatted = f"{hours}시간 {minutes}분"
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

def reviews_update(request,pk):
    review = Review.objects.get(id=pk)
    if request.method == "POST":
        review.title = request.POST["title"]
        review.year = request.POST["year"]
        review.genre = request.POST["genre"]
        review.review_star = request.POST["review_star"]
        review.director = request.POST["director"]
        review.actors = request.POST["actors"]
        review.running_time = request.POST["running_time"]
        review.review_text = request.POST["review_text"]
        review.save()
        return redirect(f"/review/{pk}")
    hours = review.running_time // 60
    minutes = review.running_time % 60
    review.running_time_formatted = f"{hours}시간 {minutes}분"
    context = {"review":review}
    return render(request,"reviews_update.html",context)
