import requests_cache

from tqdm import tqdm


API_KEY = 'cIYRIFkDV9ljgGfd7AJghr6Tcgmy8COoXyRfI6Hi'
DATE_START = '2025-05-25'
DATE_END = '2025-05-31'
NASA_API_URL = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={DATE_START}&end_date={DATE_END}&api_key={API_KEY}'
dangerous_asteroid = []


if __name__ == '__main__':
    session = requests_cache.CachedSession()
    session.cache.clear()
    response = session.get(NASA_API_URL)
    data = response.json()
    for asteroids in data["near_earth_objects"].values():
        for asteroid in asteroids:
            if asteroid["is_potentially_hazardous_asteroid"]:
                dangerous_asteroid.append(asteroid)
    print(f'Найдено {len(dangerous_asteroid)} опасных астероидов')
    for asteroid in tqdm(dangerous_asteroid, desc="Обработка астероидов", unit="шт"):
        print(f'Название: {asteroid["name"]}')
        print(f"Диаметр: {asteroid['estimated_diameter']['meters']['estimated_diameter_max']:.2f} м")
        speed = float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
        print(f"Скорость: {speed:.2f} км/ч")
        print('---------------------')
