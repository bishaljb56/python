import re
class BasePasswordManager:
    def __init__(self, current_password):
        self.old_passwords = [current_password]

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password):
        return password == self.get_password()


class PasswordManager(BasePasswordManager):
    SECURITY_LEVELS = {
        0: r'^[\da-zA-Z]+$',
        1: r'^(?=.*\d)(?=.*[a-zA-Z])[\da-zA-Z]+$',
        2: r'^(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*(),.?":{}|<>])[\da-zA-Z!@#$%^&*(),.?":{}|<>]+$'
    }

    def set_password(self, new_password):
        level = self.get_level(new_password)
        if level < self.get_level(self.get_password()):
            raise ValueError("New password must have a higher security level than the current password.")
        elif level == self.get_level(self.get_password()) and len(new_password) < 6:
            raise ValueError("New password must have a minimum length of 6 characters.")
        else:
            self.old_passwords.append(new_password)

    def get_level(self, password=None):
        if password is None:
            password = self.get_password()
        for level, regex in self.SECURITY_LEVELS.items():
            if re.match(regex, password):
                return level
        return -1

# password = PasswordManager()
# password.set_password("Bishaljb@5")