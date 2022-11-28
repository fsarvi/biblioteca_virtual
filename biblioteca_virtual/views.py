from django.shortcuts import render
from numpy import true_divide
from .forms import ContactoForm
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.urls import reverse
from datetime import datetime
# importo las tablas de la base de datos
from .models import Persona, Autor, Usuario, Editorial, Genero, Critica, Estado, Resenia, Libro, Comentario

# def ver_tabla_libros(request):
#   mi_tabla_libros = Libro.objects.all().values()
#   template = loader.get_template('ver_tabla_libros.html')
#   context = {
#     'mi_tabla_libros' : mi_tabla_libros
#     }
#   return HttpResponse(template.render(context, request))


def index(request):
    libros = Libro.objects.all().values()
    generos = Genero.objects.all().values()
    estados = Estado.objects.all().values()
    libros = {"libros": libros, "generos": generos, "estados":estados}  

    return render(request, 'index.html', libros)

def favoritos(request):
    return render(request, 'favoritos.html')

def resenias(request):

    libros = Libro.objects.all().values()
    libros = {"libros": libros}

    return render(request, 'reseñas.html', libros)


def entrada_resenia(request):
    return render(request, "entradareseña.html")

def pendientes(request):
    return render(request, "pendientes.html")

def equipo(request):
    return render(request, 'equipo.html', {})


def buscar(request):

    if request.GET['busqueda']:

        busqueda = request.GET['busqueda']
        categoria = request.GET['categoria']

        if categoria == "titulo":
            buscador = Libro.objects.filter(titulo__icontains=busqueda)
        elif categoria == "autor":
            buscador = Libro.objects.filter(autor__icontains=busqueda)

        libros = {"libros": buscador}

    else:

        try:
            request.GET['genero']
            genero = request.GET['genero']
            buscador = Libro.objects.filter(genero__nombre__icontains=genero)

            libros = {"libros": buscador}

        except:
            messages.error(
                request, 'El buscador sólo puede ir vacío si selecciona un género')
            libros = {"libros": Libro.objects.all().values()}
            return render(request, 'index.html', libros)

    return render(request, 'busqueda.html', libros)


def sinopsis(request, id):

    # cambiar por relacionados por género
    libros_relacionados = Libro.objects.all().values()

    libro_seleccionado = Libro.objects.get(id=id)
    comentarios = Comentario.objects.filter(libro_id=id)
    generos = libro_seleccionado.genero.all()

    libros_y_usuarios = {"comentarios": comentarios,
                         "relacionados": libros_relacionados, "libro_seleccionado": libro_seleccionado, "generos": generos}

    return render(request, 'sinopsis.html', libros_y_usuarios)


def contacto(request):
    if request. method == "POST":
        # Creo la instancia populada con los datos cargados en pantalla
        contacto_form = ContactoForm(request. POST)
        # Valido y proceso los datos.
        if contacto_form.is_valid():
            pass

    else:
        # Creo el formulario vacío con los valores por defecto
        contacto_form = ContactoForm()

    return render(request, "contacto.html", {'contacto_form': contacto_form})


# # Vistas para poder agregar los datos a las tablas
# # tres vistas separadas:
# # a)	llenar_libros
# # b)	llenar_recomendaciones
# # c)	llenar_relacionados

# # a)	llenar_libros

# def llenar_libros_1(request):
#     template = loader.get_template('llenar_libros_1.html')
#     return HttpResponse(template.render({}, request))

def llenar_libros(request):

    rebeca = Persona(nombre="Rebecca", apellido="Fleet")
    rebeca.save()
    rebeca_autor = Autor.objects.create(persona=rebeca)
    frank = Persona(nombre="Frank", apellido="Herbert")
    frank.save()
    frank_autor = Autor.objects.create(persona=frank)
    frank_autor.save()
    allan = Persona(nombre="Allan", apellido="Poe")
    allan.save()
    allan_autor = Autor.objects.create(persona=allan)
    allan_autor.save()
    flynn = Persona(nombre="Flynn", apellido="Gillian")
    flynn.save()
    flynn_autor = Autor.objects.create(persona=flynn)
    flynn_autor.save()
    antonio = Persona(nombre="Antonio", apellido="Garrido")
    antonio.save()
    antonio_autor = Autor.objects.create(persona=antonio)
    antonio_autor.save()
    cesar = Persona(nombre="Cesar", apellido="Gelida")
    cesar.save()
    cesar_autor = Autor.objects.create(persona=cesar)
    cesar_autor.save()

    ernesto = Persona(nombre="Ernesto", apellido="Sabato")
    ernesto.save()
    ernesto_autor = Autor.objects.create(persona=ernesto)
    ernesto_autor.save()


    editorial_unica = Editorial(nombre="Debolsillo")
    editorial_unica.save()

    genero_ficcion = Genero(nombre="Ficción")
    genero_ficcion.save()
    genero_novela = Genero(nombre="Novela")
    genero_novela.save()
    genero_thriller = Genero(nombre="Thriller")
    genero_thriller.save()
    genero_fantasia = Genero(nombre="Fantasía")
    genero_fantasia.save()
    genero_policial = Genero(nombre="Policial")
    genero_policial.save()
    genero_horror = Genero(nombre="Horror")
    genero_horror.save()
    genero_suspenso = Genero(nombre="Suspenso")
    genero_suspenso.save()
    genero_psicologico = Genero(nombre="Psicológico")
    genero_psicologico.save()

    estado_nuevo_leyendo = Estado(nuevo=True, leyendo=True)
    estado_nuevo_leyendo.save()
    estado_nuevo = Estado(nuevo=True, leyendo=False)
    estado_nuevo.save()
    estado_leyendo = Estado(nuevo=False, leyendo=True)
    estado_leyendo.save()
    estado_no_leyendo_no_nuevo = Estado(nuevo=False, leyendo=False)
    estado_no_leyendo_no_nuevo.save()

    resenia_1 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_1.save()
    resenia_2 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_2.save()
    resenia_3 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_3.save()
    resenia_4 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_4.save()
    resenia_5 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_5.save()
    resenia_6 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_6.save()
    resenia_7 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_7.save()
    resenia_8 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_8.save()
    resenia_9 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_9.save()
    resenia_10 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_10.save()
    resenia_11 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_11.save()
    resenia_12 = Resenia(titulo="Reseña:", resenia="La Reseña")
    resenia_12.save()

    critica_post = Critica(
        critica="Una deliciosa novela dedomestic noir.", fuente="The Washington Post")
    critica_post.save()
    critica_times = Critica(
        critica="Perturbadora, atrapante, magnifica.", fuente="El Canillita Times")
    critica_times.save()

    critica_post_1 = Critica(
        critica="Una deliciosa novela dedomestic noir.", fuente="The Washington Post")
    critica_post_1.save()
    critica_times_1 = Critica(
        critica="Perturbadora, atrapante, magnifica.", fuente="El Canillita Times")
    critica_times_1.save()

    critica_post_2 = Critica(
        critica="Una deliciosa novela dedomestic noir.", fuente="The Washington Post")
    critica_post_2.save()
    critica_times_2 = Critica(
        critica="Perturbadora, atrapante, magnifica.", fuente="El Canillita Times")
    critica_times_2.save()

    critica_post_3 = Critica(
        critica="Una deliciosa novela dedomestic noir.", fuente="The Washington Post")
    critica_post_3.save()
    critica_times_3 = Critica(
        critica="Perturbadora, atrapante, magnifica.", fuente="El Canillita Times")
    critica_times_3.save()

    libro_intercambio = Libro(
        titulo="El intercambio",
        descripcion="Lorem ipsum consectetuer adipiscing",
        imagen="pic11",
        sinopsis="Un intercambio de casas es el detonante de la crisis de un matrimonio en este hipnótico thriller.",
        fecha_publicacion=datetime.strptime("2018/26/4", '%Y/%d/%m'),
        editorial=editorial_unica,
        critica=critica_post,
        estado=estado_nuevo,
        autor=rebeca_autor,
        resenia=resenia_1
    )
    libro_intercambio.save()
    libro_intercambio.genero.add(
        genero_ficcion, genero_novela, genero_thriller)

    libro_dune = Libro(
        titulo="Dune",
        descripcion="Lorem ipsum consectetuer adipiscing",
        imagen="pic12",
        sinopsis= """Mezcla fascinante de aventura, misticismo, intrigas políticas y ecologismo, Dune se convirtió,
         desde el momento de su publicación, en un fenómeno de culto y en la mayor epopeya de ciencia-ficción de todos los tiempos.""",
        fecha_publicacion=datetime.strptime("1965/1/8", '%Y/%d/%m'),
        editorial=editorial_unica,
        critica=critica_times,
        estado=estado_leyendo,
        autor=frank_autor,
        resenia=resenia_2
    )
    libro_dune.save()
    libro_dune.genero.add(genero_ficcion, genero_novela, genero_fantasia)

    libro_gato_negro = Libro(
        titulo="El gato negro",
        descripcion="Lorem ipsum consectetuer adipiscing",
        imagen="pic13",
        sinopsis="""El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, 
        en los que destaca El gato negro, William Wilson y La carta robada""",
        fecha_publicacion=datetime.strptime("1843/19/8", '%Y/%d/%m'),
        editorial=editorial_unica,
        critica=critica_times_1,
        estado=estado_no_leyendo_no_nuevo,
        autor=allan_autor,
        resenia=resenia_3
    )
    libro_gato_negro.save()
    libro_gato_negro.genero.add(
        genero_horror, genero_policial, genero_psicologico)
    
    libro_perdida = Libro(
        titulo="El gato negro",
        descripcion="Lorem ipsum consectetuer adipiscing",
        imagen="pic14",
        sinopsis= """No pierdas el tren.Perdida es tu próxima parada. 
        El libro que se ha convertido en un referente del thriller psicológico contemporáneo""" ,
        fecha_publicacion=datetime.strptime("2012/24/5", '%Y/%d/%m'),
        editorial=editorial_unica,
        critica=critica_post_1,
        estado=estado_nuevo,
        autor=flynn_autor,
        resenia=resenia_4
    )
    libro_perdida.save()
    libro_perdida.genero.add(genero_ficcion, genero_policial)

    libro_tunel = Libro(
        titulo="El gato negro",
        descripcion="Lorem ipsum consectetuer adipiscing",
        imagen="pic15",
        sinopsis= """El amor ilimitado truncado por un engaño convertirá el corazón de un hombre en 
        un pedazo de duro y frío hielo y colocará en sus manos el cuchillo que pone final al sufrimiento. 
        Sabato nos entrega los elementos básicos de su visión metafísica del existir""" ,
        fecha_publicacion=datetime.strptime("1948/1/1", '%Y/%d/%m'),
        editorial=editorial_unica,
        critica=critica_times_2,
        estado=estado_nuevo,
        autor=ernesto_autor,
        resenia=resenia_5
    )
    libro_tunel.save()
    libro_tunel.genero.add(genero_novela, genero_psicologico)

    libro_lector_cadaveres = Libro(
        titulo="El lector de cadaveres",
        descripcion="Lorem ipsum consectetuer adipiscing",
        imagen="pic16",
        sinopsis= """Un absorbente thriller histórico en el que la ambición y el odio 
        van de la mano con el amor y la muerte en la exótica y fastuosa China medieval.""" ,
        fecha_publicacion=datetime.strptime("2011/5/10", '%Y/%d/%m'),
        editorial=editorial_unica,
        critica=critica_post_2,
        estado=estado_nuevo,
        autor=antonio_autor,
        resenia=resenia_6
    )
    libro_lector_cadaveres.save()
    libro_lector_cadaveres.genero.add(genero_ficcion, genero_suspenso, genero_thriller)

    libro_memento = Libro(
        titulo="Memento",
        descripcion="Lorem ipsum consectetuer adipiscing",
        imagen="pic22",
        sinopsis= """La primera entrega de la trilogía «Versos, canciones 
        y trocitos de carne», una novela negra narrada con un dinámico y atrevido lenguaje cinematográfico.""" ,
        fecha_publicacion=datetime.strptime("2013/1/1", '%Y/%d/%m'),
        editorial=editorial_unica,
        critica=critica_post_3,
        estado=estado_no_leyendo_no_nuevo,
        autor=cesar_autor,
        resenia=resenia_7
    )
    libro_memento.save()
    libro_memento.genero.add(genero_horror, genero_psicologico, genero_policial)

    return HttpResponseRedirect(reverse('index'))


# def llenar_recomendaciones_1(request):
#     template = loader.get_template('llenar_recomendaciones_1.html')
#     return HttpResponse(template.render({}, request))


# def llenar_recomendaciones(request):

#     lu = [
#             ["Rene Favaloro", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam placeat cumque vero et! A alias sed, voluptas beatae", 3],
#             ["Jose de San Martin", "quia obcaecati quisquam at eum assumenda dolorem? Rem omnis voluptates repellat aperiam voluptatem, quibusdam voluptas", 3],
#             ["Victoria Ocampo", "fugiat, commodi at laudantium, minus corrupti porro unde nihil ipsum quae? Ducimus soluta delectus a consequuntur ", 2],
#             ["Jorge Luis Borges", "error accusamus distinctio qui unde dolore quis minima suscipit maiores, voluptatum commodi iste, velit facere doloremque", 3],
#             ["Alfonsina Storni", "aliquam. Debitis commodi veniam est dolore necessitatibus cumque et reiciendis, at quod, eum porro, amet obcaecati", 5],
#             ["Maria Elena Walsh", "maxime fuga! Libero aperiam quae voluptatem obcaecati quos laudantium doloremque aspernatur exercitationem", 2],
#             ["Mercedes Sosa", "consequuntur, repellendus id, hic cum deserunt quaerat voluptas aliquam cumque illo unde dolorem. Cupiditate", 4],
#             ["Juan Manuel Fangio", "voluptatibus aliquid quos nemo aut asperiores iste nostrum possimus iusto, cum velit fugit ad tempore vitae labore", 5],
#             ["Ernesto Sabato", "nesciunt repellendus culpa fugiat reiciendis, magni voluptate, distinctio dicta. Sit laboriosam neque nemo eveniet atque nulla.", 5]
#         ]

#     for i in range(0, 9):
#         lis_usu=  Usuario(
#                     usuario_nombre = lu[i][0],
#                     usuario_critica_libro = lu[i][1],
#                     usuario_puntuacion_libro = lu[i][2]
#                     )
#     lis_usu.save()

#     return HttpResponseRedirect(reverse('index'))

# def llenar_relacionados_1(request):
#     template = loader.get_template('llenar_relacionados_1.html')
#     return HttpResponse(template.render({}, request))


# def llenar_relacionados(request):
#     lr = [
#         ["El buen hijo", "buenhijo"],
#         ["Reina del grito", "reinagrito"],
#         ["Kaiki: Cuentos de terror y locura", "kaiki"],
#         ["Reinas del abismo", "reinasabismo"],
#         ["El bazar de los malos sueños", "malossueños"],
#         ["La habitacion de Nona", "habitacionnona"]
#     ]

#     for x in range(0, 6):
#         lis_rel= Lista_libros_relacionados(libro_relacionado_titulo = lr[x][0] ,
#         libro_relacionado_imagen =  lr[x][1]  )
#         lis_rel.save()
#     return HttpResponseRedirect(reverse('index'))


def tecnologia_libros(request):
    return render(request,"tecnologia_libros.html")

def audiolibros(request):
    return render(request,"audiolibros.html")