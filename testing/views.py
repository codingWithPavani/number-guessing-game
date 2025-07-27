from django.shortcuts import render

import random


def project(request):
    lucky_number = random.randint(10,50)
    context = {'lucky_number' :  lucky_number}
    return render(request,'testing/new.html',context )
