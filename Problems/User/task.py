class User():
    users = []
    n_active = 0

    def __init__(self, active, name):
        self.active = active
        self.user_name = name
        User.users.append(name)
        if self.active:
            User.n_active += 1
