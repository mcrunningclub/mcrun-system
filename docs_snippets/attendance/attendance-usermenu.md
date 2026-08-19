### User-Menu.gs

- *function* [`logMenuAttempt_(email)`](#logmenuattempt_email)
- *function* [`onOpen()`](#onopen)
- *function* [`helpUI_()`](#helpui_)
- *function* [`confirmAndRunUserChoice_(functionName, additionalMsg, funcArg)`](#confirmandrunuserchoice_functionname-additionalmsg-funcarg)
- *function* [`sortByTimestampUI_()`](#sortbytimestampui_)
- *function* [`cleanSheetDataUI_()`](#cleansheetdataui_)
- *function* [`prettifySheetUI_()`](#prettifysheetui_)
- *function* [`formatAllNamesUI_()`](#formatallnamesui_)
- *function* [`formatNamesInRowUI_()`](#formatnamesinrowui_)
- *function* [`removePresenceCheckUI_()`](#removepresencecheckui_)
- *function* [`checkMissingAttendanceUI_()`](#checkmissingattendanceui_)
- *function* [`toggleAttendanceCheckUI_()`](#toggleattendancecheckui_)
- *function* [`findUnregisteredAttendeesUI_()`](#findunregisteredattendeesui_)
- *function* [`onFormSubmitUI_()`](#onformsubmitui_)
- *function* [`onAppSubmitUI_()`](#onappsubmitui_)
- *function* [`exportToPointsLedgerUI_()`](#exporttopointsledgerui_)
- *function* [`importAppRecordUI_()`](#importapprecordui_)
- *function* [`requestRowInput_()`](#requestrowinput_)
- *function* [`processRowInput_(userResponse, ui)`](#processrowinput_userresponse-ui)

#### logMenuAttempt_(email)

Logs the user attempting to use the custom McRUN menu.
If the input is empty, the email is extracted using `getCurrentUserEmail_()`.

Params:

- `email` (string) - *Optional* Email of the active user. Defaults to an empty string.

#### onOpen()

Creates a custom menu to run frequently used scripts in Google App Script.
Extracts function names using the `name` property to allow for refactoring.
Note: Authorization checks cannot be performed here, as unauthorized users
would not see the menu due to Google Apps Script limitations.

#### helpUI_()

Displays a help message for the custom McRUN menu.
Accessible to all users.

#### confirmAndRunUserChoice_(functionName, additionalMsg, funcArg)

Displays a confirmation dialog and executes a function if the user is authorized.

Params:

- `functionName` (string) - Name of the function to execute.
- `additionalMsg` (string) - *Optional* Custom message to display during execution. Defaults to an empty string.
- `funcArg` (string) - *Optional* Argument to pass to the function. Defaults to an empty string.

Returns:

- (string) - Return value of the executed function.

#### sortByTimestampUI_()

Scripts for formatting: Sort semester attendance sheet by timestamp

#### cleanSheetDataUI_()

Scripts for formatting: Clean data in semester attendance sheet

#### prettifySheetUI_()

Scripts for formatting: Format semester attendance sheet

#### formatAllNamesUI_()

Scripts for formatting: Format names for all rows in semester attendance sheet

#### formatNamesInRowUI_()

Scripts for formatting: Format names for a given row in semester attendance sheet.
This UI function can target a specific row, or the last row if input is omitted.

#### removePresenceCheckUI_()

Scripts for attendance: Remove prescence checkmarks

#### checkMissingAttendanceUI_()

Scripts for attendance: Check for missing attendance

#### toggleAttendanceCheckUI_()

Scripts for attendance: Allow/Disallow automatic check for missing attendance

#### findUnregisteredAttendeesUI_()

Scripts for attendance: Find unregistered attendees.
This UI function can target a specific row, or the last row if input is omitted.

#### onFormSubmitUI_()

Scripts for triggers: Process new attendance submission (for google form).

#### onAppSubmitUI_()

Scripts for triggers: Process new attendance submission (for app).

#### exportToPointsLedgerUI_()

Scripts for transferring: Export attendance to points ledger.

#### importAppRecordUI_()

Scripts for transferring: Import attendance recorded from app.

#### requestRowInput_()

Creates popup that asks user to input a row number.


#### processRowInput_(userResponse, ui)

Returns result of reponse processing for row input.
Helper function for UI functions for McRUN menu.

Params:

- `userResponse` (string) - User response text from `SpreadsheetApp.getUi().prompt`
- `ui` (GoogleAppsScript.Base.Ui) - User interface in Google Sheets
                   parsed integer value of `userResponse` and msg is the custom 
                   message to display to the user.


