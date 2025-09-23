# Useful npm commands

## Log in to npm
```
// login
npm adduser
// returns your user name if you are logged in
npm whoami
```

## publishing package
```
npm publish --access public
```

## republish packages

npm does not allow overwriting the sam version. If you want to publish updates:

```
npm version patch # increments 1.0.0 -> 1.0.1
npm publish
```