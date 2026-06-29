---
authors:
    - andrey
    - rama
    - mona
date: 2025-06-11

---

# McRUN New Member Communications

---

## About

This project handles creating passes, sending welcome emails to new members, 
and sending passes to members.

### Files

- **Github Repo:** [mcrun-new-member-communications](https://github.com/mcrunningclub/mcrun-new-member-communications)
- **Google Sheets:** [New Member Comms](https://docs.google.com/spreadsheets/d/1PrKth6f81Dx52bB3oPX1t55US-GnNRGve-TN4rU9Wlo/edit?usp=sharing)
- **Apps Script Project:** [New Member Communications](https://script.google.com/home/projects)
  - Contains .html files with email templates

### Permissions

Scripts must be run from the club account.

| OAuth scope | URL |
| --- | --- |
| Send email as you	| https://www.googleapis.com/auth/script.send_mail |
| See, edit, create, and delete all of your Google Drive files	| https://www.googleapis.com/auth/drive |
| Connect to an external service	| https://www.googleapis.com/auth/script.external_request |
| Read, compose, send, and permanently delete all your email from Gmail	| https://mail.google.com/ |
| See your primary Google Account email address	| https://www.googleapis.com/auth/userinfo.email |
| See, edit, create, and delete all your Google Sheets spreadsheets	| https://www.googleapis.com/auth/spreadsheets |
| See, edit, create, and delete all your Google Slides presentations	| https://www.googleapis.com/auth/presentations |

---

## Constants

--8<-- "communications-constants.md"

---

## Functions

--8<-- "communications-emailtemplate.md"
--8<-- "communications-memberinfo.md"
--8<-- "communications-memberpass.md"
--8<-- "communications-sendemail.md"
--8<-- "communications-utils.md"

---

## Triggers

None (?)

---

## Example Usage

### Send Welcome Email to New Member
```javascript
// Send welcome email to the last row (newest member)
sendWelcomeEmailInRow();
```

### Generate and Send Updated Pass
```javascript
// Update member status and send new pass for row 5
updateAndSendPass_({
  email: 'member@email.com',
  feeStatus: 'Paid',
  // ...other member info
});
```

### Create a Digital Pass for a Member
```javascript
const passUrl = createPassFile_({
  firstName: 'Jane',
  lastName: 'Doe',
  memberId: '12345',
  // ...other info
});
Logger.log(passUrl);
```

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Wrong email. Please try using the club's account" | Script not run as mcrunningclub@ssmu.ca | Use the club account to send emails |
| "Expected X for newMemberValues.length..." | Sheet column mismatch | Ensure header and data columns match |
| "Blob not found" | Script property missing or not cached | Run cacheBlobToStore or check Drive file access |
| "Template/Drive ID not found" | File/folder IDs incorrect | Double-check and update IDs in the code |
| Email not received | Spam filter, wrong address | Check recipient address and Gmail spam folder |