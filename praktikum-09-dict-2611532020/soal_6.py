schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a: Cari hari dengan jumlah mata kuliah terbanyak
busiest_day = ""
max_courses = -1

for day, courses in schedule.items():
    if len(courses) > max_courses:
        max_courses = len(courses)
        busiest_day = day

print(f"Busiest day: {busiest_day} ({max_courses} courses)")

# 6b: Hitung di berapa hari mata kuliah muncul
course_name = input().strip()
day_count = 0

for courses in schedule.values():
    if course_name in courses:
        day_count += 1

print(f"{course_name}: {day_count} days")