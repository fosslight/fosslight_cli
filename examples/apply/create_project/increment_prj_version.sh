# Set the version file path
VERSION_FILE="version.tmp"

# Check if the version file exists
if [ -e "$VERSION_FILE" ]; then
    # If the file exists, read the current version and increment it
    PRJ_VERSION=$(<"$VERSION_FILE")
    ((PRJ_VERSION++))
else
    # If the file doesn't exist, set the version to 1
    PRJ_VERSION=1
fi

export PRJ_VERSION=$PRJ_VERSION
echo "$PRJ_VERSION" > "$VERSION_FILE"
