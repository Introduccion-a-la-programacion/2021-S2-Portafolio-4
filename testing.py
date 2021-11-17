import Portafolio4;
import pytest;

evaluacion = Portafolio4.Evaluaciones("Universidad Los Angeles", "Ing. Computación", "Pedro Perez", "pperez@email.com")

def test_evaluaciones_1():
    assert evaluacion.agregarCurso("IC1001", "Introduccion a la programacion") == True
    
def test_evaluaciones_2():
    assert isinstance(evaluacion.agregarCurso("IC1001", "Taller de programacion"), str) == isinstance("Error: codigo repetido", str)
    
def test_evaluaciones_3():
    assert isinstance(evaluacion.mostrarCurso("IC1001"), str) == isinstance("Codigo = IC1001, Nombre= Introduccion a la Programacion", str)
    
def test_evaluaciones_4():
    assert evaluacion.crearEstudiante(2021258963, "Luis Mora", "lmora@email.com") == True
    
def test_evaluaciones_5():
    assert isinstance(evaluacion.mostrarEstudiante(2021258963), str) == isinstance("Carné = 2021258963, Nombre= Luis Mora, email= lmora@email.com", str)
    
def test_evaluaciones_6():
    assert evaluacion.agregarEvaluacion(2021258963, 2021, 2, "IC1001", 80) == True    
    
def test_evaluaciones_7():
    assert evaluacion.notaEstudianteCurso(2021258963, "IC1001", 2021, 2) == 80
    
def test_evaluaciones_8():
    assert isinstance(evaluacion.historialEstudianteCurso(2021258963, "IC1001", 2021, 2), str) == isinstance("Carné = 2021258963, Nombre= Luis Mora, email= lmora@email.com \nCodigo = IC1001, Nombre= Introduccion a la Programacion \n Nota=80", str)
    
def test_evaluaciones_9():
    assert isinstance(evaluacion.informacionCurso("IC1001", 2021, 2), str) == isinstance("Codigo = IC1001, Nombre= Introduccion a la Programacion \n Total Estudiante = 1", str)

def test_evaluaciones_10():
    assert isinstance(evaluacion.notaCurso("IC1001", 2021, 2), str) == isinstance("Codigo = IC1001, Nombre= Introduccion a la Programacion \n Estudiante: \n Carné = 2021258963, Nombre = Luis Mora, Nota = 80", str)

def test_evaluaciones_11():
    assert isinstance(evaluacion.estadisticasCurso("IC1001", 2021, 2), str) == isinstance("Codigo = IC1001, Nombre= Introduccion a la Programacion \n Total Estudiante = 1, Aprobados = 1, Reprobados = 0", str)
    
