rm -rf output
pelican -s pelicanconf.py
echo "blog.ro-bot.co.uk" >> output/CNAME
cp -r images output
ghp-import output
git push origin gh-pages

