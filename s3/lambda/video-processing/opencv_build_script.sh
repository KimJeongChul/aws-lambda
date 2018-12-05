#!/bin/bash

development_install () {
	sudo yum -y upgrade
	sudo yum -y groupinstall "Development Tools"
}

create_virtualenv () {
	cd ~
	virtualenv --python=python2.7 opencv
	source ~/opencv/bin/activate
}

pip_install () {
	pip install opencv-python
}

zip_library () {
	cd opencv/lib64/python2.7/dist-packages
	zip -r9 ~/OpenCV.zip .
}

main () {
	development_install
	create_virtualenv
	pip_install
	zip_library
}

main