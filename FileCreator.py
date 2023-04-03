from pathlib import Path
from faker import Faker

fake = Faker()
folder_path = Path.home() / 'Downloads'


def filename():
    for n in range(5):
        file_name = fake.file_name()
        open(folder_path / file_name, "w")


if __name__ == '__main__':
    filename()
