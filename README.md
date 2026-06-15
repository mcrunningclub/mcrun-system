# McRUN System Documentation

The McRun system is used to add new members, keep track of existing ones, updating the points system, and more!

This repository contains the source code for our documentation, which is written using Material for mkdocs.

> [!IMPORTANT]
> **Tag commits as `update-docs` in order to update the deployed pages.** The documentation is deployed using Github Actions, which checks for commits to `main` tagged as `update-docs`.


### USING JSDOC

install locally `npm install --save-dev jsdoc`

clone repository into the same parent folder as this one under default name

run from this folder: `./node_modules/.bin/jsdoc -c jsdoc.conf`

