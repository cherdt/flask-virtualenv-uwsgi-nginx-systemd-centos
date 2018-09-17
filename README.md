Flask + uwsgi + Nginx + systemd + CentOS
========================================

Just trying to get all these pieces to play nice.

Currently very much a work in progress.

A lot of this was cribbed from Digital Ocean's documentation at https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-centos-7

Instructions
------------

On a CentOS 7 box:

	yum install git
	yum install ansible
    git clone [this repo]
    cd flask-virtualenv-uwsgi-nginx-systemd-centos

Edit `hosts` as desired (default is localhost).

	ansible-playbook -k -i hosts site.yml

Assuming no errors occurred, you should now be able to make a request to the app:

    curl http://127.0.0.1/?text=hi