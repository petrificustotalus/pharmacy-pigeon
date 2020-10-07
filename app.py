from flask import Flask

from database import database
from scrapper.first_scrapper import scrapp_meds

USER_CHOICE = """
Enter:
- 'd' to see what's in database
- 's' to see scrapper in work :)
- 'q' to quit


Your choice: """


def menu():
    database.create_meds_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'd':
            database.print_all_meds()
        if user_input == 's':
            scrapp_meds()
        else:
            print("Your input is invalid! Try once again.")
        user_input = input(USER_CHOICE)


menu()

# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
#
# if __name__ == "__main__":
#     app.run()
