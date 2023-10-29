import random
import math

# Şehirlerin koordinatlarını temsil eden bir liste
cities = {
    "A": (0, 5),
    "B": (1, 7),
    "C": (2, 3),
    "D": (4, 9),
    "E": (6, 8)
}

# Rastgele bir başlangıç yolunun oluşturulması
def generate_initial_solution(cities):
    city_list = list(cities.keys())
    random.shuffle(city_list)
    return city_list

# İki şehir arasındaki mesafeyi hesaplayan fonksiyon
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Bir yolun uzunluğunu hesaplayan fonksiyon
def path_length(path):
    length = 0
    for i in range(len(path) - 1):
        length += distance(path[i], path[i + 1])
    length += distance(path[-1], path[0])  # Son şehirden başlangıç şehrine dönüş
    return length

# Hill Climbing algoritması
def hill_climbing(cities, max_iterations):
    current_solution = generate_initial_solution(cities)
    current_length = path_length(current_solution)

    for _ in range(max_iterations):
        # Rastgele iki şehir seç ve swap işlemi yap
        i, j = random.sample(range(len(current_solution)), 2)
        new_solution = current_solution[:]
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

        new_length = path_length(new_solution)

        if new_length < current_length:
            current_solution = new_solution
            current_length = new_length

    return current_solution, current_length

# Ana fonksiyon
if __name__ == "__main__":
    max_iterations = 10000
    best_solution, best_length = hill_climbing(cities, max_iterations)
    print("En iyi yol:", best_solution)
    print("En iyi yol uzunluğu:", best_length)