---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRUN Membership List

---

## About

**McRUN Membership List** is a Google Apps Script codebase for managing the membership roster of the McGill Students Running Club.

This project automates the collection, verification, and maintenance of member data, integrates with Google Sheets, Gmail, and automates registration, fee-tracking, and communication workflows. It is designed for efficient, accurate, and scalable club membership management.

**Purpose**

- Centralize and automate member registration (including form and manual entry).
- Verify membership fee payments via email (Zeffy, Stripe, Interac).
- Synchronize semester and master sheets, ensuring consistent member history.
- Automate communications and reporting for new members.

### Files

- **Github Repo:** [mcrun-membership-list](https://github.com/mcrunningclub/mcrun-membership-list)
- **Google Sheets:** [McRUN Membership Sheet](https://docs.google.com/spreadsheets/d/1qvoL3mJXCvj3m7Y70sI-FAktCiSWqEmkDxfZWz0lFu4/edit?usp=sharing)
- **Apps Script Project:** [McRUN Membership Apps Script](https://script.google.com/home/projects) _(Accessible via Extensions > Apps Script in the Google Sheet)_

### Key Features

- Automated import from form and manual member registration.
- Fee verification and follow-up via Gmail/Inbox search.
- Custom Google Sheets menu for common admin workflows.
- Synchronization between semester and master membership lists.
- Time-based and event-based triggers for processing new members and payments.
- Communication automation for onboarding new members.
- Robust error handling and logging.

### Tools Used

- Google Apps Script (JavaScript)
- Google Sheets (multiple sheets: Main, Master, Import, Internal Fee Collection, etc.)
- Gmail API via Apps Script
- Apps Script Triggers (onChange, time-based, onOpen)
- Google Drive (waivers, attachments)

---

## Function Docs

This section is divided by project file (alphabetical order).  
Each file lists its functions and provides a detailed reference for each.

> **Note:** Only a selection of functions may be shown below due to search result limits.  
> [See all code/functions in GitHub](https://github.com/mcrunningclub/mcrun-membership-list/search?q=function)

<br>
<!-- 
    🔴 Formatting.gs
-->

### # <big> Formatting.gs </big>
- [`trimWhitespace(lastRow)`](#trimwhitespacelastrow) → Trims whitespace from columns in last row
- [`removeDiacritics(str)`](#removediacriticsstr) → Removes diacritics (accents) from a string
- [`sortMainByName()`](#sortmainbyname) → Sorts MAIN_SHEET by first and last name

---

#### ## <big> trimWhitespace(lastRow) </big>

Trims whitespace from key columns in the last row of `MAIN_SHEET`.

```js
trimWhitespace(23);
```

| Name    | Type    | Description                                |
|---------|---------|--------------------------------------------|
| lastRow | Integer | Row number to trim (default: last row)     |

**Output:** None (in-place formatting)

**Pitfalls:** Assumes columns 3-9 are name/referral fields in MAIN_SHEET.

---

#### ## <big> removeDiacritics(str) </big>

Removes diacritics (accents) from a string, returning ASCII-only output.

```js
const result = removeDiacritics("Élise");
```

| Name | Type   | Description         |
|------|--------|---------------------|
| str  | String | Input string        |

**Output:** String (normalized, accents removed)

---

#### ## <big> sortMainByName() </big>

Sorts the MAIN_SHEET by first name and then last name (columns 3, 4).

```js
sortMainByName();
```

**Output:** None

---

<br>
<!-- 
    🔴 Member Fee.gs
-->

### # <big> Member Fee.gs </big>
- [`getPaymentItem(colIndex)`](#getpaymentitemcolindex) → Gets payment item from "Internal Fee Collection" sheet
- [`getGmailLabel(labelName)`](#getgmaillabellabelname) → Retrieves a Gmail label by name
- [`checkAndSetPaymentRef(row)`](#checkandsetpaymentrefrow) → Verifies fee payment and schedules follow-up if needed

---

#### ## <big> getPaymentItem(colIndex) </big>

Retrieves the fee payment item from a specific cell in "Internal Fee Collection".

```js
const item = getPaymentItem('A3');
```

| Name     | Type   | Description     |
|----------|--------|-----------------|
| colIndex | String | Cell reference  |

**Output:** String (cell value)

---

#### ## <big> getGmailLabel(labelName) </big>

Retrieves a Gmail label object by its name.

```js
const label = getGmailLabel("Fee Payments/Online Emails");
```

| Name      | Type   | Description                  |
|-----------|--------|------------------------------|
| labelName | String | Gmail label name             |

**Output:** GmailLabel

---

#### ## <big> checkAndSetPaymentRef(row) </big>

Verifies whether a member's payment has been found in the inbox or waived; schedules a follow-up if not.

```js
checkAndSetPaymentRef(22);
```

| Name | Type    | Description                     |
|------|---------|---------------------------------|
| row  | Integer | Row in MAIN_SHEET (default: last submission) |

**Output:** None

**Pitfalls:** Creates trigger for follow-up if payment not found.

---

<br>
<!-- 
    🔴 Membership Collected.gs
-->

### # <big> Membership Collected.gs </big>
- [`onFormSubmit(newRow)`](#onformsubmitnewrow) → Handles submission of a new registration form
- [`sendNewMemberCommunications(row)`](#sendnewmembercommunicationsrow) → Sends onboarding comms to new member
- [`getLastSubmissionInMain()`](#getlastsubmissioninmain) → Gets index of last non-empty row

---

#### ## <big> onFormSubmit(newRow) </big>

Processes a new member's registration: trims, formats, verifies payment, adds to master, and sends communications.

```js
onFormSubmit(23);
```

| Name   | Type   | Description                             |
|--------|--------|-----------------------------------------|
| newRow | Int    | Row number (default: last submission)   |

**Output:** None

---

#### ## <big> sendNewMemberCommunications(row) </big>

Packages and transfers new member info to "NewMemberComms" sheet.

```js
sendNewMemberCommunications(23);
```

| Name | Type   | Description        |
|------|--------|--------------------|
| row  | Int    | Row in MAIN_SHEET  |

**Output:** None

---

#### ## <big> getLastSubmissionInMain() </big>

Returns index (1-based) of the last filled row in MAIN_SHEET.

```js
const idx = getLastSubmissionInMain();
```

**Output:** Int (row index)

---

<br>
<!-- 
    🔴 Triggers.gs
-->

### # <big> Triggers.gs </big>
- [`createNewFeeTrigger(row, feeDetails)`](#createnewfeetriggerrow-feedetails) → Creates a time-based trigger for payment follow-up
- [`runFeeChecker()`](#runfeechecker) → Checks all active fee-check triggers and updates sheet

---

#### ## <big> createNewFeeTrigger(row, feeDetails) </big>

Creates a scheduled time-based trigger to check a member's payment status.

```js
createNewFeeTrigger(22, {memberName: "Elise Dubois", email: "elise@ex.com"});
```

| Name      | Type   | Description                        |
|-----------|--------|------------------------------------|
| row       | Int    | Row number in sheet                |
| feeDetails| Object | Details for fee checking           |

**Output:** None

---

#### ## <big> runFeeChecker() </big>

Processes all fee check triggers: finds payments, updates sheet, or schedules further action.

```js
runFeeChecker();
```

**Output:** None

---

<br>
<!-- 
    🔴 Transfer Scripts.gs
-->

### # <big> Transfer Scripts.gs </big>
- [`onChange(e)`](#onchangee) → Handles new registration imports and master updates
- [`transferLastImport()`](#transferlastimport) → Transfers latest Import row to main sheet
- [`transferThisRow(row)`](#transferthisrowrow) → Transfers specific Import row to main sheet

---

#### ## <big> onChange(e) </big>

Event handler for spreadsheet changes: processes new Import entries and master updates.

```js
function onChange(e) {
  // Triggered automatically
}
```

| Name | Type   | Description           |
|------|--------|-----------------------|
| e    | Object | Sheets event object   |

**Output:** None

---

#### ## <big> transferLastImport() </big>

Transfers the last Import sheet row to the main sheet and processes as new member.

```js
transferLastImport();
```

**Output:** None

---

#### ## <big> transferThisRow(row) </big>

Transfers a specific Import row to main sheet and processes as new member.

```js
transferThisRow(14);
```

| Name | Type   | Description           |
|------|--------|-----------------------|
| row  | Int    | Row number in Import  |

**Output:** None

---

<br>
<!-- 
    🔴 User Menu.gs
-->

### # <big> User Menu.gs </big>
- [`onOpen()`](#onopen) → Adds custom menu to Sheet UI
- [`logMenuAttempt(email)`](#logmenuattemptemail) → Logs user attempting to use menu
- [`changeSheetView(sheetName)`](#changesheetviewsheetname) → Activates a specified sheet

---

#### ## <big> onOpen() </big>

Adds the custom McRUN menu to the sheet UI.

```js
onOpen();
```

**Output:** None

---

#### ## <big> logMenuAttempt(email) </big>

Logs an attempt to use the menu by a user.

```js
logMenuAttempt("admin@mcgill.ca");
```

| Name  | Type   | Description                        |
|-------|--------|------------------------------------|
| email | String | User email (default: current user) |

**Output:** None

---

#### ## <big> changeSheetView(sheetName) </big>

Activates the specified sheet in the current spreadsheet.

```js
changeSheetView("Winter 2025");
```

| Name      | Type   | Description       |
|-----------|--------|-------------------|
| sheetName | String | Name of the sheet |

**Output:** None

---

## Triggers

### Types of Triggers

- **onChange:**  
  - Handles new registration import, master updates, and triggers member processing.
- **Time-based triggers:**  
  - For periodic fee/payment checking; created as needed for follow-up.
- **onOpen:**  
  - Adds the custom admin menu for member management.

**Purpose:**  
- Ensures all new members are processed, formatted, verified, and onboarded automatically.
- Follows up on outstanding fee payments.

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Missing required fields" | Registration data not validated | Ensure all required fields are present in import |
| "Unauthorized" | Wrong or missing API key | Ensure correct API key when using web endpoints |
| "Failed to find payment" | Payment email not found | Wait for payment notification or check search terms |
| "Label does not exist" | Gmail label missing | Create Gmail label manually |
| "Script error during onFormSubmit" | Data/range not found or sheet structure changed | Check sheet structure, update code if needed |

---

## See Also

- [mcrun-attendance](https://github.com/mcrunningclub/mcrun-attendance) — Semester attendance system
- [mcrun-master-attendance](https://github.com/mcrunningclub/mcrun-master-attendance) — Head run attendance
- [mcrace-code](https://github.com/mcrunningclub/mcrace-code) — McRUN Race registration management
- [Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [McRUN Club GitHub](https://github.com/mcrunningclub)

---

_Last updated: 2025-06-12_