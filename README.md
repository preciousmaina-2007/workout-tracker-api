# Workout Tracker API

## Project Description

The Workout Tracker API is a RESTful backend application built with Flask, SQLAlchemy, and Marshmallow. It allows users to manage workouts, exercises, and the relationship between them. The API supports creating, retrieving, and deleting workouts and exercises, as well as assigning exercises to workouts with details such as sets, reps, and duration.

---

## Features

* Create a new workout
* View all workouts
* View a single workout with its exercises
* Delete a workout
* Create a new exercise
* View all exercises
* View a single exercise with its workouts
* Delete an exercise
* Add an exercise to a workout
* Input validation using SQLAlchemy and Marshmallow
* Database migrations using Flask-Migrate

---

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLAlchemy
* Marshmallow
* SQLite

---

## Project Structure

```
server/
│── app.py
│── models.py
│── schemas.py
│── seed.py
│── Pipfile
│── Pipfile.lock
│── migrations/
│── instance/
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd workout-tracker-api/server
```

### Create a virtual environment

```bash
python3 -m venv venv
```

### Activate the virtual environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

or, if using Pipenv:

```bash
pipenv install
pipenv shell
```

---

## Database Setup

Initialize the database:

```bash
flask db init
```

Create a migration:

```bash
flask db migrate -m "Initial migration"
```

Apply the migration:

```bash
flask db upgrade
```

---

## Seed the Database

Run:

```bash
python seed.py
```

You should see:

```
Database seeded successfully!
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The server will run at:

```
http://127.0.0.1:5555
```

---

## API Endpoints

### Workouts

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| GET    | `/workouts`      | Get all workouts |
| GET    | `/workouts/<id>` | Get one workout  |
| POST   | `/workouts`      | Create a workout |
| DELETE | `/workouts/<id>` | Delete a workout |

### Exercises

| Method | Endpoint          | Description        |
| ------ | ----------------- | ------------------ |
| GET    | `/exercises`      | Get all exercises  |
| GET    | `/exercises/<id>` | Get one exercise   |
| POST   | `/exercises`      | Create an exercise |
| DELETE | `/exercises/<id>` | Delete an exercise |

### Workout Exercises

| Method | Endpoint                                                           | Description                  |
| ------ | ------------------------------------------------------------------ | ---------------------------- |
| POST   | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Add an exercise to a workout |

---

## Example Request

### Create an Exercise

**POST** `/exercises`

```json
{
    "name": "Push-ups",
    "category": "Strength",
    "equipment_needed": false
}
```

---

## Example Response

```json
{
    "message": "Exercise created",
    "id": 1
}
```

---

## Validation Rules

### Exercise

* Name must contain at least 3 characters.
* Category must be one of:

  * Strength
  * Cardio
  * Flexibility
  * Mobility
  * Balance

### Workout

* Duration must be greater than 0.
* Date cannot be in the future.

### Workout Exercise

* Sets must be greater than 0.
* Reps must be greater than 0.
* Duration (seconds) must be greater than 0.

---

## Author

**Precious Abi Wanjiku Maina**

