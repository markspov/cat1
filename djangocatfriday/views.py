from django.shortcuts import render


def mycontacts(request):
    return render(request, 'contacts.html')

def myservicepage(request):
    return  render(request, 'services.html')