---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRUN Master Attendance

---

## About

The **McRUN Master Attendance** project manages and automates the process of tracking head run attendance for the McGill Students Running Club.

It leverages Google Apps Script with Google Sheets to provide a seamless, automated workflow for importing, formatting, and exporting attendance data between the master sheet and semester sheets.

### Files

- **Github Repo:** [mcrun-master-attendance](https://github.com/mcrunningclub/mcrun-master-attendance)
- **Google Sheets:** [McRUN Master Attendance Sheet](https://docs.google.com/spreadsheets/d/1Abu4txni1zUDI79u5OtIjpffOOoYnea9_vNM9skq0Yg/edit?usp=sharing)
- **Apps Script Project:** [Master Attendance Apps Script](https://script.google.com/home/projects) _(Accessible via Extensions > Apps Script in the Google Sheet)_

### Purpose

- Ensure all head run attendance is reliably recorded, formatted, and transferred.
- Automate data cleaning and formatting for clarity and reporting.
- Integrate with semester attendance sheets for historical and analytics purposes.

### Key Features

- **Automated transfer** of new submissions to semester sheets.
- **Data formatting** for names, timestamps, and event details.
- **Consistent column formatting** (e.g., font, size, alignment, checkboxes).
- **Trigger-based automation** on sheet edits.
- **Error handling/logging** for safe operation.
- **Timezone correctness** for all date operations.

### Tools Used

- Google Apps Script (JavaScript)
- Google Sheets
- Google Sheets Triggers (onChange)
- Custom formatting and transfer functions

---

## Function Docs

This section is divided by project file (alphabetical order).  
Each file lists its functions and provides a detailed reference for each.

> **Note:** Only a selection of functions may be shown below due to search result limits.  
> [See all code/functions in GitHub](https://github.com/mcrunningclub/mcrun-master-attendance/search?q=function)

---

<!-- 
    🔴 Data-Formatting.gs
-->

### # <big> Data-Formatting.gs </big>
- [`getLastSubmission()`](#getlastsubmission) → Gets the last non-empty row in the sheet
- [`formatNamesInRow(targetCols, startRow, numRow)`](#formatnamesinrowtargetcols-startrow-numrow) → Formats and normalizes names in specific columns/rows

---

#### ## <big> getLastSubmission() </big>

Finds the row index of the last non-empty submission (by timestamp) in the master attendance sheet.

```js
const idx = getLastSubmission();
```

| Name | Type | Description |
|------|------|-------------|
| —    | —    | No parameters |

**Output:** Number (1-based index of last non-empty row)

**Pitfalls:** If all rows are empty, may return 0 or error.

---

#### ## <big> formatNamesInRow(targetCols, startRow, numRow) </big>

Formats headrunner or attendee names in the specified columns for a given row or range, normalizing apostrophes and splitting by commas/newline.

```js
formatNamesInRow([2, 7], 7, 1);
```

| Name       | Type          | Description                                      |
|------------|---------------|--------------------------------------------------|
| targetCols | Array<Integer>| Columns to format                                |
| startRow   | Integer       | Row to start formatting (default: last row)      |
| numRow     | Integer       | Number of rows to format (default: 1)            |

**Output:** None (in-place formatting in sheet)

**Pitfalls:** Out-of-range columns/rows may cause errors.

---

<br>
<!-- 
    🔴 Transfer.gs
-->

### # <big> Transfer.gs </big>
- [`onChange(e)`](#onchangee) → Main trigger handler for sheet edits/changes
- [`transferToSemesterSheet(row)`](#transfertosemestersheetrow) → Transfers the latest submission to the semester sheet

---

#### ## <big> onChange(e) </big>

Handles all sheet onChange events. Transfers new submissions to the semester sheet and triggers formatting.

```js
function onChange(e) {
  // Called automatically by trigger
}
```

| Name | Type   | Description                |
|------|--------|----------------------------|
| e    | Object | Sheets event object         |

**Output:** None (side effects: transfers data, runs formatting)

**Pitfalls:** Only processes EDIT events and correct sheet ID; errors logged.

---

#### ## <big> transferToSemesterSheet(row) </big>

Transfers the latest submission (or specified row) to the semester attendance sheet, marking it as exported.

```js
transferToSemesterSheet(5);
```

| Name | Type    | Description                                    |
|------|---------|------------------------------------------------|
| row  | Integer | Row to transfer (default: last submission)     |

**Output:** None

**Pitfalls:** Requires valid sheet IDs and permissions; falls back to direct access if library fails.

---

<br>
<!-- 
    🔴 Variables.gs
-->

### # <big> Variables.gs </big>
- [`getUserTimeZone()`](#getusertimezone) → Gets the script's timezone

---

#### ## <big> getUserTimeZone() </big>

Returns the timezone for the script as a geographical location string.

```js
const tz = getUserTimeZone();
```

| Name | Type   | Description |
|------|--------|-------------|
| —    | —      | No parameters |

**Output:** String (timezone, e.g., 'America/Montreal')

**Pitfalls:** None

---

<br>
<!-- 
    🔴 View-Formatting.gs
-->

### # <big> View-Formatting.gs </big>
- [`sortAttendanceForm()`](#sortattendanceform) → Sorts sheet by timestamp ascending
- [`prettifySheet()`](#prettifysheet) → Calls column formatting function
- [`formatSpecificColumns()`](#formatspecificcolumns) → Applies formatting to key columns

---

#### ## <big> sortAttendanceForm() </big>

Sorts all rows (except the header) by the Timestamp column in ascending order.

```js
sortAttendanceForm();
```

| Name | Type | Description |
|------|------|-------------|
| —    | —    | No parameters |

**Output:** None (sorts in-place)

**Pitfalls:** Assumes Timestamp is in COLUMN_MAP.TIMESTAMP.

---

#### ## <big> prettifySheet() </big>

Applies master formatting to the sheet for better readability.

```js
prettifySheet();
```

**Output:** None

---

#### ## <big> formatSpecificColumns() </big>

Applies font, size, bold, italics, number format, alignment, and checkboxes to specific columns.

```js
formatSpecificColumns();
```

**Output:** None

**Pitfalls:** Hardcoded ranges; will fail if columns/names change.

---

## Triggers

### onChange Trigger

- **Type:** `onChange`
- **Function:** [`onChange(e)`](#onchangee)
- **Purpose:** Runs automatically on any edit/change to the master attendance sheet.
    - Transfers new submissions to the semester sheet.
    - Runs formatting and maintenance functions.
    - Ensures all data is up-to-date and formatted after every change.

### Manual/Custom Triggers

- Functions like [`sortAttendanceForm()`](#sortattendanceform) and [`prettifySheet()`](#prettifysheet) can be run manually from the Apps Script UI for maintenance or troubleshooting.

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Early exit due to invalid e.changeType" | Triggered on wrong event type | Only EDIT events are processed |
| "thisSource is not defined" | Event object is missing source | Check Apps Script trigger setup |
| "Cannot get property 'getRange' of null" | Wrong sheet ID or sheet deleted | Check values in Variables.gs |
| "No rows transferred" | No new submissions or all rows empty | Verify data is submitted and not empty |
| Formatting is off | Sheet structure has changed | Update column indices and formatting ranges |

---

## See Also

- [mcrun-attendance](https://github.com/mcrunningclub/mcrun-attendance) — Semester attendance system
- [mcrun-membership-list](https://github.com/mcrunningclub/mcrun-membership-list) — Membership management
- [Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [McRUN Club GitHub](https://github.com/mcrunningclub)

---

_Last updated: 2025-06-12_