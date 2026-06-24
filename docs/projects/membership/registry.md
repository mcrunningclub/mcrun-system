---
authors:
    - andrey
    - mona
date: 2026-06-09
---

# McRUN Membership List

---

## About


This project handles new member registrations and fee payments.


### Files

- **Github Repo:** [mcrun-membership-list](https://github.com/mcrunningclub/mcrun-membership-list)
- **Google Sheets:** [Memberships Collected (main)](https://docs.google.com/spreadsheets/d/1qvoL3mJXCvj3m7Y70sI-FAktCiSWqEmkDxfZWz0lFu4/edit?usp=sharing)
- **Apps Script Project:** [Membership Registry Code](https://script.google.com/home/projects)

### Libraries and Services

- [New Member Communications](./communications.md) library
- Gmail service

### Permission scopes

You must have edit access to the membership spreadsheet (club email).

| Description | URL |
| --- | --- |
| See, edit, create, and delete all your Google Sheets spreadsheets | https://www.googleapis.com/auth/spreadsheets |
| Read, compose, send, and permanently delete all your email from Gmail | https://mail.google.com/|
| Allow this application to run when you are not present | https://www.googleapis.com/auth/script.scriptapp |
| See your primary Google Account email address | https://www.googleapis.com/auth/userinfo.email |
| Send email as you | https://www.googleapis.com/auth/script.send_mail |
| See, edit, create, and delete all of your Google Drive files | https://www.googleapis.com/auth/drive |
| Connect to an external service | https://www.googleapis.com/auth/script.external_request |
| See, edit, create, and delete all your Google Slides presentations | https://www.googleapis.com/auth/presentations |

---

## Constants

--8<-- "registry-constants.md"

---

## Functions

--8<-- "registry-formatting.md"
--8<-- "registry-masterscripts.md"
--8<-- "registry-memberfee.md"
--8<-- "registry-memberships.md"
--8<-- "registry-search.md"
--8<-- "registry-transfer.md"
--8<-- "registry-triggers.md"
--8<-- "registry-usermenu.md"
--8<-- "registry-utils.md"

---

## Triggers

### Time-based

- **checkExistingPaymentInSemester** runs once a day and checks for payments in the semester that need to be copied to master sheet
- **runFeeChecker** runs every 5 minutes, checks for and handles triggers for missing payments
- **setIndexStore** runs once a day and updates the index store for searching emails

### From spreadsheet
- **onChange** runs when changes are made to the spreadsheet and checks for new rows to process
- **onOpen** runs when a user opens the spreadsheet and creates the custom menu

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Missing required fields" | Registration data not validated | Ensure all required fields are present in import |
| "Unauthorized" | Wrong or missing API key | Ensure correct API key when using web endpoints |
| "Failed to find payment" | Payment email not found | Wait for payment notification or check search terms |
| "Label does not exist" | Gmail label missing | Create Gmail label manually |
| "Script error during onFormSubmit" | Data/range not found or sheet structure changed | Check sheet structure, update code if needed |