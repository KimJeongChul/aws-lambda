#!/bin/bash

development_install () {
	sudo yum -y upgrade
	sudo yum -y groupinstall "Development Tools"
	sudo yum install -y libjpeg-devel zlib-devel
}

create_virtualenv () {
	virtualenv --python=python2.7 pillow
	source ~/pillow/bin/activate
}

pip_install () {
	pip install pillow
}

zip_library() {
	zip -r9 ~/Pillow.zip pillow/lib64/python2.7/dist-packages/*
}

main () {
	development_install
	create_virtualenv
	pip_install
	zip_library
}

main