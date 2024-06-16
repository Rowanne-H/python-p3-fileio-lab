def write_file(file_name, file_content):
    file_name = str(file_name) 
    with open(file_name + ".txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = str(file_name) 
    with open(file_name + ".txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    file_name = str(file_name) 
    with open(file_name + ".txt", "r") as file:
        return file.read()
