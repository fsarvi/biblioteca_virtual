from django.shortcuts import render
from numpy import true_divide

def index(request):
######################################provisorio#####################################
    """ lista provisoria hasta que podamos implementar la base de datos """
    lista_libros = [["El intercambio","Lorem ipsum consectetuer adipiscing","pic11",True,False,"1", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Dune","Lorem ipsum consectetuer adipiscing","pic12",False,True,"2", "Mezcla fascinante de aventura, misticismo, intrigas políticas y ecologismo, Dune se convirtió, desde el momento de su publicación, en un fenómeno de culto y en la mayor epopeya de ciencia-ficción de todos los tiempos.", "Agosto de 1965", "Frank Herbert", "Ciencia ficción/ Novela/ Literatura fantástica","Debolsillo", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["El gato negro","Lorem ipsum consectetuer adipiscing","pic13",False,False,"3", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Perdida","Lorem ipsum consectetuer adipiscing","pic14",True,True,"4", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["El tunel","Lorem ipsum consectetuer adipiscing","pic15",False,True,"5", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["El lector de cadaveres","Lorem ipsum consectetuer adipiscing","pic16",True, False,"6", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Memento","Lorem ipsum consectetuer adipiscing","pic22",False,False,"7", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Quan Minimum","Lorem ipsum consectetuer adipiscing","pic17",True, False,"8", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Credula Postero","Lorem ipsum consectetuer adipiscing","pic18", True, False,"9", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Carpe Diem","Lorem ipsum consectetuer adipiscing","pic19",False,False,"10", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Expectatum","Lorem ipsum consectetuer adipiscing","pic21",False,False,"11", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Veni Vidi Vici","Lorem ipsum consectetuer adipiscing","pic20",False,True,"12", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"]]

    libros = {"titulos" : lista_libros}
######################################################################################    
    return render(request, 'index.html', libros)


def sinopsis(request, id):
######################################provisorio#####################################
    """ listas provisorias hasta que podamos implementar la base de datos """
    libros = [["El intercambio","Lorem ipsum consectetuer adipiscing","pic11",True,False,"1", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Dune","Lorem ipsum consectetuer adipiscing","pic12",False,True,"2", "Mezcla fascinante de aventura, misticismo, intrigas políticas y ecologismo, Dune se convirtió, desde el momento de su publicación, en un fenómeno de culto y en la mayor epopeya de ciencia-ficción de todos los tiempos.", "Agosto de 1965", "Frank Herbert", "Ciencia ficción/ Novela/ Literatura fantástica","Debolsillo", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["El gato negro","Lorem ipsum consectetuer adipiscing","pic13",False,False,"3", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Perdida","Lorem ipsum consectetuer adipiscing","pic14",True,True,"4", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["El tunel","Lorem ipsum consectetuer adipiscing","pic15",False,True,"5", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["El lector de cadaveres","Lorem ipsum consectetuer adipiscing","pic16",True, False,"6", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Memento","Lorem ipsum consectetuer adipiscing","pic22",False,False,"7", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Quan Minimum","Lorem ipsum consectetuer adipiscing","pic17",True, False,"8", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Credula Postero","Lorem ipsum consectetuer adipiscing","pic18", True, False,"9", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Carpe Diem","Lorem ipsum consectetuer adipiscing","pic19",False,False,"10", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Expectatum","Lorem ipsum consectetuer adipiscing","pic21",False,False,"11", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"],
    ["Veni Vidi Vici","Lorem ipsum consectetuer adipiscing","pic20",False,True,"12", "El gato negro y otros relatos es una recopilacion de los cuentos mas notables de Poe, en los que destaca El gato negro, William Wilson y La carta robada", "19 de agosto, 1843", "Edgar Allan Poe", "Horror / Psicologico / Policial","Letras de Sopa", "Perturbadora, atrapante, magnifica", "El Canillita Times"]]

    libro_seleccionado = libros[id - 1]
    
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

    libros_y_usuarios = {"usuarios":lista_usuarios,"relacionados":lista_libros_relacionados, "libro_seleccionado": libro_seleccionado}
######################################################################################
    return render(request,'sinopsis.html',libros_y_usuarios)
