import pickle
import os

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_users(users):
    """Write the list of users in a file"""
    with open('data', 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(users)

def load_users():
    """Load the list of users from the file"""
    try:
        with open('data', 'rb'):
            pass
    except IOError:
        return []
    else:
        with open('data', 'rb') as file:
            my_unpickler = pickle.Unpickler(file)
            users = my_unpickler.load()
            return users
