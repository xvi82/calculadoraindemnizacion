import math
from datetime import datetime, timedelta
from tkcalendar import DateEntry
from tkinter import Tk, Label, Entry, Button, W, mainloop
import re

def indemnizacion_despido(fecha_antiguedad, salari, fecha_despido):
    fechalimite = datetime.strptime('12/02/2012', '%d/%m/%Y').date()
    antig = datetime.strptime(fecha_antiguedad, '%d/%m/%Y').date()
    despid = datetime.strptime(fecha_despido, '%d/%m/%Y').date()
    salario = float(re.sub(',', '.', salari))
    if antig > fechalimite:
        dif = math.ceil(((despid - antig) / timedelta(days=1))) + 1
        daf = math.ceil(dif / 30.41666667)
        indem = daf * salario * 2.75
        return indem
    else:
        dif1 = math.ceil(((fechalimite - antig) / timedelta(days=1))) + 1
        daf1 = math.ceil((dif1 / 30.41666667))
        indemprev = daf1 * salario * 3.75
        dif2 = math.ceil(((despid - fechalimite) / timedelta(days=1))) + 1
        daf2 = math.ceil(dif2 / 30.41666667)
        indempost = daf2 * salario * 2.75
        indem2 = indemprev + indempost
        return indem2

def show_answer():
    indemnizacion = indemnizacion_despido(antig.get(), salario.get() ,despid.get())
    result.insert(0, round(indemnizacion, 2))

main = Tk()
main.title("Calculadora Indemnización")
Label(main, text = "Salario").grid(row=0)
Label(main, text = "Antiguedad").grid(row=1)
Label(main, text = "Despido").grid(row=2)
Label(main, text = "Indemnización").grid(row=3)

salario = Entry(main)
antig = DateEntry(main, date_pattern='dd/mm/Y', width=17,)
despid = DateEntry(main, date_pattern='dd/mm/Y', width=17,)
result = Entry(main)

salario.grid(row=0, column=1, padx=5, pady=5)
antig.grid(row=1, column=1, padx=5, pady=5)
despid.grid(row=2, column=1, padx=5, pady=5)
result.grid(row=3, column=1, padx=5, pady=5)

Button(main, text='Cerrar', command=main.destroy).grid(row=5, column=0, sticky=W, padx=5, pady=5)
Button(main, text='Calcular', command=show_answer).grid(row=5, column=1, sticky=W, padx=5, pady=5)

mainloop()