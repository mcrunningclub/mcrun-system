---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRace (Registration) Code

---

## About

!!! info "No longer in use"
    This code was only used for the McRace 2025 registrations.

### Files

- **Github Repo:** [mcrace-code](https://github.com/mcrunningclub/mcrace-code)
- **Google Sheets:** [McRace 2025 Registration](https://docs.google.com/spreadsheets/d/1vgI_bQI21npuBNvb6LcqaC7t3M81GtW0AQ1GfS75xSo/edit?usp=sharing)
- **Apps Script Project:** [McRace Code](https://script.google.com/home/projects/15mBLnuaAp63iuLK0lCgcdx0VCU6G9BIFdZnf_atcEoOyK-3zBfMb630U)

### Permissions

| Description | URL |
| --- | --- |
| See, edit, create, and delete all your Google Sheets spreadsheets | https://www.googleapis.com/auth/spreadsheets |
| See your primary Google Account email address | https://www.googleapis.com/auth/userinfo.email |
| Read, compose, send, and permanently delete all your email from Gmail | https://mail.google.com/ |
| Allow this application to run when you are not present | https://www.googleapis.com/auth/script.scriptapp |


---

## Constants

--8<-- "mcrace/registration-variables.md"

---

## Functions

Multiple functions use a custom Object called Member, to represent members' information more easily. This includes the following fields:

 * `Member.firstName` (string) - The member's first name.
 * `Member.lastName` (string) - The member's last name.
 * `Member.email` (string) - The member's email address.
 * `Member.paymentMethod` (string) - The payment method used by the member.

--8<-- "mcrace/registration-registration.md"
--8<-- "mcrace/registration-import.md"
--8<-- "mcrace/registration-formatting.md"
--8<-- "mcrace/registration-payment.md"
--8<-- "mcrace/registration-inbox.md"
--8<-- "mcrace/registration-menu.md"
--8<-- "mcrace/registration-triggers.md"

---

## Triggers

### Time-based

- Created by createNewFeeTrigger() to check if payment has been received

### From spreadsheet

- onOpen() runs when the spreadsheet is open to create the custom admin menu
- onChange() runs when new rows are inserted

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Failed to retrieve Gmail label." | Label does not exist | Create label in Gmail |
| "Failed to append registration to import sheet." | Sheet locked, invalid, or missing | Check permissions and sheet names |
| "Payment not found" | Email not received or not matched | Wait and retry; check sender and search terms |
| "Error cleaning up Gmail thread." | Gmail API error | Verify permissions, thread existence |
| Formatting is off | Sheet structure changed | Update column indices and formatting logic |