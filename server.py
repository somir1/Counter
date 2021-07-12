from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "DAcounter"

# staring the session at 1 and when refrshes increase by 1


@app.route('/')
def startdashowindex():
    if "counts" not in session:
        session["counts"] = 0
    session["counts"] += 1
    return render_template('index.html')


@app.route('/addbuttons', methods=["post"])
def showdabuttons():
    if request.form["change"] == "add":
        session["counts"] += 1
    elif request.form["change"] == "reset":
        session["counts"] = 0
    return redirect('/')


@app.route('/destroy')
def killDasession():
    session.pop("counts")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
