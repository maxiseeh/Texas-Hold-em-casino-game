from flask import Flask, make_response
from prisma import Prisma

#instantiate flask app
app = Flask(__name__)

@app.route("/student", methods=["GET"])
async def get_student():

    db = Prisma()
    await db.connect()

    #Read data => find_first, find_many, find_unique
    student = await db.student.find_first()

    student_dict = student.model_dump()

    return make_response(student_dict, 200)


if __name__ == "__main__":
    app.run(debug=True, port=5000)


