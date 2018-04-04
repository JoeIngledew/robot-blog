rm -rf output
pelican -s pelicanconf.py
ghp-import output
git push origin gh-pages

