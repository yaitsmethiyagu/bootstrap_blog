import blog
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blog_api = "https://api.npoint.io/fd58021e59a162aaf4cb"

@app.route("/")
def home():
    all_blogs= []
    response = requests.get(blog_api)
    response = response.json()

    for blogs in response:
        new_blog = blog.Blog(id= blogs["id"],
                             title= blogs["title"],
                             subtitle= blogs["subtitle"],
                             body= blogs["body"],
                             author = blogs["author"],
                             date= blogs["date"]
                             )
        all_blogs.append(new_blog)

    return render_template("index.html", blogs_data = all_blogs)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",  methods = ["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form["name"]
        return render_template("contact.html", form_sender = name)

        return f"<h1>Thankyou {name}<h1> <h3>Form submitted successfully<h3>"


@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)


