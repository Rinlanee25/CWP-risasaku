def average(students):
    total = sum(students.values())
    count = len(students)
    return total / count


class_3B = {
    "Rin": 18,
    "Pang": 15,
    "Opal": 8,
    "Fern": 9
}

class_4B = {
    "Sa": 18,
    "Park": 15,
    "Boat": 8,
    "Guy": 9
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 4B: {average(class_4B)}.")