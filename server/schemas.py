from marshmallow import Schema, fields, validate, validates, ValidationError


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    # These come from the URL, not the request body
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(dump_only=True)

    reps = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1)
    )

    sets = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1)
    )

    duration_seconds = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1)
    )


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=3)
    )

    category = fields.Str(required=True)

    equipment_needed = fields.Bool(required=True)

    workouts = fields.List(
        fields.Nested(
            lambda: WorkoutSchema(
                only=("id", "date", "duration_minutes", "notes")
            )
        ),
        dump_only=True
    )

    @validates("category")
    def validate_category(self, value):
        allowed = [
            "Strength",
            "Cardio",
            "Flexibility",
            "Mobility",
            "Balance"
        ]

        if value not in allowed:
            raise ValidationError(
                f"Category must be one of: {', '.join(allowed)}"
            )


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    notes = fields.Str(
        allow_none=True
    )

    exercises = fields.List(
        fields.Nested(
            lambda: ExerciseSchema(
                only=(
                    "id",
                    "name",
                    "category",
                    "equipment_needed"
                )
            )
        ),
        dump_only=True
    )