import requests
from bs4 import BeautifulSoup
import random

users: list = [
    {"name": "Kasia", "location": "Warszawa", "posts": 3, "img_url":""},
    {"name": "Basia", "location": "Kraków", "posts": 5, "img_url":""},
    {"name": "Asia", "location": "Wrocław", "posts": 7, "img_url":""},
]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów ")


def add_user(users_data: list) -> None:
    name: str = input("Podaj imie nowego znajomego: ")
    location: str = input("Podaj nazwę miejscowosci: ")
    posts: int = int(input("Podaj liczbę postów: "))
    users_data.append({"name": name, "location": location, "posts": posts})

def remove_user(users_data: list)->None:
    tmp_name:str=input("Podaj imię użytkownika do usunięcia ze znajomych: ")
    for user in users_data:
        if user["name"] == tmp_name:
            users.remove(user)

def update_user(users_data: list)->None:
    tmp_name:str=input("Podaj imię użytkownika do aktualizacji: ")
    for user in users_data:
        if user["name"] == tmp_name:
            user["name"]=input("Podaj nowe imię użytkownika: ")
            user["location"]=input("Podaj nową miejscowość: ")
            user["posts"]=input("Podaj nową liczbę postów: ")


def get_coordinates(city_name:str)->list:
    url:str=f'https://pl.wikipedia.org/wiki/{city_name}'
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
    response = requests.get(url, headers=headers)
    #print(response.status_code)
    #print(response.text)
    response_html=BeautifulSoup(response.text, 'html.parser')
    #print(response_html.prettify)
    latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    #print(latitude)
    longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
    #print(longitude)
    return[latitude,longitude]
#print(get_coordinates("Wrocław"))

import folium
import random

def get_map(users_data:list)->None:

    for user in users_data:
         user["img_url"] = f"https://randomuser.me/api/portraits/women/{random.randint(0, 99)}.jpg"

    m = folium.Map(location=[52.0, 19.0], zoom_start=6)

    for user in users:
         popup = (
             f"Użytkownik: <b>{user['name']}</b><br>"
             f"Liczba postów: {user['posts']}<br>"
             f"<img src=\"{user['img_url']}\" width=\"100\" alt=\"zdjęcie\"/>"
         )

         folium.Marker(
             location=get_coordinates(user["location"]),
             tooltip=f"{user['name']} ({user['location']})",
             popup=popup,
             icon=folium.Icon(icon="user"),
         ).add_to(m)


    m.save("notatnik.html")

while True:
    print("======MENU======")
    print("0. Wyjście z programu")
    print("1. Wyświetlanie aktywności znajomych")
    print("2. Dodawanie znajomego")
    print("3. Usuń znajomego")
    print("4. Aktualizacja znajomego")
    print("5. Generuj mape")
    print("==========================")

    tmp_choice: int = int(input("Wybierz opcję menu: "))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        print("wybrano funkcje wyświetlania aktywności znajomych")
        user_info(users)
    if tmp_choice == 2:
        print("wybrano funkcje dodawania znajomego")
        add_user(users)
    if tmp_choice == 3:
        print("wybrano funkcje usuwania znajomych")
        remove_user(users)
    if tmp_choice == 4:
        print("wybrano funkcje aktualizowania znajomych")
        update_user(users)
    if tmp_choice == 5:
        print("wybrano funkcje wyswietlania mapy")
        get_map(users)