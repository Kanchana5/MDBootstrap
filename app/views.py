from django.shortcuts import render

# Create your views here.
def download(request):
    return render(request,'download.html')

def mdb(request):
    return render(request,'mdb.html')


