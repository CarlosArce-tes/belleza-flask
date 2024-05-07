from flask import Blueprint, render_template
admin = Blueprint('admin', __name__)
@admin.route('/panel')
def panel():
    return render_template('rehistro.html')