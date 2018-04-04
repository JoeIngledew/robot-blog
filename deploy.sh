rm -rf output
pelican -s pelicanconf.py
echo "blog.ro-bot.co.uk" >> output/CNAME
ghp-import output
git push origin gh-pages

