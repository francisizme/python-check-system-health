#!/usr/bin/env python3
import requests
import socket


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


def check_connectivity():
    response = requests.get('http://www.google.com')
    status_code = response.status_code
    return status_code == 200

