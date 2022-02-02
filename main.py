from tkinter import *
import backend

def add_command():
    backend.insert(uzivatel_text.get(), knihy_text.get())
    listb.insert(END, (uzivatel_text.get(), knihy_text.get()))

window = Tk()
window.wm_title("Kniznica")


#uzivatel, knihy
l1 = Label(window, text = "Uzivatel")
l1.grid(row=0, column=0)
l1 = Label(window, text = "Knihy")
l1.grid(row=0, column=2)

#policka pre uyivatela a knihy na pisanie
uzivatel_text = StringVar()
ent1 = Entry(window, textvariable = uzivatel_text)
ent1.grid(row = 0, column = 1)

knihy_text = StringVar()
ent2 = Entry(window, textvariable = knihy_text)
ent2.grid(row = 0, column = 4)

# box pod polickami
listb = Listbox(window, height=6, width=35)
listb.grid(row=2, column=0, rowspan=6, columnspan=2)

#scrollbar
sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6, columnspan=2)

listb.configure(yscrollcommand=sb.set)
sb.configure(command=listb.yview)

#tlacitka
b1 = Button(window, text = "Spusti kniznicu", width=35)
b1.grid(row=1, column=5)
b2 = Button(window, text = "Vytvor nového užívateľa", width=35)
b2.grid(row=2, column=5)
b3 = Button(window, text = "Vymaž užívateľa", width=35)
b3.grid(row=3, column=5)
b4 = Button(window, text = "Zobraz zoznam všetkých užívateľov", width=35)
b4.grid(row=4, column=5)
b5 = Button(window, text = "Zobraz knihy ktoré boli zapožičané užívateľovi", width=35)
b5.grid(row=5, column=5)
b6 = Button(window, text = "Vyhľadanie užívateľa podľa mena a priezviska", width=35)
b6.grid(row=6, column=5)
b7 = Button(window, text = "Zadaj novú knihu", width=35)
b7.grid(row=7, column=5)
b8 = Button(window, text = " Zobraz zoznam všetkých kníh v knižnici", width=35)
b8.grid(row=8, column=5)
b9 = Button(window, text = " Vyhľadaj knihu podľa Názvu knihy", width=35)
b9.grid(row=9, column=5)
b10 = Button(window, text = " Zapožičaj knihu užívateľovi", width=35)
b10.grid(row=10, column=5)
b11 = Button(window, text = " Vráť knihu do knižnice od užívateľa", width=35)
b11.grid(row=11, column=5)

window.mainloop()