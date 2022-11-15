from flask   import render_template
from argon_app import app


@app.route("/", methods=["GET"])
def dashboard():
  return render_template('pages/dashboard.html', segment='dashboard')


@app.route("/billing", methods=["GET"])
def billing():
  return render_template('pages/billing.html', segment='billing')


@app.route("/tables", methods=["GET"])
def tables():
  return render_template('pages/tables.html', segment='tables')


@app.route("/virtual-reality", methods=["GET"])
def virtual_reality():
  return render_template('pages/virtual-reality.html', segment='vr')


@app.route("/rtl", methods=["GET"])
def rtl():
  return render_template('pages/rtl.html', segment='rtl')


@app.route("/profile", methods=["GET"])
def profile():
  return render_template('pages/profile.html', segment='profile')


@app.route("/sign-in", methods=["GET"])
def signin():
  return render_template('accounts/sign-in.html')


@app.route("/sign-up", methods=["GET"])
def signup():
  return render_template('accounts/sign-up.html')