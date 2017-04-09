from django.shortcuts import render

# Create your views here.


def Home(request):
    list = [{"name":"python"},{"name":"javascript"},{"name":""},{"name":"html5"},{"name":"django"}]
    return  render(request,"home.html",{"list":list,"map":map(str,range(100))})