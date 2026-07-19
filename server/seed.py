from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():

    
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()

    
    exercise1 = Exercise(
        name="Push-ups",
        category="Strength",
        equipment_needed=False
    )

    exercise2 = Exercise(
        name="Squats",
        category="Strength",
        equipment_needed=False
    )

    exercise3 = Exercise(
        name="Running",
        category="Cardio",
        equipment_needed=False
    )

    db.session.add_all([
        exercise1,
        exercise2,
        exercise3
    ])

    db.session.commit()

    
    workout1 = Workout(
        date=date(2026, 7, 17),
        duration_minutes=30,
        notes="Upper body workout"
    )

    workout2 = Workout(
        date=date(2026, 7, 18),
        duration_minutes=45,
        notes="Morning cardio"
    )

    db.session.add_all([
        workout1,
        workout2
    ])

    db.session.commit()

    
    workout_exercise1 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=exercise1.id,
        reps=15,
        sets=3
    )

    workout_exercise2 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=exercise2.id,
        reps=20,
        sets=4
    )

    workout_exercise3 = WorkoutExercise(
        workout_id=workout2.id,
        exercise_id=exercise3.id,
        duration_seconds=1800
    )

    db.session.add_all([
        workout_exercise1,
        workout_exercise2,
        workout_exercise3
    ])

    db.session.commit()

    print("Database seeded successfully!")