import random
from tkinter import *

caca = []

def sortear():

    lado = random.randint(1,3)
    fila = random.randint(1,12)
    cadeira = random.randint(1,9)

    if lado == 1:

        fila = random.randint(1,10)
        string_lado = "Esquerdo"
    else:
        string_lado = "Direito"

    print("######### SORTEIO ######### \n")
    print("Lado: %s " % string_lado)
    print("Fila: %d " % fila)
    print("Cadeira: %d" % cadeira)

    lbl_lado_result["text"]= (string_lado)
    lbl_fila_result["text"] = (str(fila))
    lbl_cad_result["text"] = (str(cadeira))

root = Tk()
root['bg'] = "black"
root.title("Sorteio - II Semana de Ciência e Fé")
frame = Frame(root)
frame['bg'] = "black"

frame.pack()
# root.geometry("500x500") #You want the size of the app to be 500x500
root.resizable(0, 0)
lbl_titulo = Label(frame, text="Sorteio" , fg="white", bg="black")
lbl_titulo["font"] = ("Comic Sans", "30", "bold")
# lbl_sorteio = Label(frame, text=lado)
lbl_titulo.pack(pady=10)

lbl_lado = Label(frame, text="Lado:", fg="white", bg="black")
lbl_lado["font"] = ("Verdana", "15", "bold")
lbl_lado.pack(pady=20)

lbl_lado_result = Label(frame, text="", fg="blue", bg="black")
lbl_lado_result["font"] = ("Verdana", "30", "bold")
lbl_lado_result.pack(pady=10)

lbl_fila = Label(frame, text="Fila:", fg="white", bg="black")
lbl_fila["font"] = ("Verdana", "15", "bold")
lbl_fila.pack(pady=10)

lbl_fila_result = Label(frame, text="", fg="blue", bg="black")
lbl_fila_result["font"] = ("Verdana", "30", "bold")
lbl_fila_result .pack(pady=10)

lbl_cad = Label(frame, text="Cadeira:", fg="white", bg="black")
lbl_cad["font"] = ("Verdana", "15", "bold")
lbl_cad.pack(pady=10)

lbl_cad_result = Label(frame, text="", fg="blue", bg="black")
lbl_cad_result["font"] = ("Verdana", "30", "bold")
lbl_cad_result.pack(pady=10)

btn = Button(frame, text='Sortear', command=sortear , fg="blue", bg ="white", relief="flat")
btn["font"] = ("Verdana", "20", "bold")
btn.pack(pady=20)



w = 400
h = 600




ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

print(root.winfo_height())
print(root.winfo_width())

root.mainloop()


