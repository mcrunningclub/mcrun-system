### Transfer.gs

- *function* [`onChange(e)`](#onchangee)
- *function* [`transferLastSubmissionToSemester(row)`](#transferlastsubmissiontosemesterrow)
- *function* [`prepareAttendanceSubmission(values)`](#prepareattendancesubmissionvalues)

#### onChange(e)

Triggered when a change occurs in the spreadsheet.
Handles edit events for the master attendance sheet. If the change is an edit on the correct sheet,
it triggers the transfer of the latest submission to the semester attendance sheet and runs maintenance formatting functions.

Params:

- `e` (Events.SheetsOnChange) - The event object containing information about the change.


#### transferLastSubmissionToSemester(row)

Transfers the latest attendance submission to the semester attendance sheet.
Attempts to use the connected library for transfer; if it fails, falls back to direct sheet access via URL.
Marks the submission as exported upon success.

Once exported, `importSheet` does not process the submission until it checks for missing attendance.
The triggers for checking attendance are time-based.

Previous attempt to trigger `onChange(e)` for `importSheet` did not work.
This is due to GAS restrictions. See page below for more information.

https://developers.google.com/apps-script/guides/triggers/installable#google_apps_triggers

These are the functions that were used to try and externally trigger `onChange(e)`:

- sheet.setValues
- sheet.appendRow
- sheet.activate
- sheet.insertRowAfter
- sheet.hideRow + sheet.unhideRow
- sheet.hideRows + sheet.showRows
- sheet.deleteRow
- ss.setActiveRange
- ss.insertSheet + ss.deleteSheet

Params:

- `row` (number) - Row index in the master attendance sheet to transfer (1-based). Defaults to last row.

#### prepareAttendanceSubmission(values)

Prepare the attendance values into JSON object to send to semester attendance spreadsheet.

Params:

- `values` (string[]) - Run attendance information from master attendance.

Returns:

- (string) - JSON-formatted string.

