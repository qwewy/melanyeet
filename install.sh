#!/bin/sh
which python >> /dev/null
if [ $? -ne 0 ]; then
	echo "python installation required. Please install a version of python first"
fi

which cowsay >> /dev/null
if [ $? -ne 0 ]; then
	echo "cowsay not installed. Please install cowsay first"
	exit 2
fi

BIN_DIR=~/bin
PACKAGE_DIR=$BIN_DIR/melanyeet_pkg

mkdir -p $PACKAGE_DIR
cp ./blank.cow $PACKAGE_DIR
cp ./melanyeet.cow $PACKAGE_DIR
cp ./melanyeet.py $PACKAGE_DIR
cp ./melanyeet /$BIN_DIR/

chmod +x $BIN_DIR/melanyeet
