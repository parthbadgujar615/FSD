from flask import Flask, render_template, request
from models import db, Student

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']

        student = Student(
            name=name,
            email=email
        )

        db.session.add(student)
        db.session.commit()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)