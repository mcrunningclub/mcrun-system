---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRUN Attendance Documentation

---

## About

Welcome to the **McRUN Attendance** codebase documentation. This project is a Google Apps Script-based solution designed to streamline attendance tracking for the McRUN club. It integrates with Google Sheets, Google Forms, and external tools to automate attendance submissions, formatting, and reporting. 

The system also includes features for email notifications, data validation, and integration with the Points Ledger for tracking participation.

<!-- automates and manages attendance for the McGill Students Running Club using Google Apps Script and Google Sheets. -->

### Files

- **Github Repo:** [mcrun-attendance](https://github.com/mcrunningclub/mcrun-attendance)
- **Google Sheets:** [Head Run Attendance - 2024-25](https://docs.google.com/spreadsheets/d/1SnaD9UO4idXXb07X8EakiItOOORw5UuEOg0dX_an3T4/edit?usp=drive_web)
- **Apps Script Project:** [Attendance Code 2024/25](https://script.google.com/u/2/home/projects/1alVHJTwNdIvc_3t2jSNhhy_1kVI-sjryNoJJvZsTe9nDgLtIv9HKfL6c) _(Accessible via Extensions > Apps Script in the Google Sheet)_

### Key Features

- **Attendance Management:** Automates the processing of attendance submissions from Google Forms and the McRUN app.
- **Data Formatting:** Ensures uniform formatting of names, headruns, and other attendance details.
- **Email Notifications:** Sends reminders and attendance copies to headrunners and club executives.
- **Integration with Points Ledger:** Transfers attendance data to a Points Ledger for tracking participation.
- **Custom Menus:** Provides a user-friendly interface in Google Sheets for executing scripts.
- **Triggers and Scheduling:** Automates tasks like checking for missing attendance and updating calendar-based triggers.

> **Note:** This documentation is generated from a code search and may not include every function in the repository.  
> [View all code on GitHub](https://github.com/mcrunningclub/mcrun-attendance/search?q=function)


## Function Docs

This section provides a quick reference to all functions in the McRUN Attendance codebase. Click on a function name to jump to its detailed documentation.


<!-- 
    🔴 FORMATTING.GS 
-->
### # <big> Formatting.gs </big>

- [`addMissingPlatform()`](#addmissingplatform)
- [`toTitleCase()`](#totitlecase) 
- [`cleanSheetData()`](#cleansheetdata)
- [`formatAllHeadRun()`](#formatallheadrun) 
- [`formatAllConfirmations()`](#formatallconfirmations) 
- [`formatConfirmationInRow()`](#formatconfirmationinrowrow)

---

#### ## <big> addMissingPlatform() </big>

Adds 'Google Form' as a platform source for a row.

```js
addMissingPlatform(7);
```

| Name | Type    | Description                  |
|------|---------|------------------------------|
| row  | Integer | Row in attendance sheet (defaults to `ATTENDANCE_SHEET.getLastRow())`)     |

---

#### ## <big> toTitleCase() </big>

Converts a string to title case.

```js
toTitleCase("hello world");
```

| Name        | Type   | Description         |
|-------------|--------|---------------------|
| inputString | String | The string to title |

**Output:** String

---

#### ## <big> cleanSheetData() </big>

Runs all formatting functions for the sheet.

```js
cleanSheetData();
```

---

#### ## <big> formatAllHeadRun() </big>

Formats all headrun entries in the sheet.

```js
formatAllHeadRun();
```

---

#### ## <big> formatAllConfirmations() </big>

Formats all confirmation columns in the sheet.

```js
formatAllConfirmations();
```

---

#### ## <big> formatConfirmationInRow(row) </big>

Formats confirmation as a user-friendly string.

```js
formatConfirmationInRow(10);
```

| Name  | Type    | Description                  |
|------- |---------|------------------------------|
| `row`  | `Integer` | Row in attendance sheet. **Default:** `ATTENDANCE_SHEET.getLastRow()` |



<!-- 
    🔴 HEADRUN-ATTENDANCE.GS 
-->
### # <big> HeadRun-Attendance.gs </big>

- [`onFormSubmission()`](#onformsubmission) 
- [`onFormSubmissionInRow()`](#onformsubmissioninrow) 
- [`onAppSubmission()`](#onappsubmission) 
- [`bulkFormatting()`](#bulkformatting) 
- [`transferAndFormat()`](#transferandformat) 
- [`getLastSubmission()`](#getlastsubmission)

---

#### ## <big> onFormSubmission() </big>

Runs after form submission; sorts, processes, transfers, and formats the new entry.

```js
onFormSubmission();
```

---

#### ## <big> onFormSubmissionInRow() </big>

Executes post-form-submission logic for a specific row.

```js
onFormSubmissionInRow(15);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet (1-index)|

---

#### ## <big> onAppSubmission() </big>

Processes app-based attendance submissions.

```js
onAppSubmission(22);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet (1-index). Defaults to `ATTENDANCE_SHEET.getLastRow()`|

---

#### ## <big> bulkFormatting() </big>

Bulk-formats a row: confirmation and names.

```js
bulkFormatting(7);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet          |

---

#### ## <big> transferAndFormat() </big>

Transfers a row to the Points Ledger, triggers formatting.

```js
transferAndFormat(7);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet          |

---

#### ## <big> getLastSubmission() </big>

Finds the last non-empty row in the attendance sheet.

```js
getLastSubmission();
```

| Name  | Type   | Description                          |
|-------|--------|--------------------------------------|
| sheet | Sheet  | (Optional) Target sheet object. Defaults to `GET_ATTENDANCE_SHEET()`  |

**Output:** Integer (1-indexed row number)



<br>
<!-- 
    🔴 HEADRUN-INFO.GS 
-->
### # <big> Headrun-Info.gs </big>

- [`storeObject(key, obj)`](#storeobject) -> Stores object in GAS document properties.
- [`getAllHeadruns()`](#getallheadruns)
- [`getAllHeadrunners()`](#getallheadrunners)
- [`getWeekday()`](#getweekday) 
- [`getScheduleFromStore()`](#getschedulefromstore) 
- [`getMatchedTimeKey()`](#getmatchedtimekey)

---

#### ## <big> storeObject() </big>

Stores `obj` in the document properties under `key`.

```js
storeObject('headrunners', {...});
```

| Name | Type   | Description            |
|------|--------|------------------------|
| key  | String | Property key           |
| obj  | Object | Object to store        |

---

#### ## <big> getAllHeadruns() </big>

Returns all stored headruns.

```js
getAllHeadruns();
```

---

#### ## <big> getAllHeadrunners() </big>

Returns all stored headrunners.

```js
getAllHeadrunners();
```

---

#### ## <big> getWeekday() </big>

Returns day string for the given index.

```js
getWeekday(2); // returns 'tuesday'
```

| Name         | Type    | Description        |
|--------------|---------|--------------------|
| weekdayIndex | Integer | 0=Sunday, 6=Saturday|

---

#### ## <big> getScheduleFromStore() </big>

Returns run schedule for the specified weekday.

```js
getScheduleFromStore('monday');
```

| Name          | Type    | Description                   |
|---------------|---------|-------------------------------|
| currentWeekday| String|Int | Day name or index         |

---

#### ## <big> getMatchedTimeKey() </big> 

Finds the time key in runSchedule matching submission time ± offset.

```js
getMatchedTimeKey(new Date(), scheduleObj, 2);
```

| Name           | Type    | Description                     |
|----------------|---------|---------------------------------|
| submissionDate | Date    | Date of the submission          |
| runSchedule    | Object  | Schedule object                 |
| offsetHours    | Integer | Offset window in hours (default `2`)|



<!-- 
    🔴 IMPORT.GS 
-->
### # <big> Import.gs </big>

- [`processImportFromApp(importObj)`](#processimportfromappimportobj)
- [`transferLastImport()`](#transferlastimport)
- [`transferThisRow()`](#transferthisrowrow)

---

#### ## <big> processImportFromApp(importObj) </big>

Processes the latest attendance submission imported via the McRUN app.  
Verifies if the import is JSON or multi-column, appends to the import sheet, processes and transfers to semester sheet, and triggers post-import logic.

```js
processImportFromApp('{"timestamp":"2025-05-25T13:00:00Z", ...}');
```

| Name      | Type                  | Description                                |
|-----------|-----------------------|--------------------------------------------|
| importObj | String (JSON)         | JSON string of the attendance submission   |

**Output:** None (side effects: rows added, triggers post-import)  
**Pitfalls:** Import must be a valid JSON string; malformed data will throw.  

---

#### ## <big> transferLastImport() </big>

Transfers the last imported attendance submission (from Import Sheet) to the semester sheet.

```js
transferLastImport();
```

| Name | Type | Description                |
|------|------|----------------------------|
| —    | —    | No parameters              |


**Output:** None (side effects: submission transferred)  
**Pitfalls:** Only for use with valid import rows.

---

#### ## <big> transferThisRow(row) </big>

Helper to transfer a specific row from the import sheet to the semester sheet.

```js
transferThisRow(5);
```

| Name | Type    | Description                                   |
|------|---------|-----------------------------------------------|
| row  | Integer | The row number in the import sheet to process |

**Output:** None.  
**Pitfalls:** Row must contain valid JSON string.



<br>
<!-- 
    🔴 POINTS-LEDGER.GS 
-->
### # <big> Points-Ledger.gs </big>

- [appendMemberEmail(row, registered, unregistered)](#appendmemberemail) -> Appends member emails to attendee names in a row.
- [`transferSubmissionToLedger(row)`](#transfersubmissiontoledger) -> Transfers a submission to the Points Ledger.

--- 

#### ## <big> appendMemberEmail() </big>

Appends member emails to attendee names in a row.

```js
appendMemberEmail(5, registeredArr, unregisteredArr);
```


| Name          | Type        | Description                 |
|---------------|------------ |-----------------------------|
| `row`         | `Integer`   | Row in attendance sheet     |
| `registered`  | `String[][]`| Registered attendees/emails |
| `unregistered`| `String[][]`| Unregistered attendees      |


---

#### ## <big> transferSubmissionToLedger() </big>

Transfers a submission to the Points Ledger.

```js
transferSubmissionToLedger(12);
```

| Name | Type    | Description                                 |
|------|---------|---------------------------------------------|
| row  | Integer | Row in attendance sheet (default: `getLastSubmission()`) |



<br>
<!-- 
    🔴 TRIGGERS.GS 
-->
### # <big> Triggers.gs </big>
- [`updateWeeklyCalendarTriggers()`](#updateweeklycalendartriggers) 
- [`addSingleEventTrigger()`](#addsingleeventtrigger) 
- [`createDailyAttendanceTrigger()`](#createdailyattendancetrigger) 
- [`getStartOfDay()`](#getstartofday)

---

#### ## <big> updateWeeklyCalendarTriggers() </big>

Adds/removes time-based triggers for events, ensures correct calendar is used.

```js
updateWeeklyCalendarTriggers();
```

---

#### ## <big> addSingleEventTrigger() </big>

Adds a trigger for all events today.

```js
addSingleEventTrigger();
```

---

#### ## <big> createDailyAttendanceTrigger() </big>

Creates time-based triggers for all relevant events in the current week.

```js
createDailyAttendanceTrigger();
```

---

#### ## <big> getStartOfDay() </big>

Returns start-of-day for a given date.

```js
getStartOfDay(new Date());
```

| Name | Type | Description    |
|------|------|----------------|
| date | Date | The date object|

**Output:** Date (start of the given day)



<br>
<!-- 
    🔴 UNREGISTERED.GS
-->
### # <big> Unregistered.gs </big>

- [`getAllUnregisteredMembers()`](#getallunregisteredmembers)
- [`getUnregisteredMembersInRow()`](#getunregisteredmembersinrowrow)

---

#### ## <big> getAllUnregisteredMembers() </big>

Runs the unregistered member check for **all** rows in the attendance sheet.

```js
getAllUnregisteredMembers();
```

| Name | Type | Description    |
|------|------|----------------|
| —    | —    | No parameters  |

---

#### ## <big> getUnregisteredMembersInRow(row) </big>

Finds attendees in a specific row who are unregistered, sets in the NOT_FOUND_COL, and appends emails to registered attendees.

```js
getUnregisteredMembersInRow(10);
```

| Name | Type    | Description                                                                       |
|------|---------|-----------------------------------------------------------------------------------|
| row  | Integer | Row in the attendance sheet (1-indexed). Default: `ATTENDANCE_SHEET.getLastRow()` |

**Output:** None; side effects on sheet.


<br>
<!-- 
    🔴 USER-MENU.GS
-->
### # <big> User-Menu.gs </big>

- [`logMenuAttempt()`](#logmenuattempt)
- [`onOpen()`](#onopen)
- [`helpUI()`](#helpui)

---

#### ## <big> logMenuAttempt() </big>

Logs a user's attempt to use the custom menu.

```js
logMenuAttempt("someone@mail.com");
```

| Name  | Type   | Description                                                  |
|-------|--------|--------------------------------------------------------------|
| email | String | Email address of the active user. Defaults to empty string.   |


#### ## <big> onOpen() </big>

Creates the custom menu in the spreadsheet UI.

```js
onOpen();
```


#### ## <big> helpUI() </big>

Displays a help message for the custom menu.

```js
helpUI();
```


<br>

## Triggers

1. **Form Submission**: Set up a trigger for `onFormSubmission` (From form).
2. **App Submission**: Set up a trigger for `onAppSubmission` (From event or manual).
3. **Scheduled Checks**:
   1. Use time-driven triggers (e.g., weekly, daily) for functions like `updateWeeklyCalendarTriggers`.
   2. Calendar event-based triggers for event-driven attendance checks.


## Troubleshooting

### Common Issues

| Issue/Error | Cause | Solution |
|-------------|-------|----------|
| "Exception: No permission" | Not authorized | Ensure proper account and OAuth scopes |
| "Cannot read property 'getRange' of null" | Sheet name or ID is wrong | Double-check constants in Attendance-Variables.gs |
| "Trigger not firing" | Trigger not set up | Manually add the trigger in Apps Script UI |
| "Malformed JSON" | Import data is not valid JSON | Validate data before import |

### FAQ

**Q:** How do I add a new admin?  
**A:** Add their email to `PERM_USER_` in `User-Menu.gs`.

**Q:** How do I change the active semester?  
**A:** Update `ATTENDANCE_SHEET_NAME` and related constants in `Attendance-Variables.gs`.

**Q:** Where are attendance logs stored?  
**A:** In the Points Ledger Google Sheet (see constants).


## See also 

- [Google Apps Script Triggers Documentation](https://developers.google.com/apps-script/guides/triggers)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [Apps Script Properties Service](https://developers.google.com/apps-script/guides/properties)

