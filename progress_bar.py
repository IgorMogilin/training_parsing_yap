from time import sleep

from tqdm import tqdm


if __name__ == '__main__':
    for i in tqdm(range(200), desc='Прогресс б'):
        sleep(0.003)
    for i in tqdm(range(1000), desc='А вот и второй'):
        sleep(0.001)
    print('Ну накрнец-то')
