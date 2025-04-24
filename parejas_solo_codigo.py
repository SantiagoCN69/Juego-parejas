import random
import time
from tkinter import Tk, Button, DISABLED, messagebox

nivel_seleccionado = None

def elegir_nivel(nivel):
    global nivel_seleccionado
    nivel_seleccionado = nivel
    selector.destroy()

selector = Tk()
selector.title("Selecciona nivel")
Button(selector, text="Fácil", command=lambda: elegir_nivel("facil")).pack(pady=10)
Button(selector, text="Difícil", command=lambda: elegir_nivel("dificil")).pack(pady=10)
selector.mainloop()

if nivel_seleccionado == "facil":
    rows = 3
    columns = 4
    num_pairs = 6
else:
    rows = 4
    columns = 6
    num_pairs = 12

def close_window():
    root.destroy()

root = Tk()
root.title("Juego de las Parejas")
root.resizable(width=False, height=False)

buttons = {}
button_symbols = {}

first = True
previousX = None
previousY = None

moves = 0
pairs_found = 0
start_time = time.time()

symbols = [ u'\u2600', u'\u2600', u'\u2601', u'\u2601', u'\u2602', u'\u2602',
           u'\u2603', u'\u2603', u'\u25EF', u'\u25EF', u'\u2605', u'\u2605',
           u'\u2606', u'\u2606', u'\u260E', u'\u260E', u'\u260F', u'\u260F',
           u'\u25C6', u'\u25C6', u'\u25C7', u'\u25C7', u'\u263B', u'\u263B']

symbols = symbols[:num_pairs*2]
random.shuffle(symbols)

def show_symbol(x, y):
    global first, pairs_found
    global previousX, previousY, moves
    buttons[x, y]["text"] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
        moves += 1
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]["text"] != buttons[x, y]["text"]:
            time.sleep(0.5)
            buttons[previousX, previousY]["text"] = ""
            buttons[x, y]["text"] = ""
        else:
            buttons[previousX, previousY]['state'] = DISABLED
            buttons[x, y]['state'] = DISABLED
            pairs_found += 1
            if pairs_found == num_pairs:
                tiempo_total = int(time.time() - start_time)
                minutos = tiempo_total // 60
                segundos = tiempo_total % 60
                messagebox.showinfo(
                    "Fin del juego",
                    f"Número de movimientos utilizados: {moves}\nTiempo total: {minutos} min {segundos} seg",
                    parent=root)
                close_window()
        first = True
        
for x in range(rows):
    for y in range(columns):
        button = Button(command = lambda x=x, y=y: show_symbol(x, y), width=3, height=2)
        button.grid(column=y, row=x)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

root.mainloop()