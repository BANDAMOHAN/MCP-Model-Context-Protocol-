from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Home page with booking form for Mumbai.

    For this simple demo we fix the location to Mumbai and allow the user to
    choose dates and the number of adults/children (default 2 adults + 2 kids).
    """
    if request.method == "POST":
        check_in = request.form["check_in"]
        check_out = request.form["check_out"]
        adults = int(request.form["adults"])
        children = int(request.form["children"])

        location = "Mumbai"  # Fixed location for this demo
        total_guests = adults + children

        return render_template(
            "confirmation.html",
            check_in=check_in,
            check_out=check_out,
            location=location,
            adults=adults,
            children=children,
            total_guests=total_guests,
        )

    return render_template("index.html")


@app.route("/confirmation")
def confirmation():
    # In this simple app users should reach this page only via the form POST
    return "This is a placeholder for the confirmation page. You should not reach here directly."


if __name__ == "__main__":
    app.run(debug=True)
