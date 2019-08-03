from flask import Flask, render_template
from api.api import api_root
from api.scrape import scrape_root

app = Flask(__name__,
            static_folder='./templates/carmenta/build/',
            template_folder='./templates/carmenta/build/')
app.register_blueprint(api_root)
app.register_blueprint(scrape_root)

@app.route('/')
def show():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
