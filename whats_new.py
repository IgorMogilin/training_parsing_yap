from bs4 import BeautifulSoup
import requests_cache
from urllib.parse import urljoin
from tqdm import tqdm

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})
    main_div_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})
    section_by_python = main_div_ul.find_all('li', attrs={'class': 'toctree-l1'})
    result = []
    for section in tqdm(section_by_python):
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(WHATS_NEW_URL, href)
        # Здесь начинается новый код!
        response = session.get(version_link)
        response.encoding = 'utf-8'  # Укажите кодировку utf-8.
        soup = BeautifulSoup(response.text, features='lxml')  # Сварите "супчик".
        h1 = soup.find('h1')  # Найдите в "супе" тег h1.
        dl = soup.find('dl')  # Найдите в "супе" тег dl.
        dl_text = dl.text.replace('\n', '')
        result.append((version_link, h1.text, dl_text))  # Добавьте в вывод на печать текст из тегов h1 и dl.
    for row in result:
        print(*row)
