cd samples

for f in *py; do
    pyreverse -A -k $f
    mv classes_no_Name.dot $f.dot
done

for f in *dot; do
    dot $f -Tsvg -O
done

cd -

mv samples/*svg static/

hovercraft slides.rst html/
