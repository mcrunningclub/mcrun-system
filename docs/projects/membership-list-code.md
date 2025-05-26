# Membership Registry

## Quick Start

1. **Access the Google Sheet:**
   - [Open the McRUN Membership Google Sheet](https://docs.google.com/spreadsheets/d/1qvoL3mJXCvj3m7Y70sI-FAktCiSWqEmkDxfZWz0lFu4/edit?usp=sharing)
2. **Register a New Member:**
   - Use the [Fillout registration form](https://www.mcrun.fillout.com/register).
3. **Scripts Setup:**
   - Ensure you have edit access to the Google Sheet.
   - Open the Apps Script editor (Extensions > Apps Script) to view or modify scripts.
4. **Run Scripts:**
   - Most scripts run automatically on form submission or via custom menu in the Sheet.
   - Manual triggers can be run from the Apps Script editor if needed.

---

## How-to

New members can register on [Fillout](https://www.mcrun.fillout.com/register).

## Database

Our database uses Google Sheets to store all member registrations and related information:
- Full Name
- Email (used as identifier)

# McRUN Membership List

## Permissions & Setup

- **Required Permissions:**
  - Google Sheets: Edit access
  - Gmail: Read access (for payment verification)
- **Setup Steps:**
  1. Open the Google Sheet and ensure you are signed in with the correct Google account.
  2. Authorize the Apps Script project when prompted (first use or after script changes).
  3. If using scheduled triggers, ensure you have permission to create time-based triggers in Apps Script.




## McRUN Membership List

**Repository:** [mcrunningclub/mcrun-membership-list](https://github.com/mcrunningclub/mcrun-membership-list)  
**Primary Language:** JavaScript (Google Apps Script)  
**Created:** 20 October 2024  
**Last Updated:** 26 May 2025  
**Live Sheet:** [McRUN Membership Google Sheet](https://docs.google.com/spreadsheets/d/1qvoL3mJXCvj3m7Y70sI-FAktCiSWqEmkDxfZWz0lFu4/edit?usp=sharing)  

## Project Summary

This repository contains all Google Apps Script code used to manage the McRUN (McGill Students Running Club) membership list.  
It automates the registration process, membership fee verification, data consolidation, and communication with new members through integration with Google Sheets and Gmail.

**Key Features:**

- Automated registration form processing.
- Fee verification via email scraping and scheduled triggers.
- Consolidation of member data across semesters.
- Custom menu integration for Google Sheets.
- Automated communication with new members.
- Advanced formatting and data-cleaning utilities.
- Custom menu integration for Google Sheets.
- Automated communication with new members.
- Advanced formatting and data-cleaning utilities.


> [View and search all code directly in GitHub](https://github.com/mcrunningclub/mcrun-membership-list/search?q=function)

---

## Function Reference

Below are notable functions grouped by their primary script file.  
Each function includes a description, created/updated dates (if available), and a usage example when documented.

---

### 1. Membership Registration and Processing

#### `onFormSubmit(newRow = getLastSubmissionInMain())`

- **Description:** Processes new registration: trims, formats, generates member ID, verifies payments, sends communications, and updates both `MAIN_SHEET` and `MASTER` sheets.
- **Created:** Oct 18, 2023
- **Example:**
  ```js
  onFormSubmit(); // Handles latest submission
  ```

#### `sendNewMemberCommunications(row)`
- **Description:** Packages and transfers new member info to a separate comms sheet.
- **Created:** Oct 18, 2023

#### `getLastSubmissionInMain()`
- **Description:** Returns the 1-indexed row of the last non-empty submission in `MAIN_SHEET`.
- **Created:** Sep 1, 2024  
- **Updated:** Dec 18, 2024

---

### 2. Master Sheet Operations

#### `createMaster()`
- **Description:** Consolidates member data from semester sheets into the `MASTER` sheet.
- **Created:** Oct 23, 2024

#### `addLastSubmissionToMaster(lastRow = getLastSubmissionInMain())`
- **Description:** Processes the last row of `MAIN_SHEET` and adds it to `MASTER`, then sorts by email.
- **Created:** Oct 23, 2024

#### `addPaidSemesterToHistory(memberRow, semesterSheetName)`
- **Description:** Appends the semester code to a member's payment history.
- **Created & Updated:** Dec 17, 2024

---

### 3. Fee Payment and Triggers

#### `checkAndSetPaymentRef(row = getLastSubmissionInMain())`
- **Description:** Verifies if a member has paid using email notifications; sets up a scheduled trigger if payment is not found.
- **Created:** Mar 16, 2025  
- **Updated:** May 20, 2025

#### `createNewFeeTrigger_(row, feeDetails)`
- **Description:** Creates a new time-based trigger to check payment status repeatedly.
- **Created & Updated:** May 20, 2025

#### `runFeeChecker()`
- **Description:** Triggered function to check for payment confirmation and clean up if found.
- **Created:** May 20, 2025  
- **Updated:** May 26, 2025

---

### 4. Sheet Formatting and Utilities

#### `trimWhitespace_(lastRow = MAIN_SHEET.getLastRow())`
- **Description:** Trims whitespace from key columns in the given row of `MAIN_SHEET`.
- **Created:** Oct 17, 2023  
- **Updated:** Feb 5, 2025

#### `removeDiacritics(str)`
- **Description:** Removes diacritical marks from a string (e.g., accents).
- **Created:** Mar 5, 2025  
- **Updated:** Mar 15, 2025
- **Example:**
  ```js
  removeDiacritics("José"); // Outputs "Jose"
  ```

#### `sortMainByName()`
- **Description:** Sorts `MAIN_SHEET` by first then last name.
- **Created:** Oct 1, 2023  
- **Updated:** Jan 11, 2025

---

### 5. Transfer and Import Scripts

#### `onChange(e)`
- **Description:** Handles changes in the spreadsheet (row insertions etc.) to automate imports and formatting.
- **No explicit dates.**

#### `transferLastImport()`
- **Description:** Transfers the latest row from the import sheet.
- **No explicit dates.**

#### `transferThisRow_(row)`
- **Description:** Helper to transfer a specific row from import to main.
- **No explicit dates.**

---

### 6. Menu and UI Integration

#### `onOpen()`
- **Description:** Adds a custom menu to Google Sheets for quick access to scripts.
- **Created:** Nov 21, 2024  
- **Updated:** Mar 1, 2025

#### `logMenuAttempt_(email = "")`
- **Description:** Logs attempts to use the custom menu.
- **Created:** Nov 21, 2024  
- **Updated:** Nov 22, 2024

#### `changeSheetView_(sheetName)`
- **Description:** Activates a specific sheet in the spreadsheet.
- **Created & Updated:** Nov 21, 2024

---

### 7. Example: Fee Verification and Automation

```js
// Check and set payment for the latest member
checkAndSetPaymentRef();

// Schedule a trigger to recheck payment for a new member
createNewFeeTrigger_(row, feeDetails);

// Run the periodic fee checker (typically not called directly)
runFeeChecker();
```

---

## Constants and Sheet Structure

The repo defines many constants for column indices, sheet names, and labels (see `Semester Variables.gs`).

---

## Advanced Usage Notes

- **Custom menus** are added through `onOpen`.
- **Scheduled triggers** are created for fee verifications using Google Apps Script Triggers.
- **Email notifications** for payment are parsed and verified via GmailApp.
- **All scripts** are intended for use within the Google Sheets UI.

---

## Viewing and Searching All Functions

This documentation lists only a subset of all available functions due to search result limits.  
For a full list and up-to-date information, see the [GitHub code search for 'function'](https://github.com/mcrunningclub/mcrun-membership-list/search?q=function).

---

## Troubleshooting & FAQ

**Q: Scripts aren’t running or menu is missing?**
- Try reloading the Google Sheet.
- Make sure you have authorized the Apps Script project (check for permission prompts).

**Q: Payment verification isn’t working?**
- Ensure the Google account has access to the relevant Gmail inbox.
- Check that triggers are set up correctly in Apps Script (Edit > Current project's triggers).

**Q: How do I manually run a script?**
- Open the Apps Script editor, select the function, and click the Run button.

For more help, see the [GitHub Issues page](https://github.com/mcrunningclub/mcrun-membership-list/issues).

---

## Contributing

For bug reports or feature requests, please use the [GitHub Issues page](https://github.com/mcrunningclub/mcrun-membership-list/issues).

---

---

## Changelog

- **2025-05-26:** Added Quick Start, Permissions & Setup, Troubleshooting, and Changelog sections to documentation.

_Last generated: 26 May 2025_