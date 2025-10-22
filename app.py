from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg:///students"
)

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def __repr__(self):
        return f"{self.id} {self.first_name}"

def student_serializer(stud: Students) -> dict:
    return {
        "id": stud.id,
        "full_name": f"{stud.first_name} {stud.last_name}",
        "age": stud.age,
        "grade": stud.grade
    }

@app.route("/old_students/", methods=["GET"])
def old_students():
    old_studs = Students.query.filter(Students.age > 20).all()
    return jsonify([student_serializer(student) for student in old_studs])

@app.route("/young_students/", methods=["GET"])
def young_students():
    young_studs = Students.query.filter(Students.age <21).all()
    return jsonify([student_serializer(student) for student in young_studs])

@app.route("/advance_students/", methods=["GET"])
def advance_students():
    adv_studs = Students.query.filter(
        Students.age < 21,
        Students.grade == 'A'
    ).all()
    return jsonify([student_serializer(student) for student in adv_studs])

@app.route("/student_names", methods=["GET"])
def student_names():
    stud_names = Students.query.all()
    name_list = []
    for student in stud_names:
        name_list.append({
            "First name": student.first_name,
            'Last name' : student.last_name})

    return jsonify(name_list)
@app.route("/student_ages", methods=["GET"])
def student_ages():
    stud_age = Students.query.all()
    age_list = []
    for student in stud_age:
        age_list.append({
            "Name": f"{student.first_name} {student.last_name}",
            "Age": student.age
        })
    return jsonify(age_list)


@app.route("/students/", methods=["GET"])
def studs():
    all_students = Students.query.all()
    print(all_students)
    return jsonify(
        [student_serializer(stud) for stud in all_students]
    )
app.run(debug=True, port=8000)