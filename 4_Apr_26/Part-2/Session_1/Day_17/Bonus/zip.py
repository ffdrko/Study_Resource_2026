import zipfile


def make_archive(filepaths, destination):
    with zipfile.ZipFile(destination, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=["pg_0.py", "pg_0.py"], destination="File/archive.zip")