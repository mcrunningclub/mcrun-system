# McRUN Master Attendance Google Apps Script

## About

This project automates and manages attendance tracking for McRUN events using Google Sheets and Google Apps Script. It provides tools for formatting, exporting, and maintaining attendance data, ensuring consistency and seamless integration with a semester attendance sheet.

**Key Features:**

- **Automatic formatting** of names and columns for readability
- **Export of new submissions** to a semester attendance sheet
- **Sheet maintenance** (sorting, prettifying, and marking exports)
- **Timezone-aware date handling**

## Files

### Github repo
[mcrun-master-attendance](https://github.com/mcrunningclub/mcrun-master-attendance)

### Google Sheets
[McRun Head Run Attendance
(MASTER)](https://docs.google.com/spreadsheets/d/1Abu4txni1zUDI79u5OtIjpffOOoYnea9_vNM9skq0Yg/edit?usp=sharing)

### Apps Script project
[Attendance Code
(MASTER)](https://script.google.com/u/2/home/projects/1xw6D3vkg0e1iHCXndVFflxrSrUmSZAg4BeVdnaQHzk2ongvJt0DfgQQn)

## Documentation

### Functions

### Data-Formatting.gs
- **getLastSubmission_()**: Returns the last non-empty row index in the master attendance sheet.
- **formatNamesInRow_(targetCols, startRow, numRow)**: Formats names in specified columns and rows, separating names by newlines.
- **formatAllNamesInRow()**: Formats all relevant name columns (headrunners and attendees) in the last submission row.

### View-Formatting.gs
- **sortAttendanceForm()**: Sorts the master attendance sheet by timestamp (ascending).
- **prettifySheet()**: Applies formatting to the master attendance sheet for improved readability.
- **formatSpecificColumns_()**: Applies font, alignment, number format, and column width settings to key columns.

### Transfer.gs
- **onChange(e)**: Triggered on sheet changes; handles new submissions, exports, and maintenance formatting.
- **transferToSemesterSheet(row)**: Transfers the latest submission to the semester attendance sheet and marks it as exported.
- **prepareAttendanceSubmission(values)**: Converts a row of attendance data into a JSON-formatted string for export.

### Variables.gs
- **getUserTimeZone_()**: Returns the script's timezone as a string (e.g., 'America/Montreal').

## Example Usage

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

## Triggers
- The `onChange` function should be set as an installable trigger for the master attendance sheet to automate exports and formatting.

## Author
- [Andrey Gonzalez](<mailto:andrey.gonzalez@mail.mcgill.ca>)
