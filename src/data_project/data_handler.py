from pathlib import Path
from data import Data


def load_data():
    project_folder = Path(__file__).parent.parent
    covid_data = []
    with open(f'{project_folder}\\covid_data\\usa_county_wise.csv') as covid_file:
        for line in covid_file:
            values = covid_file.readline().split(',')
            if len(values) >= 13:
                covid_data.append(Data(values[0], values[6], values[7], values[11], values[12], values[13]))
    return covid_data


def save_to_file(data):
    with open('log.txt', 'w') as log_file:
        for item in data:
            log_file.write(item.get_uid())
            log_file.write('\n')


if __name__ == '__main__':
    data_from_object = load_data()
    save_to_file(data_from_object)
