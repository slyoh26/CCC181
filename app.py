"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from flask import Flask, render_template

app = Flask(__name__)

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
    # render_template looks inside the templates/ folder and passes
    # keyword arguments to the template as variables.
    return render_template("index.html", name="Ana", tickets=TICKETS, services=SERVICES)


@app.route("/queue/<int:ticket_id>")
def ticket(ticket_id):
    # <int:ticket_id> only matches numbers, so /queue/abc returns 404.
    return render_template("ticket.html", ticket_id=ticket_id)


@app.route("/hello")
def hello():
    # The plain-string version from the Routes slide.
    return "Hello, CCC181!"


if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)
