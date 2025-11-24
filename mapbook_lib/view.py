
from tkinter import *
import tkintermapview
from controller import *

def start_gui():
    root = Tk()
    root.title("Mapbook")
    root.geometry("1025x760")

    users = []

    ramka_lista = Frame(root)
    ramka_form = Frame(root)
    ramka_info = Frame(root)
    ramka_mapa = Frame(root)

    ramka_lista.grid(row=0, column=0)
    ramka_form.grid(row=0, column=1)
    ramka_info.grid(row=1, column=0, columnspan=2)
    ramka_mapa.grid(row=2, column=0, columnspan=2)

    map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1025, height=600, corner_radius=0)
    map_widget.set_position(52.0, 21.0)
    map_widget.set_zoom(6)
    map_widget.grid(row=0, column=0)

    # LISTA
    label_lista = Label(ramka_lista, text="Lista obiektów")
    label_lista.grid(row=0, column=0, columnspan=3)

    list_box = Listbox(ramka_lista)
    list_box.grid(row=1, column=0, columnspan=3)

    # FORMULARZ
    Label(ramka_form, text="Formularz:").grid(row=0, column=0, columnspan=2)

    labels = ["Imie", "Lokalizacja", "Posty", "Obrazek"]
    entries = {}

    for i, lbl in enumerate(labels, start=1):
        Label(ramka_form, text=f"{lbl}: ").grid(row=i, column=0, sticky=W)
        entry = Entry(ramka_form)
        entry.grid(row=i, column=1)
        entries[lbl.lower()] = entry

    button_add = Button(
        ramka_form,
        text="Dodaj obiekt",
        command=lambda: add_user(
            users, map_widget,
            entries["imie"], entries["lokalizacja"], entries["posty"], entries["obrazek"],
            lambda u: user_info(u, list_box)
        )
    )
    button_add.grid(row=5, column=0, columnspan=2)

    # Szczegóły
    Label(ramka_info, text="Szczegóły obiektu: ").grid(row=0, column=0, sticky=W)

    labels_info = {
        "name": Label(ramka_info, text="..."),
        "location": Label(ramka_info, text="..."),
        "posts": Label(ramka_info, text="...")
    }

    Label(ramka_info, text="Imię:").grid(row=1, column=0)
    labels_info["name"].grid(row=1, column=1)

    Label(ramka_info, text="Lokalizacja:").grid(row=1, column=3)
    labels_info["location"].grid(row=1, column=4)

    Label(ramka_info, text="Posty:").grid(row=1, column=5)
    labels_info["posts"].grid(row=1, column=6)

    # Przyciski listy
    Button(ramka_lista, text="Pokaż szczegóły",
           command=lambda: user_details(users, list_box, labels_info, map_widget)).grid(row=2, column=0)

    Button(ramka_lista, text="Usuń obiekt",
           command=lambda: delete_user(users, list_box, lambda u: user_info(u, list_box))).grid(row=2, column=1)

    Button(ramka_lista, text="Edytuj obiekt",
           command=lambda: edit_user(
               users, list_box,
               {
                   "name": entries["imie"],
                   "location": entries["lokalizacja"],
                   "posts": entries["posty"],
                   "img": entries["obrazek"],
               },
               button_add,
               lambda us, i: update_user(
                   us, i,
                   {
                       "name": entries["imie"],
                       "location": entries["lokalizacja"],
                       "posts": entries["posty"],
                       "img": entries["obrazek"],
                   },
                   lambda u: user_info(u, list_box),
                   map_widget,
                   button_add
               )
           )).grid(row=2, column=2)

    root.mainloop()
