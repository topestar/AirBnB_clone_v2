#!/usr/bin/python3
""" Deletes out-of-date archives using the function do_clean """

import os
from fabric.api import *

env.hosts = ['52.91.160.121', '54.160.112.198']

def do_clean(number=0):
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
