# McRUN System Documentation

The McRun system is used to add new members, keep track of existing ones, updating the points system, and more!

This repository contains the source code for our documentation, which is written using Material for mkdocs.

---

**USING `GENERATE.PY`**

```terminal
python generate.py <input_file> <output_file>
```

*input_file* should be the path to the Google Apps Script (.js or .gs) to parse,
and *output_file* should be the path to the markdown file where the parsed documentation
will be saved.

Simple parsing of docstring descriptions, parameters, and return values.

Please double check output results! There may be edge cases that the script misses.

---

**USING JSDOC**

install locally `npm install --save-dev jsdoc`

clone repository from git or clone apps script project using clasp (do NOT clone into this folder)

run from this folder: `./node_modules/.bin/jsdoc -c jsdoc.conf [path to folders or files to document]`

html site is saved in jsdoc_site/

tutorials should be put into a folder named jsdoc_tutorials/ in this folder

**USING JSDOC-TO-MARKDOWN**

quality not as good as jsdoc, but it can output markdown

install locally `npm install --save-dev jsdoc-to-markdown`

clone repository from git or clone apps script project using clasp (do NOT clone into this folder)

run from this folder: `./node_modules/.bin/jsdoc2md -c jsdoc.conf [path to folders or files to document] > docs.md`

you can replace *docs.md* with the name or path of the file where you want to save the markdown

**USING DOCUMENTATION.JS**

very unreliable quality and as of June 2026 seems to rely on packages with vulnerabilities, but supports markdown and html output (supposedly)

install locally `npm install --save-dev documentation`

clone repository from git or clone apps script project using clasp (do NOT clone into this folder)

run from this folder: `./node_modules/.bin/documetnation build [path to folders or files to document] -f md > docs.md`

you can replace *docs.md* with the name or path of the file where you want to save the markdown