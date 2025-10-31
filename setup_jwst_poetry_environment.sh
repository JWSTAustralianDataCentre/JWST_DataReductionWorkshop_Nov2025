# Setup instructions for using the poetry managed git repo
NAME=jadc-nircam-25
GITUSER=ivolabbe

pip install poetry

git clone https://github.com/$GITUSER/$NAME.git
cd $NAME

# install the packages with dependencies
poetry install --no-root
poetry add ipython

# open the local poetry environment
poetry env use python3.12
poetry run ipython
