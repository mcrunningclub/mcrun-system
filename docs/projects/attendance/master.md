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

### Files

- **Github Repo:** [mcrun-master-attendance](https://github.com/mcrunningclub/mcrun-master-attendance)
- **Google Sheets:** [McRUN Head Run Attendance (Master)](https://docs.google.com/spreadsheets/d/1Abu4txni1zUDI79u5OtIjpffOOoYnea9_vNM9skq0Yg/edit?usp=sharing)
- **Apps Script Project:** [Attendance Code (MASTER)](https://script.google.com/home/projects)

### Permissions

|OAuth Scope|URL|
|---|---|
|Allow this application to run when you are not present | https://www.googleapis.com/auth/script.scriptapp|
|Connect to an external service | https://www.googleapis.com/auth/script.external_request|
|See, edit, create, and delete all your Google Sheets spreadsheets | https://www.googleapis.com/auth/spreadsheets|
|See, edit, create, and delete all of your Google Drive files | https://www.googleapis.com/auth/drive|
|See your primary Google Account email address | https://www.googleapis.com/auth/userinfo.email|

---

## Constants

--8<-- "masterattendance-constants.gs"

---

## Functions

--8<-- "masterattendance-dataformatting.gs"
--8<-- "masterattendance-viewformatting.gs"
--8<-- "masterattendance-transfer.gs"

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

## Usage Examples

### Format Names in Last Row
```javascript
formatNamesInRow_([COLUMN_MAP.ATTENDEES]);
```

### Format Names in Specific Row and Columns
```javascript
formatNamesInRow_([COLUMN_MAP.HEADRUNNERS, COLUMN_MAP.ATTENDEES], 7);
```

### Sort Attendance Sheet by Timestamp
```javascript
sortAttendanceForm();
```

### Export Latest Submission to Semester Sheet
```javascript
transferToSemesterSheet();
```

### Get Last Submission Row
```javascript
const lastRow = getLastSubmission_();
```

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Early exit due to invalid e.changeType" | Triggered on wrong event type | Only EDIT events are processed |
| "thisSource is not defined" | Event object is missing source | Check Apps Script trigger setup |
| "Cannot get property 'getRange' of null" | Wrong sheet ID or sheet deleted | Check values in Variables.gs |
| "No rows transferred" | No new submissions or all rows empty | Verify data is submitted and not empty |
| Formatting is off | Sheet structure has changed | Update column indices and formatting ranges |