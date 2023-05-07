from modules.frontend import update_frontend
from modules.backend import update_backend
from modules.strings import *

option = ''
option2 = ''
def menu():
    global option, option2
    print(title)
    try:
        option = int(input(question))
    except ValueError:
        error()

    if (option == 1):
        repository = "angular-test"
        project = "websitetiims"
    elif (option == 2):
        repository = "adminwebsite"
        project = "adminpanel"
    else:
        error()

    try:
        option2 = int(input(question2))
    except ValueError:
        error()
        
    if (option2 == 1):
        update_frontend(repository, project)
    elif (option2 == 2):
        update_backend(repository, project)
    else:
        error()
        
def error():
    print(error_message)
    menu()
    
if __name__ == "__main__":
    menu()