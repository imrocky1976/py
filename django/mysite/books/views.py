from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
from .models import Book

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def show_header(request):
    items = sorted([(k, v) for k, v in request.META.items() if isinstance(v, str)])
    t = get_template('show_header.html')
    html = t.render({'header_items': items, 'author': 'shihj'})
    return HttpResponse(html)
    #return render_to_response('show_header.html', {'header_items': items, 'author': 'shihj'})

#def search_form(request):
#    return render_to_response('search_form.html')

def search(request):
    error = ''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = 'Please submit a search term.'
        elif len(q) > 20:
            error = 'Please enter at most 20 characters.'
        else:
            request.session['query'] = request.session.get('query', "") + ";" + q
            books = Book.objects.filter(name__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q, 'author': 'shihj'})
    
    #return HttpResponse('Please submmit a search term.')
    return render_to_response('search_form.html', {'error': error})

'''
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Please input a subject.')
        if not request.POST.get('message', ''):
            errors.append('Please input a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Please enter a valid e-mail address.')
        if not errors:
            """
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['shihj@nrec.com']
            )
            """
            return HttpResponseRedirect('/books/contact/thanks/')

    return render(
        request, 
        "contact_form.html", 
        {
            'errors': errors, 
            'subject': request.POST.get('subject', ''),
            'message': request.POST.get('message', ''),
            'email': request.POST.get('email', '')
        }
    )
    #return render_to_response("contact_form.html", {'errors': errors})
'''

def contact(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            #print(request.session.get("test", "no test session"))
            #print(request.session.get("last_contact", "no last_contact session"))
            request.session.delete_test_cookie()
            form = ContactForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                """
                send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email', 'noreply@example.com'),
                    ['shihj@nrec.com']
                )
                """
                request.session['last_contact'] = cd['subject']
                return HttpResponseRedirect('/books/contact/thanks/')
        else:
            return HttpResponse("Please enable cookies and try again.")
    else:
        request.session.set_test_cookie()
        request.session['test'] = "test"
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(
        request, 
        "contact_form.html", 
        {'form': form}
    )

def thanks(request):
    return HttpResponse("Thanks!")