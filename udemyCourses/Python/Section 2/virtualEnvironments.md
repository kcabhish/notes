# Virtual Environments

Sometimes you will need to make sure your library installation are in the correct location and using the correct python version. For example, some projects might be running on pythond 2.5 and some might be running on 3.11. In those instances virtual environments comes into play, where developers can switch between the python versions using virtual environments.

# Managing Environments

Instruction and documentation for setting up the environments can be found in this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Creating Environments

1. To create a new environment

`conda create --name my-virtual-environment-name`

2. To create a environment with specific python version

`conda create --name myenv python=3.9`

### Activating and Deactivating Environments

`activate <env-name>` to activate the environment.
`deactivate` to deactivate the environment.

### installing packages

`conda insall <package-name>` to install new packgees.