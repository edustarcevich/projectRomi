from django.shortcuts import render, redirect

from contact.forms import Envio_de_Email
from django.core.mail import send_mail
# Create your views here.


def Contact_views (request):
    form_email = Envio_de_Email ()
    if request.method == "POST":
        form_email = Envio_de_Email (request.POST)
        print (form_email)
        if form_email.is_valid ():
            asunto = request.POST["asunto"] #recuperado del name
            email = request.POST["email"]
            mensaje = request.POST["mensaje"]
            print (form_email) #para ver en consola que llega # borrar
            
            send_mail (
                        asunto,
                        mensaje + " enviado por: " + email,
                        'agregar correo de ccva en outlook',
                        ['aqui se agrega un correo al cual se quiere avisar'],
                        fail_silently=False,
                    )
            return redirect (request, "thank")
    return render (request, "contact.html", {"form_email":form_email})


def Send_email_ok (request):
    return render (request, "thank.html")


def Mision_and_Vision (request):
    return render (request, "mision_vision.html")

def History (request):
    return render (request, "history.html")

def Groups (request):
    return render (request, "groups.html")