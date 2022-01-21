from .home import Home
from .account import Account
from .tools import load_users, save_users


class Controller:
    """Controller"""
    def __init__(self, views):
        """Has views, a list of users, HomeController and
        AccountContoller.

        Args:
            - views (ViewsManager) : the ViewsManager
        """
        self.views = views
        self.users = load_users() # comes from tools
        self._home = Home(self.views, self.users)
        self._account = Account(self.views)

    def run(self):
        """Run the program"""
        running = True
        while running:
            user = self._home.home_manager()
            # set the user to the account
            self._account.user = user
            while self._account.user:
                self._account.account_manager()
                save_users(self.users) # comes from tools
