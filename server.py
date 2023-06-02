import blog
from flask import Flask, render_template
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

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)


