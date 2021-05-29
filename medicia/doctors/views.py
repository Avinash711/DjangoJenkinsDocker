from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def doc_show(request):
    return HttpResponse('''<h1> Doc 1: Master Avinash</h1>,
                        <h2>Doc 2: Gaurav</h2>,
                        <h3>Doc 3: Sachin</h3>,
                        <h3> Supriya </h3>''')

def asst_show(request):
    return HttpResponse('''<h1> asst: Mr. Gaurav Kumar</h1>,
                        <h2>asst 2: Akg Company</h2>,
                        <h3>asst 3: Srivastava</h3>,
                        <h4>asst 4: Subham </h4>,
                        ''')



def patient_show(request):
    return HttpResponse('''<h1> Patients are : Robert</h1>,
                        <h2>Rajveer Singh</h2>,
                        <h3>Ajay kumar</h3>,
                        <h4>Arvind</h4>,
                        ''')


