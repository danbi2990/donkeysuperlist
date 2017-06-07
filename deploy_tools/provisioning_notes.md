=======================
provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx-template.conf
* replace SITENAME with, eg, staging.my-domain.com

## systemd service

* put /lib/systemd/system/gunicorn-template.service
* put /lib/systemd/system/gunicorn-template.socket
* put /etc/tmpfile.d/gunicorn-template.conf
* run sudo systemctl enable gunicorn-superlists-staging.socket
* run sudo systemctl start gunicorn-superlists-staging.socket
* service will be active after socket access (curl --unix-socket /tmp/gunicorn-superlists-staging.socket http)

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
