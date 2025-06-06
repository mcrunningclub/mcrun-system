# Contributing 

## Contributing to the code

### Google Scripts
- Make sure your Google account has edit access to Google Sheets (read access
        to Gmail for payment verification).
- Open the Google Sheet and ensure you are signed in with the correct Google account.
- Authorize the Apps Script project when prompted (first use or after script changes).
- If using scheduled triggers, ensure you have permission to create time-based triggers in Apps Script.
- Open the Apps Script editor (Extensions > Apps Script or script.google.com) to view or modify scripts.

### clasp
- You can also use [Google's `clasp` module](https://github.com/google/clasp) to edit Apps Script files locally.
- After installing node.js and npm, run `npm install -g @google/clasp` (to
        install globally; then you can call clasp directly from anywhere) or
`npm install --save-dev @google/clasp` (to install locally; then you need to
        call clasp using its full path).
- Use `clasp login` to authorize your Google account.
- Push and pull changes to the Apps Script project with `clasp push` and
`clasp pull`.


### Version control
- If directly editing scripts in your browser:
    - Install the [Google Apps Script Github
Assistant](https://chromewebstore.google.com/detail/google-apps-script-github/lfjcgcmkmjjlieihflfhjopckgpelofo?hl=en&pli=1) (Chrome only).
    - Go to your Github account > Settings > Developer Settings > Personal
    access tokens > Fine-grained tokens and generate a new one.
    - Set the resource owner to **mcrunningclub** and repository access to
    **All repositories**.
    - The required permissions are in the Repository permissions section:
        - Commit statuses - read & write
        - Contents - read & write
        - Pull requests - read & write
    - After copying your generated token, log in to the extension using
    "Extension options"; it should require access to your account.
    - Now the repositories should show up in the Apps Script editor toolbar.


## Contributing to the docs (this)
- The docs use **mkdocs** with the Material theme, which you can install using
`pip install mkdocs-material`.
- The source files are in the `docs` folder of the `mcrun-system` repository.
- There is a github action configured to deploy the docs to
[mcrunningclub.github.io/mcrun-system/](https://mcrunningclub.github.io/mcrun-system/) whenever the main branch is
updated
- See the other sections for more information on mkdocs, syntax, and
formatting.

### Example function documentation:

	**sendEmail(recipient, subject, body)**  
	Sends an email message.

	```js
	MailApp.sendEmail(
	  'recipient@example.com',
	  'TPS reports',
	  'Where are the TPS reports?',
	);
	```

	| Name      | Type   | Description                              |
	|-----------|--------|------------------------------------------|
	| recipient | String | The addresses of the recipients          |
	| subject   | String | The subject line                         |
	| body      | String | The body of the email                    |



**sendEmail(recipient, subject, body)**  
Sends an email message.

```js
MailApp.sendEmail(
  'recipient@example.com',
  'TPS reports',
  'Where are the TPS reports?',
);
```

| Name      | Type   | Description                              |
|-----------|--------|------------------------------------------|
| recipient | String | The addresses of the recipients          |
| subject   | String | The subject line                         |
| body      | String | The body of the email                    |
