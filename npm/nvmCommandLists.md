# NVM Commands Cheat Sheet

| Commands | Description |
|----------|-------------|
| `nvm ls` | List all Node versions installed locally. |
| `nvm ls-remote` | List all Node versions available for download. |
| `nvm ls-remote --lts` | List only LTS (Long Term Support) versions available. |
| `nvm install <version>` | Install a specific Node version, e.g., `nvm install 18.17.0`. |
| `nvm install <major>` | Install the latest version of a major version, e.g., `nvm install 18`. |
| `nvm install --lts` | Install the latest LTS version of Node.js. |
| `nvm uninstall <version>` | Uninstall a specific Node version. |
| `nvm use <version>` | Switch to a specific Node version in the current shell. |
| `nvm use node` | Use the latest installed Node version. |
| `nvm alias default <version>` | Set a default Node version for new shells. |
| `nvm alias <name> <version>` | Create a custom alias for a Node version. |
| `nvm use <alias>` | Use a Node version via its alias. |
| `nvm alias` | List all aliases defined. |
| `node -v` | Check the current Node version. |
| `npm -v` | Check the current npm version. |
| `nvm run <version> <script>` | Run a Node script with a specific version without switching globally. |
| `nvm current` | Show the currently active Node version. |
| `nvm use` | Switch to the Node version specified in a `.nvmrc` file (if present). |
