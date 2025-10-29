users: list = [
    {'name': 'Kasia', 'location': 'Warszawa', 'posts': 3},
    {'name': 'Asia', 'location': 'Krakow', 'posts': 5},
    {'name': 'Basia', 'location': 'Wroclaw', 'posts': 7},

]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twoja znajoma {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów ')


while True:
    tmp_choice: int = int(input('Wybierz opcje menu'))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        print('Wybrano funkcję wyświetlania aktywności znajomych')
        user_info(users)
    if tmp_choice == 2:
        print("Wybrano funkcję dodawania znajomego")
    if tmp_choice == 3:
        print('Wybrano funkcję usuwania znajomego')
    if tmp_choice == 4:
        print('Wybrano funkcję aktualizacji danych znajomego')

# user_info petla z 13 i 14 linijki
