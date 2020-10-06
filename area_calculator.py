from tkinter import Tk, LEFT, RIGHT, TOP, BOTTOM, X, StringVar, NE, E, NW, W, S, SE, SW, N
from tkinter.ttk import Button, Entry, Label, Style, Frame

# Funciones


def getAreaT():
    # if  # len(str(base_value.get())) > 0:
    try:
        base = float(base_value.get())
        high = float(high_value.get())
        area = (base * high) / 2
        lbl_areaTriangle.set(f'El área del triángulo es {area}')
    # else:
    except ValueError:
        lbl_areaTriangle.set('Escribe sólo números...')


def getAreaS():
  # if  # len(str(base_value.get())) > 0:
    try:
        side = float(side_value.get())
        area = side * side
        lbl_areaSquare.set(f'El área del cuadrado es {area}')
    # else:
    except ValueError:
        lbl_areaSquare.set('Escribe sólo números...')

# Estilos para los widgets


# Creamos la ventana principal
root = Tk()
root.geometry('800x600')
root.title('Calculadora de áreas v.1.0')

frm_triangle = Frame(root)
frm_square = Frame(root)
frm_circle = Frame(root)

Label(root, text="Cálculo de áreas").pack(side=TOP, expand=0)


Label(frm_triangle, text="Triángulo").pack(side=TOP)

frm_base = Frame(frm_triangle)
Label(frm_base, text="Base").pack(side=LEFT, expand=0)
base_value = StringVar()
Entry(frm_base, textvariable=base_value).pack(
    side=LEFT, fill=X, expand=1)
frm_base.pack(side=TOP)

frm_high = Frame(frm_triangle)
Label(frm_high, text="Altura").pack(side=LEFT, expand=0)
high_value = StringVar()
Entry(frm_high, textvariable=high_value).pack(
    side=LEFT, fill=X, expand=1)
frm_high.pack(side=TOP)

frm_button = Frame(frm_triangle)
Button(frm_button, text='Calcular área', command=getAreaT).pack()
lbl_areaTriangle = StringVar()
# lbl_areaTriangle.set('')
Label(frm_button, textvariable=lbl_areaTriangle).pack()
frm_button.pack(fill=X, expand=1)

frm_triangle.pack(side=LEFT, expand=0, anchor=N)


Label(frm_square, text="Cuadrado").pack(side=TOP)

frm_side = Frame(frm_square)
Label(frm_side, text="Lado").pack(side=LEFT, expand=0)
side_value = StringVar()
Entry(frm_side, textvariable=side_value).pack(
    side=LEFT, fill=X, expand=1)
frm_side.pack(side=TOP)

frm_button = Frame(frm_square)
Button(frm_button, text='Calcular área', command=getAreaS).pack()
lbl_areaSquare = StringVar()
# lbl_areaTriangle.set('')
Label(frm_button, textvariable=lbl_areaSquare).pack()
frm_button.pack(fill=X, expand=1)

frm_square.pack(side=RIGHT, expand=0, anchor=NE)

frm_circle.pack(fill=X)


root.mainloop()
