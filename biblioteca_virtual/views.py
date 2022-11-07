from django.shortcuts import render
from numpy import true_divide
from .forms import ContactoForm
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.urls import reverse
from datetime import datetime
# importo las tablas de la base de datos
from .models import Lista_libros_relacionados ,  Lista_usuarios , Lista_libros

def ver_tabla_libros(request):
  mi_tabla_libros = Lista_libros.objects.all().values()
  template = loader.get_template('ver_tabla_libros.html')
  context = {
    'mi_tabla_libros' : mi_tabla_libros
    }
  return HttpResponse(template.render(context, request))

def index(request):

    libros = Lista_libros.objects.all().values()    
    libros = {"libros": libros}

    return render(request, 'index.html', libros)

def resenias(request):

    libros = Lista_libros.objects.all().values()    
    libros = {"libros": libros}

    return render(request, 'reseñas.html', libros)

def buscar(request):
    
    busqueda= request.GET['busqueda']

    if request.GET['categoria']:

        categoria= request.GET['categoria']

        if categoria == "titulo":
            buscador = Lista_libros.objects.filter(libro_titulo__icontains=busqueda)
        elif categoria == "autor":
            buscador = Lista_libros.objects.filter(libro_autor__icontains=busqueda)
        else:   
            buscador = Lista_libros.objects.filter(libro_genero__icontains=busqueda)


    libros = {"libros": buscador}

    return render(request, 'busqueda.html', libros)


def sinopsis(request, id):
    
    libros_relacionados = Lista_libros_relacionados.objects.all().values()
    usuarios = Lista_usuarios.objects.all().values()
    libro_seleccionado = Lista_libros.objects.get(id=id)
    

    libros_y_usuarios = {"usuarios": usuarios,
                          "relacionados": libros_relacionados, "libro_seleccionado": libro_seleccionado}

    return render(request, 'sinopsis.html', libros_y_usuarios)


def equipo(request):
    return render(request, 'equipo.html', {})


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


# Vistas para poder agregar los datos a las tablas
# tres vistas separadas:
# a)	llenar_libros
# b)	llenar_recomendaciones
# c)	llenar_relacionados

# a)	llenar_libros
def llenar_libros_1(request):
    template = loader.get_template('llenar_libros_1.html')
    return HttpResponse(template.render({}, request))

  
  

def llenar_libros(request):
    lib =  [["El intercambio", "Lorem ipsum consectetuer adipiscing", "pic11", True, False, "1", "Un intercambio de casas es el detonante de la crisis de un matrimonio en este hipnótico thriller.", 
        "2018/26/4" , "REBECCA FLEET", "Ficción Literaria/ Novela Negra /Thriller", " Debolsillo", "Una deliciosa novela dedomestic noir.", "The Washington Post"],
        ["Dune", "Lorem ipsum consectetuer adipiscing", "pic12", False, True, "2", "Mezcla fascinante de aventura, misticismo, intrigas políticas y ecologismo, Dune se convirtió, desde el momento de su publicación, en un fenómeno de culto y en la mayor epopeya de ciencia-ficción de todos los tiempos.",
        "1965/1/8", "Frank Herbert", "Ciencia ficción/ Novela/ Literatura fantástica", "Debolsillo", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["El gato negro", "Lorem ipsum consectetuer adipiscing", "pic13", False, False, "3", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada",
        "1843/19/8", "Edgar Allan Poe", "Horror / Psicologico / Policial", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["Perdida", "Lorem ipsum consectetuer adipiscing", "pic14", True, True, "4", "No pierdas el tren.Perdida es tu próxima parada. El libro que se ha convertido en un referente del thriller psicológico contemporáneo.",
        "2012/24/5", "Flynn Gillian", "FICCIÓN / NARRATIVA / POLICIALES", "Debolsillo", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["El tunel", "Lorem ipsum consectetuer adipiscing", "pic15", False, True, "5", "El amor ilimitado truncado por un engaño convertirá el corazón de un hombre en un pedazo de duro y frío hielo y colocará en sus manos el cuchillo que pone final al sufrimiento. Sabato nos entrega los elementos básicos de su visión metafísica del existir.",
        "1948/1/1", "ERNESTO SABATO", "Novela / Novela Psicológica ", "SEIX BARRAL", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["El lector de cadaveres", "Lorem ipsum consectetuer adipiscing", "pic16", True, False, "6", "Un absorbente thriller histórico en el que la ambición y el odio van de la mano con el amor y la muerte en la exótica y fastuosa China medieval.",
        "2011/5/10", "Antonio Garrido", "Ficción, Thriller, Misterio, Suspenso", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["Memento", "Lorem ipsum consectetuer adipiscing", "pic22", False, False, "7", "La primera entrega de la trilogía «Versos, canciones y trocitos de carne», una novela negra narrada con un dinámico y atrevido lenguaje cinematográfico.",
        "2013/1/1", "CESAR PEREZ GELLIDA", "Horror / Psicologico / Policial", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["Quan Minimum", "Lorem ipsum consectetuer adipiscing", "pic17", True, False, "8", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada",
        "1843/19/8", "Edgar Allan Poe", "Horror / Psicologico / Policial", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["Credula Postero", "Lorem ipsum consectetuer adipiscing", "pic18", True, False, "9", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada",
        "1843/19/8", "Edgar Allan Poe", "Horror / Psicologico / Policial", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["Carpe Diem", "Lorem ipsum consectetuer adipiscing", "pic19", False, False, "10", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada",
        "1843/19/8", "Edgar Allan Poe", "Horror / Psicologico / Policial", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["Expectatum", "Lorem ipsum consectetuer adipiscing", "pic21", False, False, "11", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada",
        "1843/19/8", "Edgar Allan Poe", "Horror / Psicologico / Policial", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
        ["Veni Vidi Vici", "Lorem ipsum consectetuer adipiscing", "pic20", False, True, "12", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", 
        "1843/19/8", "Edgar Allan Poe", "Horror / Psicologico / Policial", "Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"]]

    for x in range(0 , 12): 
        librs=  Lista_libros( 
            libro_titulo = lib[x][0] ,    
            libro_descripcion_breve = lib[x][1] ,
            libro_imagen = lib[x][2] ,
            libro_nuevo = lib[x][3] ,    
            libro_leyendo = lib[x][4] ,
            libro_numero_id = lib[x][5] ,      
            libro_sinopsis_breve = lib[x][6] ,    
            libro_fecha_publicacion = datetime.strptime( lib[x][7] , '%Y/%d/%m'  ) ,    
            libro_autor  = lib[x][8] ,
            libro_genero = lib[x][9] ,    
            libro_formato = lib[x][10] ,  
            libro_critica_breve = lib[x][11] ,    
            libro_critica_fuente = lib[x][12] )    
        librs.save()
    return HttpResponseRedirect(reverse('index'))


def llenar_recomendaciones_1(request):
    template = loader.get_template('llenar_recomendaciones_1.html')
    return HttpResponse(template.render({}, request))

  
def llenar_recomendaciones(request):
    lu = [["Rene Favaloro", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam placeat cumque vero et! A alias sed, voluptas beatae", 3],
        ["Jose de San Martin", "quia obcaecati quisquam at eum assumenda dolorem? Rem omnis voluptates repellat aperiam voluptatem, quibusdam voluptas", 3],
        ["Victoria Ocampo", "fugiat, commodi at laudantium, minus corrupti porro unde nihil ipsum quae? Ducimus soluta delectus a consequuntur ", 2],
        ["Jorge Luis Borges", "error accusamus distinctio qui unde dolore quis minima suscipit maiores, voluptatum commodi iste, velit facere doloremque", 3],
        ["Alfonsina Storni", "aliquam. Debitis commodi veniam est dolore necessitatibus cumque et reiciendis, at quod, eum porro, amet obcaecati", 5],
        ["Maria Elena Walsh", "maxime fuga! Libero aperiam quae voluptatem obcaecati quos laudantium doloremque aspernatur exercitationem", 2],
        ["Mercedes Sosa", "consequuntur, repellendus id, hic cum deserunt quaerat voluptas aliquam cumque illo unde dolorem. Cupiditate", 4],
        ["Juan Manuel Fangio", "voluptatibus aliquid quos nemo aut asperiores iste nostrum possimus iusto, cum velit fugit ad tempore vitae labore", 5],
        ["Ernesto Sabato", "nesciunt repellendus culpa fugiat reiciendis, magni voluptate, distinctio dicta. Sit laboriosam neque nemo eveniet atque nulla.", 5]]

    for x in range(0, 9): 
        lis_usu=  Lista_usuarios(   usuario_nombre = lu[x][0] ,    
        usuario_critica_libro = lu[x][1] ,    
        usuario_puntuacion_libro = lu[x][2] )    
        lis_usu.save()
    return HttpResponseRedirect(reverse('index'))

def llenar_relacionados_1(request):
    template = loader.get_template('llenar_relacionados_1.html')
    return HttpResponse(template.render({}, request))

  
def llenar_relacionados(request):
    lr = [
        ["El buen hijo", "buenhijo"],
        ["Reina del grito", "reinagrito"],
        ["Kaiki: Cuentos de terror y locura", "kaiki"],
        ["Reinas del abismo", "reinasabismo"],
        ["El bazar de los malos sueños", "malossueños"],
        ["La habitacion de Nona", "habitacionnona"]
    ]

    for x in range(0, 6): 
        lis_rel= Lista_libros_relacionados(      libro_relacionado_titulo = lr[x][0] ,
        libro_relacionado_imagen =  lr[x][1]  )
        lis_rel.save()
    return HttpResponseRedirect(reverse('index'))