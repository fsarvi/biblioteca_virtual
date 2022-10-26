from django.shortcuts import render
from numpy import true_divide

def index(request):
######################################provisorio#####################################
    """ lista provisoria hasta que podamos implementar la base de datos """
    lista_libros = [["El intercambio","Lorem ipsum consectetuer adipiscing","pic11",True],
    ["Dune","Lorem ipsum consectetuer adipiscing","pic12",False,True],
    ["El gato negro","Lorem ipsum consectetuer adipiscing","pic13"],
    ["Perdida","Lorem ipsum consectetuer adipiscing","pic14",True,True],
    ["El tunel","Lorem ipsum consectetuer adipiscing","pic15",False,True],
    ["El lector de cadaveres","Lorem ipsum consectetuer adipiscing","pic16",True],
    ["Memento","Lorem ipsum consectetuer adipiscing","pic22"],
    ["Quan Minimum","Lorem ipsum consectetuer adipiscing","pic17",True],
    ["Credula Postero","Lorem ipsum consectetuer adipiscing","pic18", True],
    ["Carpe Diem","Lorem ipsum consectetuer adipiscing","pic19"],
    ["Expectatum","Lorem ipsum consectetuer adipiscing","pic21"],
    ["Veni Vidi Vici","Lorem ipsum consectetuer adipiscing","pic20",False,True]]

    libros = {"titulos" : lista_libros}
######################################################################################    
    return render(request, 'index.html', libros)


def sinopsis(request):
######################################provisorio#####################################
    """ listas provisorias hasta que podamos implementar la base de datos """
    lista_libros_relacionados = [
    ["El buen hijo","buenhijo"],
    ["Reina del grito","reinagrito"],
    ["Kaiki: Cuentos de terror y locura","kaiki"],
    ["Reinas del abismo","reinasabismo"],
    ["El bazar de los malos sueños","malossueños"],
    ["La habitacion de Nona","habitacionnona"],
    ]

    lista_usuarios = [["Rene Favaloro", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam placeat cumque vero et! A alias sed, voluptas beatae", 3],
    ["Jose de San Martin", "quia obcaecati quisquam at eum assumenda dolorem? Rem omnis voluptates repellat aperiam voluptatem, quibusdam voluptas", 3],
    ["Victoria Ocampo", "fugiat, commodi at laudantium, minus corrupti porro unde nihil ipsum quae? Ducimus soluta delectus a consequuntur ", 2],
    ["Jorge Luis Borges", "error accusamus distinctio qui unde dolore quis minima suscipit maiores, voluptatum commodi iste, velit facere doloremque", 3],
    ["Alfonsina Storni", "aliquam. Debitis commodi veniam est dolore necessitatibus cumque et reiciendis, at quod, eum porro, amet obcaecati", 5],
    ["Maria Elena Walsh", "maxime fuga! Libero aperiam quae voluptatem obcaecati quos laudantium doloremque aspernatur exercitationem", 2],
    ["Mercedes Sosa", "consequuntur, repellendus id, hic cum deserunt quaerat voluptas aliquam cumque illo unde dolorem. Cupiditate", 4],
    ["Juan Manuel Fangio", "voluptatibus aliquid quos nemo aut asperiores iste nostrum possimus iusto, cum velit fugit ad tempore vitae labore", 5],
    ["Ernesto Sabato", "nesciunt repellendus culpa fugiat reiciendis, magni voluptate, distinctio dicta. Sit laboriosam neque nemo eveniet atque nulla.", 5]]

    libros_y_usuarios = {"usuarios":lista_usuarios,"relacionados":lista_libros_relacionados}
######################################################################################
    return render(request,'sinopsis.html',libros_y_usuarios)
