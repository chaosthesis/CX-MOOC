from django.shortcuts import render, render_to_response
from django.template import RequestContext
from CXMOOC_Course.models import Course



def list_course(request):
    
    template='course/courses.html'
    page_template='course/courses_page.html'
    
    context = {
           'courses': Course.objects.all(),
           'page_template': page_template,
    }
    
    if request.is_ajax():
        template = page_template
    
    return render(request, template, context)


def search_course(request):
    
    query = request.GET.get('course_name')
    template ='course/courses.html'
    page_template='course/courses_page.html'
    
    if query:
        courses = Course.objects.filter(name__contains=query)
    else:
        courses = Course.objects.all()

    if request.is_ajax():
        return render(request, page_template, {'courses': courses, 'page_template': page_template})
    else:
        return render(request, template, {'courses': courses, 'page_template': page_template})


def index_view(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def about_view(request):
    return render(request, 'about.html', {})


def coursedev_view(request):
    course = Course.objects.filter(name=query)
    return render(request, 'course/course_content.html', {})