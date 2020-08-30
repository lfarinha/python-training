from flask import Flask, request

from flask_training.connection import Connection

app = Flask(__name__)
app.config['ENV'] = 'development'

connection = Connection(server='192.168.1.189', database='flask', user='sa', password='40634630Leo*')


# HTTP METHODS POST, GET, PUT, DELETE, ETC.

# decorator
@app.route('/')
def root():
    return "This is my default page"


@app.route("/leo", methods=['POST'])
def leo_route():
    return "La pagina de leo"


@app.route("/daniel", methods=['GET'])
def daniel_route():
    return "La pagina de daniel"


@app.route('/authenticate', methods=['POST'])
def authentication():
    user_request = request.get_json()
    query = (f"SELECT * "
             f"FROM [dbo].[users] "
             f"WHERE username = '{user_request.get('username')}' "
             f"AND password = '{user_request.get('password')}'")
    data = connection.select(query)

    if len(data) > 0:
        if user_request.get('username') == data[0].get('username') and user_request.get('password') == data[0].get(
                'password'):
            return {"Status": f"welcome {user_request.get('username')}"}, 200
    else:
        return {"Error": "wrong credentials"}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
