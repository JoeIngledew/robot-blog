export PYTHON_VERSION=`python -c 'import sys; version=sys.version_info[:2]; print("{0}.{1}".format(*version))'`
if [ $PYTHON_VERSION = "3.6" ]
then
	pip install pelican markdown ghp-import shovel
else
	echo "You need python v3.6"
fi

echo "Init complete"
