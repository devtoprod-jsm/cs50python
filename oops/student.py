def get_student():
    return {"name":input("Name: "),"age":input("Age: ")}

def main():
    student = get_student()
    if student["name"] == "Jai":
        student["age"] = 4

    print(f"{student['name']} is {student['age']} years old")


if __name__ == "__main__":
    main()