from django.shortcuts import render

l1 = [1,2,3,4,5]
def home(request):
    data = {
        'l1' : l1,
        'name' : 'Shiv ram sharma',
        'age' : 20
    }
    return render(request, 'index.html',data)

def about(request):
    return render(request, 'about.html')

