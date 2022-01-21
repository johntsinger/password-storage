#!J:\Python\Projet\password\env\Scripts\python

from views.manager import ViewsManager
from controllers.base import Controller

def main():

    # Instanciate the view manager
    views = ViewsManager()
    # Instantiate the controller
    controller = Controller(views)
    # launch the controller
    controller.run()

if __name__ == '__main__':
    main()
