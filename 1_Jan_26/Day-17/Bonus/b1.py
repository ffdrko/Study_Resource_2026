import pathlib
import zipfile

def make_archive(filepath, folder_des):
    folder_destination = pathlib.Path(folder_des)

    with zipfile.ZipFile(folder_destination, 'w') as zf:
        for file in filepath:
            zf.write(file)



if __name__ == "__main__":
    make_archive("todo_list", "zip")