#!/bin/bash

development_install () {
	sudo yum -y upgrade
	sudo yum -y groupinstall "Development Tools"
}

create_virtualenv () {
	cd ~
	virtualenv --python=python2.7 pillow
	source ~/pillow/bin/activate
}

pip_install () {
	pip install opencv-python
}

zip_library () {
	zip -r9 ~/OpenCV.zip opencv/lib64/python2.7/dist-packages/*
}

main () {
	development_install
	create_virtualenv
	pip_install
	zip_library
}

main