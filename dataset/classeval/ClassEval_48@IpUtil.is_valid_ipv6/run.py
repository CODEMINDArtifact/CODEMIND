import os
import unittest
import socket


class IpUtil:

    @staticmethod
    def is_valid_ipv4(ip_address):
        try:
            socket.inet_pton(socket.AF_INET, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def is_valid_ipv6(ip_address):
        try:
            socket.inet_pton(socket.AF_INET6, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def get_hostname(ip_address):
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            return hostname
        except socket.herror:
            return None
class Test(unittest.TestCase):
    def test(self):
            result = IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
            return result
t=Test()
a=t.test()
with open('/home/changshu/CODEMIND/dataset/classeval/ClassEval_48@IpUtil.is_valid_ipv6/output.txt', 'w') as wr:
    wr.write(str(a))
        