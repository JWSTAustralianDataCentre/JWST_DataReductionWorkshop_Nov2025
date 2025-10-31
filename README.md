# JWST Python pipeline setup instructions

## Step 1: Clone this repository

`git clone https://github.com/JWSTAustralianDataCentre/JWST_DataReductionWorkshop_Nov2025.git`

## Step 2: run the bash script

`bash setup_jwst_poetry_environment.sh`

This will set up an environment managed by the python dependencies software ‘poetry’, which is similar to conda and venvs . We’ll be using this environment to run the pipeline. To test it has been set up correctly, in the ipython shell that automatically opens, run:

`import jwst`

If it imports, you’re ready to go!

#### Other useful software

-   Download and install the [Astronomer’s proposal Tool](https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt "https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt")

-   Download and install [QFitsView](https://www.mpe.mpg.de/~ott/QFitsView/ "https://www.mpe.mpg.de/~ott/QFitsView/")