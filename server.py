import blog
from flask import Flask, render_template, request
import requests
from smtplib import SMTP
from email.message import EmailMessage

app = Flask(__name__)

blog_api = "https://api.npoint.io/fd58021e59a162aaf4cb"


def send_email(name, sender_email, phone, form_message):
    email_id = "thoobfooz@gmail.com"
    app_password = "XXXXXXXXXXXXX"
    smtp_address = "smtp.gmail.com"
    subject = "New form submitted from Blog"

    em = EmailMessage()
    em["From"] = email_id
    em["Subject"] = subject
    em.set_content(f"Name: {name}, \nSender: {sender_email} \nPhone: {phone} \nMessage: {form_message}")

    with SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=email_id, password=app_password)
        connection.sendmail(from_addr=email_id, to_addrs="yaitsmethiyagu@gmail.com", msg=em.as_string())


@app.route("/")
def home():
    all_blogs = []
    response = requests.get(blog_api)
    response = response.json()

    for blogs in response:
        new_blog = blog.Blog(id=blogs["id"],
                             title=blogs["title"],
                             subtitle=blogs["subtitle"],
                             body=blogs["body"],
                             author=blogs["author"],
                             date=blogs["date"]
                             )
        all_blogs.append(new_blog)

    return render_template("index.html", blogs_data=all_blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form["name"]
        sender_email = request.form["sender_email"]
        phone = request.form["phone"]
        form_message = request.form["form_message"]

        send_email(name, sender_email, phone, form_message)

        return render_template("contact.html", form_sender=name)


@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
