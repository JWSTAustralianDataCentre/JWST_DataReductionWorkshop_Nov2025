# Workshop slides

All the workshop slides are available at this [google drive](https://drive.google.com/drive/folders/18C-CmFfNId1Bk5zP4f_-YnQook7s7vrJ?usp=sharing)

# JWST Python pipeline setup instructions

## Step 1: Clone this repository

`git clone https://github.com/JWSTAustralianDataCentre/JWST_DataReductionWorkshop_Nov2025.git`

## Step 2: run the bash script

`bash setup_jwst_poetry_environment.sh`

This will set up an isolated python environment managed by the dependencies software ‘poetry’, which is similar to conda and venvs (so it won't interfere with your usual python environment). We’ll be using this environment to run the pipeline.

To test it has been set up correctly, in the ipython shell that automatically opens, run:

`import jwst`

If it imports, you’re ready to go!

If you get the following when running the bash script:

`setup_jwst_poetry_environment.sh: line 5: pip: command not found`

You'll need to work where you have a python installation, whether that's in a conda environment or your base system python. If you are working in a conda environment, make sure it has python version 3.12 or above. If it doesn't, make a new conda environemnt using

`conda create -n jwst python=3.12`

And try running the bash script again.

#### Other software we'll use during the workshop

-   Download and install the [Astronomer’s proposal Tool](https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt "https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt")

-   Download and install [QFitsView](https://www.mpe.mpg.de/~ott/QFitsView/ "https://www.mpe.mpg.de/~ott/QFitsView/")