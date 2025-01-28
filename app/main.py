from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/submit",methods= ["GET","POST"])
def submit(request):
    if request.method == "POST":
        username  = request.form['username']
        return f"The username of user is {username}"
    return render_template("base.html")
    
@app.route("/about")
def about():
    return "This is the About"

@app.route("/username/<username>")
def user(username):
    return f"The username is {username}"

if __name__ == "__main__":
    app.run(debug=True)