from flask import Flask, render_template
from api.api import api_root
from api.scrape import scrape_root
from api.cluster import cluster_root
from api.user import user_root
from database.models import db

app = Flask(__name__,
            static_folder='./templates/carmenta/build/',
            template_folder='./templates/carmenta/build/')

app.register_blueprint(api_root)
app.register_blueprint(scrape_root)
app.register_blueprint(cluster_root)
app.register_blueprint(user_root)

db.init_app(app)

with app.app_context():
  db.create_all()

from database.models import Candidate
c = Candidate("1","Walter S","mytitle","schools1", "work1", "location1", "cool")
with app.app_context():
    db.session.add(c)
    db.session.commit()

@app.route('/')
def show():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
