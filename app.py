"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "dev-only-change-me"  # moves into an environment variable in Week 11

SERVICES = [
    {"id": 1, "name": "Transcript request"},
    {"id": 2, "name": "Enrollment certification"},
    {"id": 3, "name": "ID validation"},
]

TICKETS = [
    {"number": 1, "name": "Maria Santos", "email": "maria@msuiit.edu.ph", "service_id": 1, "status": "waiting"},
    {"number": 2, "name": "Jun Reyes", "email": "jun@msuiit.edu.ph", "service_id": 2, "status": "waiting"},
    {"number": 3, "name": "Liza Cruz", "email": "liza@msuiit.edu.ph", "service_id": 1, "status": "called"},
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/join")
def join_form():
    return render_template("join.html")


@app.route("/staff")
def staff_dashboard():
    return "Staff dashboard coming soon"


@app.route("/queue/<int:ticket_id>")
def ticket(ticket_id):
    # <int:ticket_id> only matches numbers, so /queue/abc returns 404.
    return render_template("ticket.html", ticket_id=ticket_id)



if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)
