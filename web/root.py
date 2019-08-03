from flask import Flask
from api.api import api_root
from api.scrape import scrape_root

app = Flask(__name__)
app.register_blueprint(api_root)
app.register_blueprint(scrape_root)


@app.route('/')
def show():
  return 'Hello, World!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
