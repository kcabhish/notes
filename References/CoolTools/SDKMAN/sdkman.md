# Installing and Managing Java Versions with SDKMAN!

Source: https://chatgpt.com/c/6809a42b-653c-8004-8990-b906a1dcb07c

##  1. Install SDKMAN!

Open your terminal and run:

```bash
curl -s "https://get.sdkman.io" | bash
```

Then, follow the instructions to add SDKMAN! to your shell config (.bashrc, .zshrc, etc.) and restart your terminal, or run:

```
source "$HOME/.sdkman/bin/sdkman-init.sh"
```

### For Windows

1. Install WSL (if not already installed)
Open PowerShell as Administrator and run:

```
wsl --install
```
By default, this installs Ubuntu. Restart your system if prompted.

ℹ️ If you already have WSL installed, you can skip this step.

After WSL is set up, open the "Ubuntu" app from the Start menu or Windows Terminal.

```
curl -s "https://get.sdkman.io" | bash
```

Then initialize it:

```
source "$HOME/.sdkman/bin/sdkman-init.sh"
```
To make this permanent, add the following line to your .bashrc or .zshrc:

```
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
```

Then reload:

```
source ~/.bashrc
```

check if sdk is installed

```
sdk version
```