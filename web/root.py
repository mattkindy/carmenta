from flask import Flask
from api.api import api_page

app = Flask(__name__)
app.register_blueprint(api_page, url_prefix='/api')


@app.route('/')
def show():
  return 'Hello, World!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
