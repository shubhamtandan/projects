
# Create your views here.
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Destination
# Create your views here.

def index(request):
    #Create the object of the model and then render that in index.html
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = "THe city of dreams"
    # dest1.image = "destination_1.jpg"
    # dest1.price = "700"
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = "Famous Biryani"
    # dest2.image = "destination_2.jpg"
    # dest2.price = "780"
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'Bangalore'
    # dest3.desc = "THe beautiful city"
    # dest3.image = "destination_3.jpg"
    # dest3.price = "900"
    # dest3.offer = True

    # dest = [dest1,dest2,dest3]

    #This will fetch all the content dynamically.
    dest = Destination.objects.all()

    return render(request,'index.html',{'dest':dest})
