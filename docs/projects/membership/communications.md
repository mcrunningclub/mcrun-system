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

### Files

- **Github Repo:** [mcrun-new-member-communications](https://github.com/mcrunningclub/mcrun-new-member-communications)
- **Google Sheets:** [New Member Comms](https://docs.google.com/spreadsheets/d/1PrKth6f81Dx52bB3oPX1t55US-GnNRGve-TN4rU9Wlo/edit?usp=sharing)
- **Apps Script Project:** [New Member Communications](https://script.google.com/home/projects)

### Requirements
- Google Workspace (Gmail, Google Sheets, Google Drive)
- Script must be run from the club's Google account for full functionality

---

## Functions

<!-- ## Main Functions
- **sendWelcomeEmailInRow(row)**: Sends a welcome email to the member in the specified row of the sheet.
- **sendWelcomeEmail_(memberInformation)**: Sends a personalized welcome email to a new member using their information.
- **createPassFile_(passInfo)**: Generates a digital pass for a member and returns a download link.
- **updateAndSendPass(statusObj, isLogged)**: Updates member status, creates a new pass, and sends an updated pass email.
- **logMessage_(message, sheet, row)**: Logs email or pass status to the sheet. -->

--8<-- "communications-memberinfo.md"
--8<-- "communications-memberpass.md"
--8<-- "communications-mailmerge.md"
--8<-- "communications-sendemail.md"


---

## Triggers

### Types of Triggers

- **Manual triggers:**  
  - Most functions are designed to be invoked when a new member is added, or by admin action via Apps Script.
- **Event-based triggers:**  
  - Can be set up to run when new rows are added (e.g., via onChange in a connected membership sheet).
- **Time-based triggers:**  
  - Not present by default, but possible for scheduled reminders or follow-ups if extended.

**Purpose:**  
- Automate sending of welcome emails and pass generation for each new member registration.

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
updateAndSendPass({
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