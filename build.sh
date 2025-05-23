#!/bin/bash

# Make sure we're in the directory where this script lives.
cd "${0%/*}" 2> /dev/null

shout() { echo "$0: $*" >&2; }  # Just echo an error and the program name
barf() { shout "$*"; exit 111; }
safe() { "$@" || barf "cannot $*"; }

# Install stuff if needed
#TMP_REQ=`mktemp -t req.txt`
#safe ./bin/pip freeze > $TMP_REQ 
#cmp -s $TMP_REQ requirements.txt || safe ./bin/pip install -r requirements.txt
#rm -f $TMP_REQ

# Build the graphics

safe cd samples

for f in *py; do
    echo Generating $f.dot file from $f...
    pyreverse -A -k $f
    # Name convention from older pyreverse version
    test -f classes_No_Name.dot && mv classes_No_Name.dot $f.dot
    # Newer name convention
    test -f classes.dot && mv classes.dot $f.dot
done

dot -? > /dev/null 2>&1 || barf "You don't appear to have the 'dot' command. Install graphviz.  Eg. on OSX with Homebrew, try 'brew install graphviz'."

for f in *dot; do
    echo Generating SVG output from $f...
    dot $f -Tsvg -O
done

cd -

mv samples/*svg static/

# Build the slides.
rm -rf html
mkdir html
safe hovercraft slides.rst html/
# Doesn't seem to include my css?
cp -f static/*css $PWD/html/

echo Output is in $PWD/html/

echo Serving  \(ctrl-C to exit\)
cd $PWD/html/
python -m http.server
