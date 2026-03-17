grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

def get_average_grade(grades: dict) -> float:
    avg_grades = 0
    for grade in grades.values():
        avg_grades += grade
    return round(avg_grades / len(grades.values()), 2)

print(get_average_grade(grades))