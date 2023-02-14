from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route('/')
def index():
    url_for('static', filename='style.css')
    return render_template("index.html")

@app.route('/vehicles')
def vehicles():
    return 'vehicles'

@app.post("/account/login/<username>%<encryptedPassword>")
def login(username=None,encryptedPassword=None):
    pass
    
@app.route('/account', methods = ['GET', 'POST'])
def accountPage():
    return 'account'

if __name__ == "__main__":
  app.run()