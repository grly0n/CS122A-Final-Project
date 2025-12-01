# Steps for usage

1. Install dependencies from `uv.lock`, and create and run the Python virtual environment.

2. Import `initial-project.sql` into the MySQL server via command line.

- This creates a user named `test` with a password `password` that has complete access to the `final_project` database. `project.py` uses this user when making connections to the MySQL server.

3. Run `python project.py [data_directory]`, where `data_directory` is a folder containing `.csv` files with the name of each table in the database.

- This operation will re-create the `final_project` database from the imported data, deleting any prior changes.

4. Run other commands in the format `python project.py [command]`.

- Note: `python3` currently does not properly import `mysql-connector-python`. Use `python` instead.
