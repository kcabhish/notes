# Git commit strategy

Source: https://www.conventionalcommits.org/en/v1.0.0/ 

## Commit Message Structure

Top level commit message should be structured as
```
<type>[scope] : <description>
```
examples:
```
feat[JIRA-345] : Sample message for creating top level commit message
fix[JIRA-567] : Sample message for a bug fix
feat[JIRA-999]! : Sample for breaking change
```
### Types

Types define the nature of the PR or commit. Below are lists of types that can be used but not limited to the provided list:
- feat : A new feature
- fix : A bug fix or error correction
- docs : Documentation only changes like editing README.md or code comments etc.
- chore : Routine maintenance tasks, fle reorganization, updating dependencies.
- test : Adding missing tests, updating test suites, or fixing existing test scripts.
- revert : Reverting a previous commit back to prior stable state.
- CI: Updates to CICD pipelines or workflows

### Scope

Use JIRA tickets for the scopes. If there are multiple tickets associated then use the array format and separate them by commas. eg: 
```
feat[JIRA-123, JIRA-456] : Sample with multiple tickets
```

### Description

Short description associated to the changes in the PR or commit.

## Why use commit strategy

- Makes autogenerating the CHANGELOGS easier.
- Easy to understand what types of changes are included with fix, feat, etc tags.
- Having commit/PR message scoped to JIRA tickets makes it easy to connect documents and changes.