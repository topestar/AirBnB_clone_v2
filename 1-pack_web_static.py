#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        achieve_file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(achieve_file_name))
        return achieve_file_name
    except:
        return None
