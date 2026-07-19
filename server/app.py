from flask import Flask, request, jsonify
from flask_migrate import Migrate
from marshmallow import ValidationError
from datetime import date

from models import db, Exercise, Workout, WorkoutExercise
from schemas import ExerciseSchema, WorkoutSchema, WorkoutExerciseSchema

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

exercise_schema = ExerciseSchema()
workout_schema = WorkoutSchema()
workout_exercise_schema = WorkoutExerciseSchema()



@app.get("/workouts")
def get_workouts():

    workouts = Workout.query.all()

    results = []

    for workout in workouts:
        results.append({
            "id": workout.id,
            "date": workout.date.isoformat(),
            "duration_minutes": workout.duration_minutes,
            "notes": workout.notes
        })

    return jsonify(results), 200



@app.get("/workouts/<int:id>")
def get_workout(id):

    workout = db.session.get(Workout, id)

    if workout is None:
        return jsonify({"error": "Workout not found"}), 404

    exercises = []

    for item in workout.workout_exercises:
        exercises.append({
            "exercise_id": item.exercise.id,
            "name": item.exercise.name,
            "category": item.exercise.category,
            "sets": item.sets,
            "reps": item.reps,
            "duration_seconds": item.duration_seconds
        })

    return jsonify({
        "id": workout.id,
        "date": workout.date.isoformat(),
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes,
        "exercises": exercises
    }), 200



@app.post("/workouts")
def create_workout():

    try:
        data = workout_schema.load(request.get_json())

    except ValidationError as err:
        return jsonify(err.messages), 400

    workout = Workout(
        date=data["date"],
        duration_minutes=data["duration_minutes"],
        notes=data.get("notes")
    )

    db.session.add(workout)
    db.session.commit()

    return jsonify({
        "message": "Workout created",
        "id": workout.id
    }), 201



@app.delete("/workouts/<int:id>")
def delete_workout(id):

    workout = db.session.get(Workout, id)

    if workout is None:
        return jsonify({"error": "Workout not found"}), 404

    db.session.delete(workout)
    db.session.commit()

    return jsonify({
        "message": "Workout deleted"
    }), 200



@app.get("/exercises")
def get_exercises():

    exercises = Exercise.query.all()

    results = []

    for exercise in exercises:
        results.append({
            "id": exercise.id,
            "name": exercise.name,
            "category": exercise.category,
            "equipment_needed": exercise.equipment_needed
        })

    return jsonify(results), 200



@app.get("/exercises/<int:id>")
def get_exercise(id):

    exercise = db.session.get(Exercise, id)

    if exercise is None:
        return jsonify({"error": "Exercise not found"}), 404

    workouts = []

    for item in exercise.workout_exercises:
        workouts.append({
            "workout_id": item.workout.id,
            "date": item.workout.date.isoformat(),
            "sets": item.sets,
            "reps": item.reps,
            "duration_seconds": item.duration_seconds
        })

    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed,
        "workouts": workouts
    }), 200



@app.post("/exercises")
def create_exercise():

    try:
        data = exercise_schema.load(request.get_json())

    except ValidationError as err:
        return jsonify(err.messages), 400

    exercise = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data["equipment_needed"]
    )

    db.session.add(exercise)
    db.session.commit()

    return jsonify({
        "message": "Exercise created",
        "id": exercise.id
    }), 201



@app.delete("/exercises/<int:id>")
def delete_exercise(id):

    exercise = db.session.get(Exercise, id)

    if exercise is None:
        return jsonify({"error": "Exercise not found"}), 404

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({
        "message": "Exercise deleted"
    }), 200



@app.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise_to_workout(workout_id, exercise_id):

    workout = db.session.get(Workout, workout_id)
    exercise = db.session.get(Exercise, exercise_id)

    if workout is None:
        return jsonify({"error": "Workout not found"}), 404

    if exercise is None:
        return jsonify({"error": "Exercise not found"}), 404

    try:
        data = workout_exercise_schema.load({
            "workout_id": workout_id,
            "exercise_id": exercise_id,
            **request.get_json()
        })

    except ValidationError as err:
        return jsonify(err.messages), 400

    workout_exercise = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data.get("reps"),
        sets=data.get("sets"),
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return jsonify({
        "message": "Exercise added to workout"
    }), 201


if __name__ == "__main__":
    app.run(port=5555, debug=True)