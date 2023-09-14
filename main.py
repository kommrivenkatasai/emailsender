from flask import Flask, render_template, request
import smtplib
app = Flask(__name__)

my_email = "kommurivenkatasai1@gmail.com"
password = "vbjngnxanjccktwy"
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    name=request.form["uname"]
    email=request.form["uemail"]
    mess=request.form["uta"]
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"{name}\n{mess}")
    return "sucessssssss"


if __name__ == "__main__":
    app.run(debug=True,port=8090)
