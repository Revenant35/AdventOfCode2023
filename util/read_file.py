
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'File {file_path} not found.')
        exit(1)
    except Exception as e:
        print(e)
        exit(1)