
users:list=[
    {'name': 'Kasia', 'location': 'Warszawa', 'posts': 3},
    {'name': 'Asia', 'location': 'Krakow', 'posts': 5},
    {'name': 'Basia', 'location': 'Wroclaw', 'posts': 7},

]

for user in users:
    print(f'Twoja znajoma {user['name']} z miejscowości {user['location']}opublikował {user['posts']} postów ')
