
authors:
    - andrey
date: 2025-05-26


# McRUN Attendance Documentation

## About

Welcome to the **McRUN Attendance** codebase documentation. This project automates and manages attendance for the McGill Students Running Club using Google Apps Script and Google Sheets.

## Files

### Github repo
[mcrun-attendance](https://github.com/mcrunningclub/mcrun-attendance)

### Google Sheets
[Head Run Attendance -
2024-25](https://docs.google.com/spreadsheets/d/1SnaD9UO4idXXb07X8EakiItOOORw5UuEOg0dX_an3T4/edit?usp=drive_web)

### Apps Script project
[Attendance Code
2024/25](https://script.google.com/u/2/home/projects/1alVHJTwNdIvc_3t2jSNhhy_1kVI-sjryNoJJvZsTe9nDgLtIv9HKfL6c)

**Required Permissions:**

- **Sheets API**: Read and write access to the Attendance Sheet and Points Ledger.
- **Gmail API**: (If using email features) Send and read email.
- **Calendar API**: For time-based and event-based triggers.
- **Properties Service**: Store persistent data (e.g., headrunners, headruns).

**Apps Script Scopes:**

Be sure to grant the following scopes when authorizing for the first time:

- `https://www.googleapis.com/auth/spreadsheets`
- `https://www.googleapis.com/auth/script.external_request`
- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/gmail.send` (if emailing)
- `https://www.googleapis.com/auth/script.properties`
- `https://www.googleapis.com/auth/userinfo.email`


## Documentation

### Functions

All functions are grouped by file.  
Functions ending in `_` are "hidden" but still documented and callable.

- **Import.gs**: 
[`processImportFromApp(importObj)`](#processimportfromappimportobj)
[`transferLastImport()`](#transferlastimport)
[`transferThisRow()`](#transferthisrowrow)

- **Unregistered.gs**: 
[`getAllUnregisteredMembers()`](#getallunregisteredmembers)
[`getUnregisteredMembersInRow()`](#getunregisteredmembersinrowrow)

- **User-Menu.gs**: 
[`logMenuAttempt()`](#logmenuattempt)
[`onOpen()`](#onopen) [`helpUI()`](#helpui)

- **Triggers.gs**: 
[`updateWeeklyCalendarTriggers()`](#updateweeklycalendartriggers) 
[`addSingleEventTrigger()`](#addsingleeventtrigger) 
[`createDailyAttendanceTrigger()`](#createdailyattendancetrigger) 
[`getStartOfDay()`](#getstartofday)

- **HeadRun-Attendance.gs**: 
[`onFormSubmission()`](#onformsubmission) 
[`onFormSubmissionInRow()`](#onformsubmissioninrow) 
[`onAppSubmission()`](#onappsubmission) 
[`bulkFormatting()`](#bulkformatting) 
[`transferAndFormat()`](#transferandformat) 
[`getLastSubmission()`](#getlastsubmission)

- **Points-Ledger.gs**: 
[`appendMemberEmail()`](#appendmemberemail) 
[`transferSubmissionToLedger()`](#transfersubmissiontoledger)

- **Formatting.gs**: 
[`addMissingPlatform()`](#addmissingplatform) 
[`toTitleCase()`](#totitlecase) 
[`cleanSheetData()`](#cleansheetdata) 
[`formatAllHeadRun()`](#formatallheadrun) 
[`formatAllConfirmations()`](#formatallconfirmations) 
[`formatConfirmationInRow()`](#formatconfirmationinrow)

- **HeadRun-Info.gs**:
[`storeObject()`](#storeobject)
[`getAllHeadruns()`](#getallheadruns)
[`getAllHeadrunners()`](#getallheadrunners)
[`getWeekday()`](#getweekday)
[`getScheduleFromStore()`](#getschedulefromstore)
[`getMatchedTimeKey()`](#getmatchedtimekey)



### Import.gs

#### processImportFromApp(importObj)

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
**@author:** Andrey Gonzalez  
**@date:** Feb 10, 2025  
**@update:** Apr 7, 2025


#### transferLastImport()

Transfers the last imported attendance submission (from Import Sheet) to the semester sheet.

```js
transferLastImport();
```

| Name | Type | Description                |
|------|------|----------------------------|
| —    | —    | No parameters              |

**Output:** None (side effects: submission transferred)  
**Pitfalls:** Only for use with valid import rows.


#### transferThisRow(row)

Helper to transfer a specific row from the import sheet to the semester sheet.

```js
transferThisRow(5);
```

| Name | Type    | Description                                   |
|------|---------|-----------------------------------------------|
| row  | Integer | The row number in the import sheet to process |

**Output:** None.  
**Pitfalls:** Row must contain valid JSON string.


### Unregistered.gs

#### getAllUnregisteredMembers()

Runs the unregistered member check for **all** rows in the attendance sheet.

```js
getAllUnregisteredMembers();
```

| Name | Type | Description    |
|------|------|----------------|
| —    | —    | No parameters  |


#### getUnregisteredMembersInRow(row)

Finds attendees in a specific row who are unregistered, sets in the NOT_FOUND_COL, and appends emails to registered attendees.

```js
getUnregisteredMembersInRow(10);
```

| Name | Type    | Description                                                                       |
|------|---------|-----------------------------------------------------------------------------------|
| row  | Integer | Row in the attendance sheet (1-indexed). Default: `ATTENDANCE_SHEET.getLastRow()` |

**Output:** None; side effects on sheet.


### User-Menu.gs

#### logMenuAttempt()

Logs a user's attempt to use the custom menu.

```js
logMenuAttempt("someone@mail.com");
```

| Name  | Type   | Description                                                  |
|-------|--------|--------------------------------------------------------------|
| email | String | Email address of the active user. Defaults to empty string.   |


#### onOpen()

Creates the custom menu in the spreadsheet UI.

```js
onOpen();
```

_No parameters. Triggered by opening the sheet._


#### helpUI()

Displays a help message for the custom menu.

```js
helpUI();
```


### Triggers.gs

#### updateWeeklyCalendarTriggers()

Adds/removes time-based triggers for events, ensures correct calendar is used.

```js
updateWeeklyCalendarTriggers();
```


#### addSingleEventTrigger()

Adds a trigger for all events today.

```js
addSingleEventTrigger();
```


#### createDailyAttendanceTrigger()

Creates time-based triggers for all relevant events in the current week.

```js
createDailyAttendanceTrigger();
```


#### getStartOfDay()

Returns start-of-day for a given date.

```js
getStartOfDay(new Date());
```
| Name | Type | Description    |
|------|------|----------------|
| date | Date | The date object|

**Output:** Date (start of the given day)


### HeadRun-Attendance.gs

#### onFormSubmission()

Runs after form submission; sorts, processes, transfers, and formats the new entry.

```js
onFormSubmission();
```


#### onFormSubmissionInRow()

Executes post-form-submission logic for a specific row.

```js
onFormSubmissionInRow(15);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet (1-index)|


#### onAppSubmission()

Processes app-based attendance submissions.

```js
onAppSubmission(22);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet (1-index). Defaults to `ATTENDANCE_SHEET.getLastRow()`|


#### bulkFormatting()

Bulk-formats a row: confirmation and names.

```js
bulkFormatting(7);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet          |


#### transferAndFormat()

Transfers a row to the Points Ledger, triggers formatting.

```js
transferAndFormat(7);
```

| Name | Type    | Description                      |
|------|---------|----------------------------------|
| row  | Integer | Row in attendance sheet          |


#### getLastSubmission()

Finds the last non-empty row in the attendance sheet.

```js
getLastSubmission();
```

| Name  | Type   | Description                          |
|-------|--------|--------------------------------------|
| sheet | Sheet  | (Optional) Target sheet object. Defaults to `GET_ATTENDANCE_SHEET()`  |

**Output:** Integer (1-indexed row number)


### Points-Ledger.gs

#### appendMemberEmail()

Appends member emails to attendee names in a row.

```js
appendMemberEmail(5, registeredArr, unregisteredArr);
```

| Name        | Type      | Description                 |
|-------------|-----------|-----------------------------|
| row         | Integer   | Row in attendance sheet     |
| registered  | String[][]| Registered attendees/emails |
| unregistered| String[][]| Unregistered attendees      |


#### transferSubmissionToLedger()

Transfers a submission to the Points Ledger.

```js
transferSubmissionToLedger(12);
```

| Name | Type    | Description                                 |
|------|---------|---------------------------------------------|
| row  | Integer | Row in attendance sheet (default: `getLastSubmission()`) |


### Formatting.gs

#### addMissingPlatform()

Adds 'Google Form' as a platform source for a row.

```js
addMissingPlatform(7);
```

| Name | Type    | Description                  |
|------|---------|------------------------------|
| row  | Integer | Row in attendance sheet (defaults to `ATTENDANCE_SHEET.getLastRow())`)     |


#### toTitleCase()

Converts a string to title case.

```js
toTitleCase("hello world");
```

| Name        | Type   | Description         |
|-------------|--------|---------------------|
| inputString | String | The string to title |

**Output:** String


#### cleanSheetData()

Runs all formatting functions for the sheet.

```js
cleanSheetData();
```


#### formatAllHeadRun()

Formats all headrun entries in the sheet.

```js
formatAllHeadRun();
```


#### formatAllConfirmations()

Formats all confirmation columns in the sheet.

```js
formatAllConfirmations();
```


#### formatConfirmationInRow()

Formats confirmation as a user-friendly string.

```js
formatConfirmationInRow(10);
```

| Name | Type    | Description                  |
|------|---------|------------------------------|
| row  | Integer | Row in attendance sheet. Default: `ATTENDANCE_SHEET.getLastRow()`      |


### HeadRun-Info.gs

#### storeObject()

Stores `obj` in the document properties under `key`.

```js
storeObject('headrunners', {...});
```

| Name | Type   | Description            |
|------|--------|------------------------|
| key  | String | Property key           |
| obj  | Object | Object to store        |


#### getAllHeadruns()

Returns all stored headruns.

```js
getAllHeadruns();
```


#### getAllHeadrunners()

Returns all stored headrunners.

```js
getAllHeadrunners();
```


#### getWeekday()

Returns day string for the given index.

```js
getWeekday(2); // returns 'tuesday'
```

| Name         | Type    | Description        |
|--------------|---------|--------------------|
| weekdayIndex | Integer | 0=Sunday, 6=Saturday|


#### getScheduleFromStore()

Returns run schedule for the specified weekday.

```js
getScheduleFromStore('monday');
```

| Name          | Type    | Description                   |
|---------------|---------|-------------------------------|
| currentWeekday| String|Int | Day name or index         |


#### getMatchedTimeKey()

Finds the time key in runSchedule matching submission time ± offset.

```js
getMatchedTimeKey(new Date(), scheduleObj, 2);
```

| Name           | Type    | Description                     |
|----------------|---------|---------------------------------|
| submissionDate | Date    | Date of the submission          |
| runSchedule    | Object  | Schedule object                 |
| offsetHours    | Integer | Offset window in hours (default `2`)|

## Triggers

1. **Form Submission**: Set up a trigger for `onFormSubmission` (From form).
2. **App Submission**: Set up a trigger for `onAppSubmission` (From event or manual).
3. **Scheduled Checks**:  
   - Use time-driven triggers (e.g., weekly, daily) for functions like `updateWeeklyCalendarTriggers`.
   - Calendar event-based triggers for event-driven attendance checks.


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

