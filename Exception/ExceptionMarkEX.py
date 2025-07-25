def get_marks():
    marks = []
    for i in range(1, 6):
        try:
            mark = int(input(f"Enter marks for Subject {i}: "))
            if mark < 0 or mark > 100:
                raise ValueError(f"Invalid mark: {mark}. Marks must be between 0 and 100.")
            marks.append(mark)
        except ValueError as e:
            print("Error:", e)
            return
    print("\nAll marks entered successfully:", marks)
get_marks()
