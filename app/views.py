from flask import render_template, redirect, url_for, flash
from app import app
from app import db
from app.forms import AddRepair                       
from app.models import Repairs


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