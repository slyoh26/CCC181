"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "dev-only-change-me"  # moves into an environment variable in Week 11

SERVICES = [
    {"id": 1, "name": "Transcript of records (TOR)"},
    {"id": 2, "name": "Certificate of registration (COR)"},
    {"id": 3, "name": "Report of grades"},
]

REQUESTER_TYPES = ["Student", "Alumni"]

TICKETS = [
    {"number": 1, "name": "Maria Santos", "email": "maria@msuiit.edu.ph",
     "service_id": 1, "requester_type": "Student", "status": "waiting"},
    {"number": 2, "name": "Jun Reyes", "email": "jun@msuiit.edu.ph",
     "service_id": 2, "requester_type": "Alumni", "status": "waiting"},
]

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/join")
def join_form():
    return render_template("join.html", services=SERVICES,
                           requester_types=REQUESTER_TYPES, form={}, errors={})


@app.post("/join")
def join():
    form = request.form
    name = form.get("name", "").strip()
    email = form.get("email", "").strip().lower()
    service_id = form.get("service_id", type=int)
    requester_type = form.get("requester_type", "")

    errors = {}
    if not name:
        errors["name"] = "Enter your name."
    if "@" not in email:
        errors["email"] = "Enter a valid email address."
    if service_id not in [s["id"] for s in SERVICES]:
        errors["service_id"] = "Choose a document."
    if requester_type not in REQUESTER_TYPES:
        errors["requester_type"] = "Choose whether you are a student or an alumnus."

    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", services=SERVICES,
                               requester_types=REQUESTER_TYPES,
                               form=form, errors=errors), 400

    number = TICKETS[-1]["number"] + 1 if TICKETS else 1
    TICKETS.append({"number": number, "name": name, "email": email,
                    "service_id": service_id, "requester_type": requester_type,
                    "status": "waiting"})
    flash(f"You joined the queue. Your number is #{number}.", "success")
    return redirect(url_for("ticket", ticket_id=number))

@app.route("/staff")
def staff_dashboard():
    return "Staff dashboard coming soon"


def find_ticket(number):
    return next((t for t in TICKETS if t["number"] == number), None)


def people_ahead(t):
    return sum(1 for x in TICKETS
               if x["service_id"] == t["service_id"]
               and x["status"] == "waiting"
               and x["number"] < t["number"])


@app.get("/queue/<int:ticket_id>")
def ticket(ticket_id):
    t = find_ticket(ticket_id)
    if t is None:
        abort(404)
    service = next(s for s in SERVICES if s["id"] == t["service_id"])
    return render_template("ticket.html", ticket=t, service=service,
                           ahead=people_ahead(t))


@app.post("/queue/<int:ticket_id>/leave")
def leave(ticket_id):
    t = find_ticket(ticket_id)
    if t is None:
        abort(404)
    t["status"] = "no-show"
    flash("You left the queue.", "info")
    return redirect(url_for("index"))



if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)
