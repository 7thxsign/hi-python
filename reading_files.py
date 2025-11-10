

file_path = "C:/Users/Mithil/Documents/inpt.txt"
try:
    with open(file_path, "r") as file:
        file_content = file.read()
        print(file_content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
finally:
    print('Finally haha')

