#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=filepath
    -i private-key -u user
"""

from os.path import exists
from fabric.api import put, run, env

env.hosts = ['54.160.112.198', '52.91.160.121']


def do_deploy(archive_path):
    """
    copies archive file from local to my webservers
    """

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("sudo mkdir -p /data/web_static/releases/{}".format(file_name))

        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('sudo rm -rf /tmp/{}.tgz'.format(file_name))

        run(('sudo mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('sudo rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run('sudo rm -rf /data/web_static/current')

        run(('sudo ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False
