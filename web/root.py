import sys
from functools import wraps

from flask import Flask, render_template, g, redirect, url_for, request

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

from passageidentity import Passage, PassageError

PASSAGE_APPHANDLE = "kv9fjL97gD"
PASSAGE_API_KEY = "azVSPTBtHy.ywwcUW1VKve79xwKAnZI0j4uq9BdgxYNQrwMvW6t1LGD8Q4CC1XzlMmK9s2BEg2U"
psg = Passage(PASSAGE_APPHANDLE, PASSAGE_API_KEY)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            g.user = psg.authenticateRequest(request)
            print("Got user ${g.user}")
        except PassageError as e:
            print(f"Error: ${e}")
            g.user = None

        sys.stdout.flush()

        if g.user is None:
            return redirect(url_for('show', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/authd')
@login_required
def authd_page():
    return "Wooo!"

@app.route('/')
def show():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
