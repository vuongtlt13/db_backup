import os.path
from enum import Enum
from typing import Tuple


class DriverType(str, Enum):
    MYSQL = "mysql"
    POSTGRES = "postgres"

    @classmethod
    def get_file_names_by_type(cls, driver_type: str) -> Tuple[str, str]:
        if driver_type == DriverType.MYSQL:
            return "mysqldump", "mysql"

        raise ValueError(f"Driver `{driver_type}` was not supported!")


class Driver:
    def __init__(self, name: str, version: str, file_path: str):
        self.name = name
        self.version = version
        self.folder_path = file_path

        backup_file, restore_file = DriverType.get_file_names_by_type(self.name)
        self.backup_file_path = os.path.join(file_path, backup_file)
        self.restore_file_path = os.path.join(file_path, restore_file)

    def __str__(self):
        return f"{self.name}:{self.version} at folder {self.folder_path}"

    def is_valid_driver(self, driver_str: str):
        return driver_str == f"{self.name}:{self.version}"
