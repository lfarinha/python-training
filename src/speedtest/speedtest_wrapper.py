from speedtest import Speedtest
import pprint


def test_connection():
    # crear un objecto del tipo Speedtest
    speed_test = Speedtest()
    # metodo para traer todos los servers
    speed_test.get_servers()
    # busca el mejor/mas cercano
    speed_test.get_best_server()
    # test el download
    speed_test.download()
    # test el upload
    speed_test.upload()

    return speed_test.results.dict()


if __name__ == '__main__':
    pprint.pprint(test_connection())
