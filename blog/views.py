from django.shortcuts import render
from .models import post
# from .models import post
# from django.views import generic
# # Create your views here.


# class postlist(generic.ListView):
#     queryset: post.objects.filter(status=1).order_by('-created_on')
#     template_name: 'index.html'
#     def get_queryset(self): 
#         return post.objects.order_by('-created_on')

# class detaillist(generic.DetailView):
#     model: post
#     template_name: 'detailed.html'

def index(request):
    p=post.objects.all()
    return render(request, "index.html", {'post' : p}) 
  
def detailed(request):
    return render(request,'detailed.html')

    