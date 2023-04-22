from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from main.models import Lecture, Student


# Create your views here.
def main_views(request):
    link_list = [("Pierwszy wykład", '/lecture_details/1/'),
                 ("Zapisz mnie", '/set_username/<twoje imię>/'),
                 ("Przywitaj mnie", '/say_hello/'),
                 ("Przywitaj mnie 5 razy", '/say_hello/5/'),
                 ("Upiecz ciastko", '/create_cookie/cookie/cookie/10/'),
                 ("Zjedz ciastko", '/delete_cookie/cookie/'),
                 ("Dodaj studenta", '/add_student/')]
    return render(request, 'main/view.html', {'links': link_list})


def lecture(request, lecture_id):
    lecture_ = Lecture.objects.get(pk=lecture_id)
    return render(request, 'main/lecture.html', {'lecture': lecture_})


def set_user(request, name):
    request.session['user_name'] = name
    return HttpResponse('Zapisano dane')


def hello(request, number):
    name = request.session.get('user_name')
    if name:
        return HttpResponse(f'Witaj {name} ' * number)
    return HttpResponse('Witaj nieznajomy ' * number)


def create_cookie(request, cookie_name, cookie_value, cookie_time):
    response = HttpResponse('Ciasteczko upieczone')
    response.set_cookie(key=cookie_name, value=cookie_value, expires=cookie_time * 60)
    return response


def delete_cookie(request, cookie_name):
    response = HttpResponse('Brak takiego ciasteczka')
    if cookie_name in request.COOKIES:
        response = HttpResponse(f'Ciasteczko {request.COOKIES.get(cookie_name)} zostało usunięte')
        response.delete_cookie(key=cookie_name)
    return response


def hello_(request):
    return redirect('/say_hello/10')


class AddStudent(View):
    def get(self, request):
        return render(request, 'main/add_studetnt.html')

    def post(self, request):
        name = request.POST.get('name')
        year_at_university = request.POST.get('year_at_university')
        is_active = bool(request.POST.get('is_active'))

        try:
            year_at_university = int(year_at_university)
        except ValueError:
            return HttpResponse('Rok musi być liczbą')

        if not name or year_at_university < 1:
            return HttpResponse('Podana nazwa lub rok jest nieprawidłowa')

        Student.objects.create(name=name, year_at_university=year_at_university, is_active=is_active)
        return HttpResponse('Dodano nowego studenta')
