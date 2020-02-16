from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode = 'a') as database:
		Email = data["Email"]
		Subject = data["Subject"]
		Message = data["Message"]
		file = database.write(f'\n{Email},{Subject},{Message}')

def write_to_csv(data):
	with open('database.csv', newline='' ,mode ='a') as database_csv:
		Email = data["Email"]
		Subject = data["Subject"]
		Message = data["Message"]
		csv_writer = csv.writer(database_csv, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([Email, Subject, Message])

@app.route('/submit_form', methods = ["POST", "GET"])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_file(data)
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'Something went wrong. Try again!'

# @app.route('/about.html')
# def about():
# 	return render_template("about.html")

# @app.route('/works.html')
# def works():
# 	return render_template("works.html")

# @app.route('/work.html')
# def work():
# 	return render_template('work.html')

# @app.route('/index.html')
# def home():
# 	return render_template('index.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/components.html')
# def components():
# 	return render_template('components.html')	