jupyter nbconvert --to markdown ./examples/*ipynb --output-dir=./examples/
sed -i 's/\.ipynb/\.md/g' examples/*md
