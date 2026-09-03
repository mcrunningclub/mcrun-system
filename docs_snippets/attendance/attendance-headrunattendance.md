### Headrun-Attendance.gs

- *function* [`onFormSubmission()`](#onformsubmission)
- *function* [`processRow_(row)`](#processrow_row)
- *function* [`onAppSubmission(row)`](#onappsubmissionrow)
- *function* [`packageAndEmailAttendance_(row)`](#packageandemailattendance_row)
- *function* [`toggleAttendanceCheck_()`](#toggleattendancecheck_)
- *function* [`getHeadrunTitle_(submission)`](#getheadruntitle_submission)
- *function* [`checkMissingAttendance(today, headrunTitle, level)`](#checkmissingattendancetoday-headruntitle-level)
- *function* [`sendBotEmail_(subject, recipient, htmlBody)`](#sendbotemail_subject-recipient-htmlbody)
- *function* [`createAttendanceEmail_(emailDetails)`](#createattendanceemail_emaildetails)
- *function* [`sendAttendanceCopy_({ headrunTitle, headrunnerEmails }, submission)`](#sendattendancecopy_)
- *function* [`sendAttendanceReminder_({ emailsByLevel, headrunTitle })`](#sendattendancereminder_)

#### onFormSubmission()

Functions to execute after form submission.

Sort & format attendance and process last row (newest).
To use as a trigger function, it cannot have parameters.
Otherwise, a runtime exception is raised for new form submission.

#### processRow_(row)

Sets platform to "Google Form", formats, and extracts unregistered
members for the given row.

Params:

- `row` (number) - The row index in the attendance sheet to process.

#### onAppSubmission(row)

Functions to execute after McRUN app submission.

Format new entry, transfer to Points Ledger, sort & format attendance.

Params:

- `row` (number) - *Optional* The row index in the attendance sheet to process.
                                            Defaults to the last row.

#### packageAndEmailAttendance_(row)

Get headrunner emails from the submission and send them a copy of the submitted
attendance.

Cannot be called using Attendance Code library (i.e. from AC-M)

Params:

- `row` (number) - Row number of submission

#### toggleAttendanceCheck_()

Toggles the flag to run `checkAttendance()` by updating the value in the `ScriptProperties` bank.

Returns:

- (string) - The new state of the attendance checker ("true" or "false").


#### getHeadrunTitle_(submission)

Gets the headrun title (weekday + AM/PM) from attendance submission.
If no submission, uses current date.

Params:

- `submission` (list) - Values from row in attendance sheet

Returns:

- (string) - e.g. Tuesday AM

#### checkMissingAttendance(today, headrunTitle, level)

Checks for missing submissions after a scheduled headrun.

The service property IS_CHECKING_ATTENDANCE must be set to true.

Params:

- `today` (Date) - *Optional* Date to check. Defaults to current day.
- `headrunTitle` (string) - Title of the headrun
- `level` (string?) - Level of the headrun

Returns:

- (boolean) - True if attendance is missing?


#### sendBotEmail_(subject, recipient, htmlBody)

Sends an email using the McRUN bot.

Params:

- `subject` (string) - The subject of the email.
- `recipient` (string) - The recipient's email address.
- `htmlBody` (string) - The HTML content of the email.

#### createAttendanceEmail_(emailDetails)

Create email using details from input `emailDetails' for internal use

Params:

- `emailDetails` (Map<string>) - Information needed to populate email body.

Returns:

- (string) - HTML code for email.

Example:

```js
// Sample Script ➜ Create email using info.
const emailDetails = {
   title : 'Monday - 6pm',
   distance : '5km',
   attendees : `['- Beginner: Bob Burger', '- Easy: Marge Simpson, Mabel Pines']`,
   confirmation : No,
   comments : 'Bob will pay fee next time.'
};
const emailHTML = createEmailCopy(emailDetails);
```

#### sendAttendanceCopy_(\{ headrunTitle, headrunnerEmails \}, submission) {#sendattendancecopy_}

Send a copy of attendance submission to headrunners, President & VP Internal.
Attendees are separated by level.

Params:

- `emailObj` (Object) - Contains email details.
   - `emailObj.headrunTitle` (string) - The title of the headrun.
   - `emailObj.headrunnerEmails` (Object) - Emails of headrunners grouped by levels.
- `submission` (Array) - The attendance submission data.

#### sendAttendanceReminder_(\{ emailsByLevel, headrunTitle \}) {#sendattendancereminder_}

Send a reminder email to headrunners when attendance for a respective headrun not found.

Params:

- `emailObj` (Object) - Contains email details.
   - `emailObj.emailsByLevel` (Object) - Emails of headrunners grouped by levels.
   - `emailObj.headrunTitle` (string) - The title of the headrun.

