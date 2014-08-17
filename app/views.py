from flask import render_template, redirect, url_for, flash
from app import app
from app import db
from app import admin
from app.forms import AddRepair, SelectReport                     
from app.models import Repairs
from flask.ext.admin.contrib.sqla import ModelView

# Admin views for modifying records
# need to make this available via log in only.
admin.add_view(ModelView(Repairs, db.session))


#Home page route
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	# Get repairs for display on home page
	repairs = Repairs.query.order_by('date desc').all()
	# Render the home page with list of repairs
	return render_template('index.html', repairs = repairs)

# Route for data entry (Repairs)
@app.route('/repairs', methods = ['GET', 'POST'])
def addrepair():
	form = AddRepair()
	# Logic for inserting data into repair.db
	if form.validate_on_submit():
		new_repair = Repairs(date = form.date.data,
							pc_num = form.pc_num.data,
							franchise = form.franchise.data,
							problem = form.problem.data,
							solution = form.solution.data,
							tech = form.tech.data,
							pc_app = form.pcapp.data,
							pc_mb = form.pcmb.data)
		db.session.add(new_repair)
		db.session.commit()
		flash('Database updated!')
		return render_template('repairs.html', form = form)
	return render_template('repairs.html', form = form)

# Route for Reports
@app.route('/reports', methods=['GET','POST'])
def reports():
    form = SelectReport()
    if form.validate_on_submit():       
        if form.report_type.data == 'all':
            return redirect(url_for('all'))

    return render_template('reports.html', form=form)



# Route for All Repairs
@app.route('/all', methods=['GET','POST'])
def all():
    repairs = Repairs.query.order_by('date desc').all()
    return render_template('all.html', repairs = repairs)
