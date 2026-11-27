
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MensajeContacto
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone


# FORMULARIO DE REGISTRO
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electronico")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# FORMULARIO PARA EDITAR USUARIOS
class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
        )


# PAGINAS PRINCIPALES
def apply(request):
    return HttpResponse("Bienvenido a mi Sitio Web.. :)")


def pagina(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def inicio(request):
    return render(request, 'index.html')


def marcas(request):
    return render(request, 'marcas.html')


def Juegos(request):
    return render(request, 'Juegos.html')


def collecciones(request):
    return render(request, 'collecciones.html')


def ofertas(request):
    return render(request, 'ofertas.html')


# FORMULARIO DE CONTACTO
def contacto(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')

        if nombre and correo and telefono and mensaje:

            MensajeContacto.objects.create(
                nombre=nombre,
                correo=correo,
                telefono=telefono,
                mensaje=mensaje
            )

            messages.success(
                request,
                '¡Tu mensaje se ha enviado correctamente!'
            )

            return redirect('contacto')

        else:
            messages.error(
                request,
                'Debes completar todos los campos.'
            )

    return render(request, 'contacto.html')


# INICIO DE SESION
def login(request):

    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":

        usuario = request.POST.get("usuario", "").strip()
        password = request.POST.get("password", "")

        usuario_validado = authenticate(
            request,
            username=usuario,
            password=password
        )

        if usuario_validado is not None:
            auth_login(request, usuario_validado)
            return redirect("inicio")

        return render(request, "login.html", {
            "error": "Usuario o contrasena incorrectos."
        })

    return render(request, "login.html")


# REGISTRO DE USUARIOS
def registro(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Cuenta creada correctamente. Ya puedes iniciar sesion."
            )

            return redirect("login")

    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form})


# CERRAR SESION
@login_required
def cerrar_sesion(request):

    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("inicio")


# COMPROBAR SI ES ADMINISTRADOR
def es_administrador(user):
    return user.is_authenticated and user.is_staff


# LISTA DE USUARIOS
@user_passes_test(es_administrador)
def usuarios(request):

    lista_usuarios = User.objects.all().order_by("username")

    return render(request, "usuarios.html", {
        "usuarios": lista_usuarios
    })


# AGREGAR USUARIO
@user_passes_test(es_administrador)
def agregar_usuario(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Usuario agregado correctamente.")

            return redirect("usuarios")

    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form})


# EDITAR USUARIO
@user_passes_test(es_administrador)
def editar_usuario(request, id):

    usuario = get_object_or_404(User, pk=id)

    if request.method == "POST":

        form = EditarUsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()

            messages.success(request, "Usuario modificado correctamente.")

            return redirect("usuarios")

    else:
        form = EditarUsuarioForm(instance=usuario)

    return render(request, "editar_usuario.html", {
        "form": form,
        "usuario": usuario
    })


# ELIMINAR USUARIO
@user_passes_test(es_administrador)
def eliminar_usuario(request, id):

    usuario = get_object_or_404(User, pk=id)

    if request.method == "POST":

        if usuario.pk == request.user.pk:

            messages.error(
                request,
                "No puedes eliminar tu propia cuenta desde este panel."
            )

        else:
            usuario.delete()

            messages.success(
                request,
                "Usuario eliminado correctamente."
            )

    return redirect("usuarios")




PRODUCTOS = {
    'stellar': {
        'nombre': 'Stellar Blade',
        'precio': 1600.00
    },
    'cyberpunk': {
        'nombre': 'Cyberpunk 2077',
        'precio': 1420.00
    },
    'persona': {
        'nombre': 'Persona 5 Royal',
        'precio': 1050.00
    },
    'ninja': {
        'nombre': 'Ninja Gaiden 4',
        'precio': 980.00
    },
    'bleach': {
        'nombre': 'Bleach Rebirth of Souls',
        'precio': 1600.00
    },
    'metalgear': {
        'nombre': 'Metal Gear Solid Delta',
        'precio': 1367.00
    }
}
PRODUCTOS.update({
    'infamous': {
        'nombre': 'inFAMOUS Second Son',
        'precio': 500.00
    },
    'metalgear5': {
        'nombre': 'Metal Gear Solid 5',
        'precio': 200.00
    },
    'asura': {
        'nombre': "Asura's Wrath",
        'precio': 250.00
    },
    'batman': {
        'nombre': 'Batman Arkham Collection',
        'precio': 350.00
    },
    'p5coleccionista': {
        'nombre': 'Edición coleccionista PS5',
        'precio': 1700.00
    },
    'resident': {
        'nombre': 'Resident Evil Requiem',
        'precio': 600.00
    }
})

PRODUCTOS.update({
    'cybercoleccion': {
        'nombre': 'Edición coleccionista Cyberpunk 2077',
        'precio': 2769.00
    },
    'doomcoleccion': {
        'nombre': 'Edición coleccionista Doom Eternal',
        'precio': 4000.00
    },
    'metalgearcoleccion': {
        'nombre': 'Edición coleccionista Metal Gear Solid 5',
        'precio': 2500.00
    },
    'requiemcoleccion': {
        'nombre': 'Edición coleccionista Resident Evil Requiem',
        'precio': 7695.00
    },
    'infamouscoleccion': {
        'nombre': 'Edición coleccionista inFamous Second Son',
        'precio': 5456.00
    },
    'ninjagaidencoleccion': {
        'nombre': 'Edición coleccionista Ninja Gaiden 3',
        'precio': 1500.00
    }
})

def agregar_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')

        if producto_id in PRODUCTOS:
            carrito = request.session.get('carrito', {})

            carrito[producto_id] = carrito.get(producto_id, 0) + 1

            request.session['carrito'] = carrito
            messages.success(request, 'Producto agregado al carrito.')
        else:
            messages.error(request, 'Producto no válido.')

    return redirect(request.META.get('HTTP_REFERER', 'Juegos'))


def carrito(request):
    carrito_sesion = request.session.get('carrito', {})
    productos_carrito = []
    total = 0

    for producto_id, cantidad in carrito_sesion.items():
        if producto_id in PRODUCTOS:
            producto = PRODUCTOS[producto_id]
            subtotal = producto['precio'] * cantidad

            productos_carrito.append({
                'id': producto_id,
                'nombre': producto['nombre'],
                'precio': producto['precio'],
                'cantidad': cantidad,
                'subtotal': subtotal
            })

            total += subtotal

    return render(request, 'carrito.html', {
        'productos': productos_carrito,
        'total': total
    })


def eliminar_carrito(request, producto_id):
    if request.method == 'POST':
        carrito_sesion = request.session.get('carrito', {})

        if producto_id in carrito_sesion:
            del carrito_sesion[producto_id]
            request.session['carrito'] = carrito_sesion

    return redirect('carrito')


def finalizar_compra(request):
    if request.method == 'POST':
        carrito_sesion = request.session.get('carrito', {})
        productos_comprados = []
        total = 0

        for producto_id, cantidad in carrito_sesion.items():
            if producto_id in PRODUCTOS:
                producto = PRODUCTOS[producto_id]
                subtotal = producto['precio'] * cantidad

                productos_comprados.append({
                    'nombre': producto['nombre'],
                    'cantidad': cantidad,
                    'precio': producto['precio'],
                    'subtotal': subtotal
                })

                total += subtotal

        if not productos_comprados:
            messages.error(request, 'Tu carrito está vacío.')
            return redirect('carrito')

        comprobante = {
            'fecha': timezone.localtime(),
            'productos': productos_comprados,
            'total': total
        }

        request.session['ultimo_comprobante'] = {
            'fecha': comprobante['fecha'].strftime('%d/%m/%Y %H:%M'),
            'productos': productos_comprados,
            'total': total
        }

        request.session['carrito'] = {}

        return render(request, 'comprobante.html', comprobante)

    return redirect('carrito')