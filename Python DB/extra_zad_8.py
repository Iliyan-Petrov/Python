import shutil
import os
from datetime import time


def create_sqlite_backup(database_file, backup_directory):

	if not os.path.isfile(database_file): print("Error: The database file does not exist.")
    	return

	if not os.path.isdir(backup_directory): print("Error: The backup directory does not exist.")
    	return

	database_filename = os.path.basename(database_file)

	backup_filename = f"{database_filename.split('.')[0]}_{int(time.time())}.db"


	backup_file = os.path.join(backup_directory, backup_filename)

	try:
    	shutil.copy(database_file, backup_file)
    	print(f"Backup created successfully at {backup_file}")
	except Exception as e:
    	print(f"Error creating backup: {e}")

database_file = "example.db"
backup_directory = "backups"

create_sqlite_backup(database_file, backup_directory)
