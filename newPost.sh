year="$(date +'%Y')"
month="$(date +'%m')"

echo "path: content/posts/$year/$month/$1.md"
echo "Opening a post named $1 for edit."

mkdir -p content/posts/$year/$month
vi content/posts/$year/$month/$1.md
