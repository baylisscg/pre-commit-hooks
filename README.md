# README

A [pre-commit](http://pre-commit.com/).

## Usage

Add

```yaml
repos:
  - repo: "https://github.com/aurin/pre-commit"
    rev: "master"
    hooks:
      - …
```

to your `.pre-commit-config.yaml`

## Hooks

### google-java-format

Runs Google's [java-format](https://github.com/google/google-java-format/) on Java code.
