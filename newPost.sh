year="$(date +'%Y')"
month="$(date +'%m')"


echo "path: content/posts/$year/$month/$1.md"
echo "Opening a post named $1 for edit."

file=content/posts/$year/$month/$1.md
echo "creating $file"

mkdir -p content/posts/$year/$month
touch $file

echo "Title:" >> $file
echo "Date: $(date +'%Y-%m-%d %H:%M')" >> $file
echo "Slug: $1" >> $file
echo "Author: Ro Avery" >> $file
echo "Category:" >> $file
echo "Tags:" >> $file

vi $file
