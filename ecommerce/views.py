from django.http import HttpResponse
def welcome(HttpRequest):
    return HttpResponse("whaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat!")
    # return render(request,'whatt')
def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'login.html', data)

# def handler500(request):
#     response = render_to_response('500.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response

def index(HttpRequest):
    return render("hekki")