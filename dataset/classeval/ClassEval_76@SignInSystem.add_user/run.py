import os
import unittest
class SignInSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username in self.users:
            return False
        else:
            self.users[username] = False
            return True

    def sign_in(self, username):
        if username not in self.users:
            return False
        else:
            self.users[username] = True
            return True

    def check_sign_in(self, username):
        if username not in self.users:
            return False
        else:
            if self.users[username]:
                return True
            else:
                return False

    def all_signed_in(self):
        if all(self.users.values()):
            return True
        else:
            return False

    def all_not_signed_in(self):
        not_signed_in_users = []
        for username, signed_in in self.users.items():
            if not signed_in:
                not_signed_in_users.append(username)
        return not_signed_in_users
class Test(unittest.TestCase):
    def test(self):
            signin_system = SignInSystem()
            result = signin_system.add_user("ccc")
            return result
t=Test()
a=t.test()
with open('/home/changshu/CODEMIND/dataset/classeval/ClassEval_76@SignInSystem.add_user/output.txt', 'w') as wr:
    wr.write(str(a))
        