def read_file_line_by_line():
    try:
        with open("Abc.txt", "r") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("The file 'Abc.txt' was not found.")
    except Exception as e:
        print("An error occurred:", e)
read_file_line_by_line()
