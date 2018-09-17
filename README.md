Flask + uwsgi + Nginx + systemd + CentOS
========================================

Just trying to get all these pieces to play nice.

Currently very much a work in progress.

A lot of this was cribbed from Digital Ocean's documentation at https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-centos-7

Instructions
------------

On a CentOS 7 box:

    git clone [this repo]

Edit `hosts` as desired (default is localhost).

	yum install epel-release
	yum install git
	yum install ansible
	ansible-playbook -k -i hosts site.yml
