from subprocess import Popen, PIPE, STDOUT
from pathlib import Path
import json
import time

from connection import Connection

PATH_TO_SPEEDTEST = Path(__file__).parent


def do_the_test():
    speedtest = Popen(f'{PATH_TO_SPEEDTEST}\\speedtest_cli\\speedtest.exe -f json',
                      shell=True,
                      stdin=PIPE,
                      stdout=PIPE,
                      stderr=STDOUT)
    # STRING = BYTES
    results = speedtest.stdout.read().decode('utf-8')
    # DICTIONARY = JSON
    test_results = json.loads(results)
    download = round(float(test_results['download']['bandwidth']) / 131072)
    upload = round(float(test_results['upload']['bandwidth']) / 131072)
    ping = round(test_results['ping']['latency'])
    print(download, upload, ping)
    test_results['download']['bandwidth'] = str(download)
    test_results['upload']['bandwidth'] = str(upload)
    test_results['ping']['latency'] = str(ping)
    print(test_results)
    save_to_database(test_results)


def save_to_database(results):
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    connection = Connection(server='192.168.1.189', database='internet_test', user='sa', password='40634630Leo*')
    query = ("INSERT INTO [dbo].speed_test([download], [upload], [ping], [date], [ip], [link]) "
             f"VALUES('{results['download']['bandwidth']}', "
             f"'{results['upload']['bandwidth']}', "
             f"'{results['ping']['latency']}', "
             f"'{date}', "
             f"'{results['interface']['externalIp']}', "
             f"'{results['result']['url']}')")
    connection.execute(query)


if __name__ == '__main__':
    do_the_test()
