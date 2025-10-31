# Setup instructions for using the poetry managed git repo
cd jwst_pipeline_poetry

# install poetry incase not already installed
pip install poetry

# install the packages with dependencies
poetry install --no-root
poetry add ipython

# open the local poetry environment
poetry env use python3.12
poetry run ipython