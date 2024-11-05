# GIT CHEATSHEETS

# logs

If you want to check the logs from other branch you can use the following command.
`git log <branch>`

logs by user
`git log --author="akc"`

check by tags
`git log --tags="v*"`

## git configs

To view your configuration file:
`git config --list` or `git config -l`

You can view the global, local or system level configs by adding the following parameter

`git config -l --local`

`git config -l --global`

`git config -l --system`

### find user name and email

`git config user.name`

`git config user.email`

### Resetting users for git

In windows, you will have to manually go and reset the git credentials from `Manage your credentials` if you have used web browser for authentication. Search for `Manage your credentials` in the settings, find the git config and reset the data.

Next time you try to login, it will ask to enter your credentials.

### Setting Up User Configuration

`git config --global user.name "[git username]"`

`git config --global user.email "[valid email]"`




