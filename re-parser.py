import re


addresses = [
    ('Он проживал в городе Иваново на улице Наумова. ' 
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]
for address in addresses:
    pattern = r'город[а-я]*\s(?P<city>[а-яё]+).*?улиц[а-я]*\s(?P<street>[а-яё]+).*?дом[а-я]*\s(?P<house>\d+).*?квартир[а-я]*\s(?P<apartment>\d+)'
    address_match = re.search(pattern, address, re.IGNORECASE)
    if address_match is not None:
        city, street, house, apartment = address_match.groups()
        print(city, street, house, apartment, sep=' ')
