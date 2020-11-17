from plant_app import plant_app
from flask import render_template

@plant_app.route("/admin/dashboard")
def admin_dashboard():
    return render_template('/admin/dashboard.html')
