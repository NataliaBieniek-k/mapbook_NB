
from model import User

def add_user(users_data, map_widget, entry_name, entry_lokalizacja, entry_posty, entry_img_url, list_update_function):
    name = entry_name.get()
    location = entry_lokalizacja.get()
    posts = int(entry_posty.get())
    img_url = entry_img_url.get()

    users_data.append(User(name=name, location=location, posts=posts, img_url=img_url, map_widget=map_widget))
    list_update_function(users_data)

    entry_name.delete(0, "end")
    entry_lokalizacja.delete(0, "end")
    entry_posty.delete(0, "end")
    entry_img_url.delete(0, "end")
    entry_name.focus()


def user_info(users_data, list_box):
    list_box.delete(0, "end")
    for idx, user in enumerate(users_data):
        list_box.insert(idx, f"{user.name} {user.location} {user.posts} posty")


def delete_user(users_data, list_box, update_list):
    i = list_box.index("active")
    users_data[i].marker.delete()
    users_data.pop(i)
    update_list(users_data)


def user_details(users_data, list_box, labels, map_widget):
    i = list_box.index("active")
    user = users_data[i]

    labels["name"].config(text=user.name)
    labels["location"].config(text=user.location)
    labels["posts"].config(text=user.posts)

    map_widget.set_position(user.coords[0], user.coords[1])
    map_widget.set_zoom(14)


def edit_user(users_data, list_box, entries, button, update_user_func):
    i = list_box.index("active")

    entries["name"].insert(0, users_data[i].name)
    entries["location"].insert(0, users_data[i].location)
    entries["posts"].insert(0, users_data[i].posts)
    entries["img"].insert(0, users_data[i].img_url)

    button.config(text="Zapisz zmiany", command=lambda: update_user_func(users_data, i))


def update_user(users_data, i, entries, list_update_function, map_widget, button_add):
    users_data[i].name = entries["name"].get()
    users_data[i].location = entries["location"].get()
    users_data[i].posts = entries["posts"].get()
    users_data[i].img_url = entries["img"].get()

    users_data[i].coords = users_data[i].get_coordinates()
    users_data[i].marker.set_position(*users_data[i].coords)
    users_data[i].marker.set_text(text=users_data[i].name)

    list_update_function(users_data)

    button_add.config(text="Dodaj obiekt")

    for entry in entries.values():
        entry.delete(0, "end")
