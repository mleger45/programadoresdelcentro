


class Alumno:

    def __init__(self, nombre, materias):
        self.nombre = nombre
        self.materias = materias

    def obtenerNota(self, materia):
        for mat in self.materias:
            n_mat, nota = mat
            if n_mat == materia:
                return nota
        return 0

            
    def __repr__(self):
        return "<Nombre: {}, materias={}>".format(self.nombre, len(self.materias))


class AnalisisAlumnos:

    def __init__(self, alumnos):
        self.alumnos = self.crearObjetos(alumnos)

    def crearObjetos(self, alumnos):
        alumnosObjetos = []

        for nombreAlumno, materias in alumnos.items():
            alumnoObj = Alumno(nombreAlumno, materias)
            alumnosObjetos.append(alumnoObj)
        return alumnosObjetos

    def procesar(self, materia, notaminima):
        alumnosMateria = []
        for alumno in self.alumnos:
            if alumno.obtenerNota(materia) > notaminima:
                alumnosMateria.append(alumno)
        return alumnosMateria

        
if __name__ == "__main__":

    alumnos = {
        'Luis':[('matematica', 5), ('fisica', 7), ('quimica', 8)],
        'Carmen':[('matematica', 8), ('fisica', 4), ('quimica', 9), ('biologia', 10)],
        'Julio':[('matematica', 10), ('fisica', 2), ('quimica', 5)],
        'Maria':[('matematica', 10), ('fisica', 10), ('quimica', 10)],
    }

    analisis = AnalisisAlumnos(alumnos)
    # print(analisis.alumnos)
    alumnosMate = analisis.procesar("fisica", 5)
    print("Los alumnos que pasaron matematica fueron: {}" .format(alumnosMate))