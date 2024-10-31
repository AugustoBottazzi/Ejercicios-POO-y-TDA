class Libro:
    def __init__ (self, titulo, autor, año_publicacion) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.año_publicacion}")

    libro_1 = ("It", "Stephen King", 1986)
    libro_2 = ("El Exorcista", "William Peter Blatty", 1971)
    libro_3 = ("El Resplandor", "Stephen King", 1977)

    libro_1.mostrar_info
    