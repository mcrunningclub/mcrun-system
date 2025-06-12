---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRUN Race Code

---

## About

**McRUN Race Code** is a Google Apps Script codebase that manages McGill Students Running Club (McRUN) race registrations, automates payment verification (online/Interac), and maintains robust data flows between Google Sheets and Gmail.  
It streamlines the process of receiving, validating, and formatting race registrations, integrating with email and payment platforms for automation and oversight.

**Purpose:**

- Automate import, formatting, and verification of race registrations.
- Integrate payment confirmation (Zeffy, Stripe, Interac) with Gmail.
- Enable custom menu actions, triggers, and streamlined workflows for admins.


### Files

- **Github Repo:** [mcrace-code](https://github.com/mcrunningclub/mcrace-code)
- **Google Sheets:** [McRUN Race Registrations Sheet](https://docs.google.com/spreadsheets/d/1vgI_bQI21npuBNvb6LcqaC7t3M81GtW0AQ1GfS75xSo/edit?usp=sharing)
- **Apps Script Project:** [McRUN Race Code Apps Script](https://script.google.com/home/projects) _(Accessible via Extensions > Apps Script in the Google Sheet)_

### Key Features

- Custom Google Sheets menu for admin workflows.
- Import and process race registrations (manual or triggered).
- Automated payment verification via Gmail (Zeffy, Stripe, Interac).
- Time-based and event-based triggers for payment and registration processing.
- Advanced formatting (checkboxes, banding, phone/date formats).
- Robust logging and error handling for all critical operations.

### Tools Used

- Google Apps Script (JavaScript)
- Google Sheets
- Gmail API (via Apps Script)
- Apps Script Triggers (time-based, onOpen, onChange)
- Zeffy/Stripe/Interac payment integration via email search


---

## Function Docs

This section is divided by project file (alphabetical order).  
Each file lists its functions and provides a detailed reference for each.

> **Note:** Only a selection of functions may be shown below due to search result limits.  
> [See all code/functions in GitHub](https://github.com/mcrunningclub/mcrace-code/search?q=function)

<br>
<!-- 
    🔴 Formatting.gs
-->

### # <big> Formatting.gs </big>
- [`removeDiacritics(str)`](#removediacriticsstr) → Remove diacritics (accents) from a string
- [`formatSpecificColumns()`](#formatspecificcolumns) → Apply formatting to the registration sheet

---

#### ## <big> removeDiacritics(str) </big>

Removes diacritics (accents) from the given string.

```js
const normalized = removeDiacritics("Élise");
```

| Name | Type   | Description            |
|------|--------|------------------------|
| str  | String | Input string to format |

**Output:** String (normalized, accents removed)

---

#### ## <big> formatSpecificColumns() </big>

Applies formatting to the registration sheet: freezes panes, wraps text, sets alignment, phone/date formats, checkboxes, and banding.

```js
formatSpecificColumns();
```

**Output:** None (side effect: formats the sheet)

**Pitfalls:** Relies on sheet structure and column names.

---

<br>
<!-- 
    🔴 Import.gs
-->

### # <big> Import.gs </big>
- [`appendToImport(reg)`](#appendtoimportreg) → Append a registration to the import sheet
- [`processLastImport()`](#processlastimport) → Process the last imported registration
- [`onChange(e)`](#onchangee) → Event handler for changes in the import sheet

---

#### ## <big> appendToImport(reg) </big>

Appends a registration object (stringified) to the import sheet.

```js
const rowNum = appendToImport(JSON.stringify(regObj));
```

| Name | Type   | Description              |
|------|--------|--------------------------|
| reg  | String | Registration data string |

**Output:** Integer (row number where appended)

**Pitfalls:** Import sheet must be accessible and not locked.

---

#### ## <big> processLastImport() </big>

Processes the last imported registration (parsing, registering, formatting, payment check).

```js
processLastImport();
```

**Output:** None

**Pitfalls:** Throws if the target row is invalid or missing.

---

#### ## <big> onChange(e) </big>

Triggered when a change occurs in the spreadsheet; processes new imports when rows are inserted.

```js
function onChange(e) {
  // Triggered automatically
}
```

| Name | Type   | Description            |
|------|--------|------------------------|
| e    | Object | Sheets event object    |

**Output:** None

**Pitfalls:** Only processes 'INSERT_ROW' changes on the import sheet.

---

<br>
<!-- 
    🔴 Inbox.gs
-->

### # <big> Inbox.gs </big>
- [`getGmailLabel(labelName)`](#getgmaillabellabelname) → Retrieve a Gmail label by name
- [`getGmailSearchString(sender, offset)`](#getgmailsearchstringsender-offset) → Build Gmail search string for sender/date
- [`cleanUpMatchedThread(thread, label)`](#cleanupmatchedthreadthread-label) → Archive, mark read, and label Gmail thread

---

#### ## <big> getGmailLabel(labelName) </big>

Retrieves a Gmail label object by its name.

```js
const label = getGmailLabel("Fee Payments/Online Emails");
```

| Name      | Type   | Description                  |
|-----------|--------|------------------------------|
| labelName | String | Name of the Gmail label      |

**Output:** GmailLabel

**Pitfalls:** Throws if label does not exist.

---

#### ## <big> getGmailSearchString(sender, offset) </big>

Builds a Gmail search string for a sender and minimum date.

```js
const search = getGmailSearchString("zeffy.com", 7 * 24 * 60 * 60 * 1000);
```

| Name   | Type    | Description                                        |
|--------|---------|----------------------------------------------------|
| sender | String  | Sender email address                               |
| offset | Integer | Time offset in ms to calculate minimum search date |

**Output:** String (Gmail search query)

---

#### ## <big> cleanUpMatchedThread(thread, label) </big>

Marks a Gmail thread as read, archives it, and adds the provided label.

```js
cleanUpMatchedThread(thread, label);
```

| Name   | Type          | Description         |
|--------|---------------|---------------------|
| thread | GmailThread   | Gmail thread object |
| label  | GmailLabel    | Gmail label object  |

**Output:** None

**Pitfalls:** Throws if thread or label is invalid.

---

<br>
<!-- 
    🔴 Menu.gs
-->

### # <big> Menu.gs </big>
- [`onOpen()`](#onopen) → Add custom menu to the sheet
- [`helpUI()`](#helpui) → Show help message for menu
- [`confirmAndRunUserChoice(functionName, additionalMsg, funcArg)`](#confirmandrunuserchoicefunctionname-additionalmsg-funcarg) → Confirm and run a user-selected menu function

---

#### ## <big> onOpen() </big>

Creates a custom menu in the sheet UI for McRace admin actions.

```js
onOpen();
```

**Output:** None

---

#### ## <big> helpUI() </big>

Displays a help dialog with info on menu actions and contact.

```js
helpUI();
```

**Output:** None

---

#### ## <big> confirmAndRunUserChoice(functionName, additionalMsg, funcArg) </big>

Displays a confirmation dialog and runs the selected function with an optional argument.

```js
confirmAndRunUserChoice("formatSpecificColumns", "Format sheet?", "");
```

| Name         | Type   | Description                                 |
|--------------|--------|---------------------------------------------|
| functionName | String | Name of function to execute                 |
| additionalMsg| String | Custom message for confirmation (default: "")|
| funcArg      | String | Optional argument to pass (default: "")     |

**Output:** Return value of the executed function

---

<br>
<!-- 
    🔴 Payment.gs
-->

### # <big> Payment.gs </big>
- [`checkPayment(member)`](#checkpaymentmember) → Check payment status for a member
- [`checkOnlinePayment(member)`](#checkonlinepaymentmember) → Check for online payment
- [`checkInteracPayment(member)`](#checkinteracpaymentmember) → Check for Interac payment

---

#### ## <big> checkPayment(member) </big>

Checks payment status for a member depending on their method.

```js
const paid = checkPayment(memberObj);
```

| Name   | Type   | Description                |
|--------|--------|----------------------------|
| member | Object | Member info (name, email, paymentMethod) |

**Output:** Boolean (true if paid)

**Pitfalls:** Method must be known ("CC" or "Interac").

---

#### ## <big> checkOnlinePayment(member) </big>

Checks for online payment (Zeffy, Stripe) via Gmail.

```js
const hasPaid = checkOnlinePayment(memberObj);
```

| Name   | Type   | Description                |
|--------|--------|----------------------------|
| member | Object | Member info                |

**Output:** Boolean (true if payment found)

---

#### ## <big> checkInteracPayment(member) </big>

Checks for Interac payment via Gmail.

```js
const hasPaid = checkInteracPayment(memberObj);
```

| Name   | Type   | Description                |
|--------|--------|----------------------------|
| member | Object | Member info                |

**Output:** Boolean (true if payment found)

---

<br>
<!-- 
    🔴 Registration.gs
-->

### # <big> Registration.gs </big>
- [`getLastRowInReg()`](#getlastrowinreg) → Get last non-empty registration row
- [`onNewRegistration({newRow, member})`](#onnewregistrationnewrow-member) → Process new registration
- [`addNewRegistration(registrationObj)`](#addnewregistrationregistrationobj) → Add new registration to sheet

---

#### ## <big> getLastRowInReg() </big>

Returns the last non-empty row in the registration sheet.

```js
const lastRow = getLastRowInReg();
```

**Output:** Integer

---

#### ## <big> onNewRegistration({newRow, member}) </big>

Processes a new registration (extract payment, verify, format sheet).

```js
onNewRegistration({ newRow: 25, member: memberArr });
```

| Name   | Type   | Description                    |
|--------|--------|--------------------------------|
| newRow | Int    | Row where new data added       |
| member | Array  | Formatted member data          |

**Output:** None

---

#### ## <big> addNewRegistration(registrationObj) </big>

Formats and adds a new registration to the sheet. Returns the new row and member data.

```js
const { newRow, member } = addNewRegistration(regObj);
```

| Name           | Type   | Description            |
|----------------|--------|------------------------|
| registrationObj| Object | Registration data      |

**Output:** Object `{ newRow, member }`

---

<br>
<!-- 
    🔴 Triggers.gs
-->

### # <big> Triggers.gs </big>
- [`createNewFeeTrigger(row, feeDetails)`](#createnewfeetriggerrow-feedetails) → Create a time-based trigger for fee check
- [`runFeeChecker()`](#runfeechecker) → Handler for time-based fee triggers

---

#### ## <big> createNewFeeTrigger(row, feeDetails) </big>

Creates a time-based trigger to check for a member’s fee payment.

```js
createNewFeeTrigger(23, { fullName: "John Doe", email: "john@example.com", paymentMethod: "CC" });
```

| Name        | Type   | Description                |
|-------------|--------|----------------------------|
| row         | Int    | Registration row           |
| feeDetails  | Object | Member's fee/payment info  |

**Output:** None

**Pitfalls:** Only works if Script Properties are writable.

---

#### ## <big> runFeeChecker() </big>

Processes all fee check triggers, verifying payments and sending notifications as needed.

```js
runFeeChecker();
```

**Output:** None

---

<br>
<!-- 
    🔴 Variables.gs
-->

### # <big> Variables.gs </big>
- [`getCurrentUserEmail()`](#getcurrentuseremail) → Returns current user’s email

---

#### ## <big> getCurrentUserEmail() </big>

Returns the email address of the current user executing the script.

```js
const email = getCurrentUserEmail();
```

**Output:** String (email address)

---

## Triggers

### Types of Triggers

- **onOpen:** Adds the custom admin menu for registrations and formatting.
- **onChange:** Processes new imports when rows are inserted (Import.gs).
- **Time-based triggers:**  
  - For fee/payment checking (Triggers.gs), periodically checking if payment has been received for a registration.
  - Configured via `createNewFeeTrigger(row, feeDetails)`.

**Purpose:**  
- Automates admin workflows, payment verification, and keeps the registration sheet up-to-date with minimal manual intervention.

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Failed to retrieve Gmail label." | Label does not exist | Create label in Gmail |
| "Failed to append registration to import sheet." | Sheet locked, invalid, or missing | Check permissions and sheet names |
| "Payment not found" | Email not received or not matched | Wait and retry; check sender and search terms |
| "Error cleaning up Gmail thread." | Gmail API error | Verify permissions, thread existence |
| Formatting is off | Sheet structure changed | Update column indices and formatting logic |

---

## See Also

- [McRUN Attendance](https://github.com/mcrunningclub/mcrun-attendance)
- [McRUN Points System](https://github.com/mcrunningclub/points-system)
- [Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [McRUN Club GitHub](https://github.com/mcrunningclub)

---

_Last updated: 2025-06-12_