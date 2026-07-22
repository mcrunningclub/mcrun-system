# Contributing to the docs

We use mkdocs (more specifically, Material for mkdocs) to write our documentation.
For more documentation visit [mkdocs.org](https://www.mkdocs.org) and [the Material for mkdocs documentation](https://squidfunk.github.io/mkdocs-material).

The source files are in the `docs` folder of the `mcrun-system` repository.

## Installation

```shell
pip install mkdocs-material
```

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Deployment

There is a github action configured to deploy the docs to
[mcrunningclub.github.io/mcrun-system/](https://mcrunningclub.github.io/mcrun-system/) whenever the main branch is
updated

## Example documentation

````markdown
#### sendEmail(recipient, subject, body)

Sends an email message.

Parameters:

- `recipient` (String) - The addresses of the recipients
- `subject` (String) - The subject line
- `body` (String) - The body of the email

Example:

```js
MailApp.sendEmail(
	'recipient@example.com',
	'TPS reports',
	'Where are the TPS reports?',
);
```
````

#### sendEmail(recipient, subject, body)

Sends an email message.

Parameters:

- `recipient` (String) - The addresses of the recipients
- `subject` (String) - The subject line
- `body` (String) - The body of the email

Example:

```js
MailApp.sendEmail(
  'recipient@example.com',
  'TPS reports',
  'Where are the TPS reports?',
);
```