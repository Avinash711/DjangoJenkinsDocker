from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def doc_show(request):
    return HttpResponse('''<h1> Doc 1: Master Avinash</h1>,
                        <h2>Doc 2: Gaurav</h2>,
                        <h3>Doc 3: Sachin</h3>,
                        <h4>Doc 4: Mrs...Supriya </h4>,
                        ''')

def asst_show(request):
    return HttpResponse('''<h1> Doc 1: Gaurav Kumar</h1>,
                        <h2>Doc 2: Akg Company</h2>,
                        <h3>Doc 3: Srivastava</h3>,
                        <h4>Doc 4: Subham </h4>,
                        ''')