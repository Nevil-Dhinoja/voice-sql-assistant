from sqlalchemy import create_engine, text
import pandas as pd, random, os

os.makedirs("data", exist_ok=True)
engine = create_engine("sqlite:///data/school.db")

students = pd.DataFrame({
    "id": range(1, 51),
    "name": [f"Student_{i}" for i in range(1, 51)],
    "age": [random.randint(15, 20) for _ in range(50)],
    "class": [random.choice(["10A","10B","11A","11B"])
               for _ in range(50)],
    "marks": [random.randint(40, 100) for _ in range(50)],
    "city": [random.choice(["Surat","Mumbai","Ahmedabad",
              "Baroda","Rajkot"]) for _ in range(50)]
})

subjects = pd.DataFrame({
    "id": range(1, 6),
    "name": ["Maths","Science","English","History","CS"],
    "teacher": ["Mr.Shah","Ms.Patel","Mr.Joshi",
                 "Ms.Desai","Mr.Mehta"]
})

scores = pd.DataFrame({
    "student_id": [random.randint(1,50) for _ in range(200)],
    "subject_id": [random.randint(1,5) for _ in range(200)],
    "score": [random.randint(30,100) for _ in range(200)]
})

students.to_sql("students", engine,
                if_exists="replace", index=False)
subjects.to_sql("subjects", engine,
                if_exists="replace", index=False)
scores.to_sql("scores", engine,
              if_exists="replace", index=False)

print("Database seeded!")
print("Tables: students, subjects, scores")