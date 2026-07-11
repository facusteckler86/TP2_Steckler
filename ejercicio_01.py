from datetime import date

notas = [0,3,7,9,5,10,2,1,4,6,8]

notas_aprobadas = list(filter(lambda notas: notas >= 7, notas))

fecha_actual = date.today()

print(f"Notas aprobadas: {notas_aprobadas}")
print(f"Reporte generado el: {fecha_actual}")

