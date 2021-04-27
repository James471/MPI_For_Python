# MPI For Python
This is a repository for the python implementation of the material covered at the [MPI Workshop(2021) IISERM](https://sites.google.com/view/mpi-workshop) held at IISERM. The lecture notes and the C++ implementation of the code can be found at [MPI Workshop Mateiral](https://sites.google.com/view/mpi-workshop/materials).

## Setup
Welp, I am using wsl and I had already installed MPI on linux so I didn't want to do it on windows again just for the sake of python. I anyways haven't used jupyter and VS Code provides and excellent interface for running code on linux when using wsl while still enjoying most of the power of a GUI. 
You can follow this [link](https://code.visualstudio.com/docs/remote/wsl) to set up VS Code for wsl. Everything boils down to just installing this [extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).

## Running your code
It's really simple if you have installed python, and mpi4py. Just run the following command in the terminal-
```
mpiexec -n numProcs python3 ScriptName.py
```
This is assuming that you have already installed python3 and mpi4py using pip which might require installing pip too.

If you are using communication in your script, it's best to run the script using-
```
mpiexec -n numProcs python3 -m mpi4py ScriptName.py
```