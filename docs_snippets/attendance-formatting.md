### Formatting.gs

- *function* [`addMissingPlatform_(row)`](#addmissingplatform_row)
- *function* [`formatSemesterAttendance()`](#formatsemesterattendance)
- *function* [`formatConfirmationInRow_(row)`](#formatconfirmationinrow_row)
- *function* [`formatAllNames()`](#formatallnames)
- *function* [`formatNamesInRow_(row)`](#formatnamesinrow_row)
- *function* [`formatAttendeeNamesInRow_(row)`](#formatattendeenamesinrow_row)
- *function* [`formatHeadrunnersInRow_(startRow, numRow)`](#formatheadrunnersinrow_startrow-numrow)
- *function* [`formatHeadrunnerName_(name)`](#formatheadrunnername_name)
- *function* [`formatHeadrunInRow_(startRow, numRow)`](#formatheadruninrow_startrow-numrow)
- *function* [`runOnSheet_(functionName, functionName2)`](#runonsheet_functionname-functionname2)
- *function* [`sortSemesterAttendance()`](#sortsemesterattendance)
- *function* [`removePresenceChecks()`](#removepresencechecks)
- *function* [`formatSpecificColumns_()`](#formatspecificcolumns_)

#### addMissingPlatform_(row)

Adds `Google Form` as source of attendance submission.

#### formatSemesterAttendance()

Global wrapper function that runs the following on the sheet:

 - formats head run column for each row
 - formats headrunner names for each row
 - formats attendees' names for each row
 - formats confirmations in each row

Row number is 1-indexed in GSheet. Header row skipped. Top-to-bottom execution.

#### formatConfirmationInRow_(row)

Formats confirmation bool in `row` into user-friendly string.

Params:

- `row=ATTENDANCE_SHEET.getLastRow()` (integer) - The row in the `ATTENDANCE_SHEET` sheet (1-indexed).
                                                      Defaults to the last row in the sheet.

#### formatAllNames()

Wrapper function for `formatAttendeeNamesInRow` and `formatHeadRunnerInRow`
for **ALL** submissions in GSheet.
Row number is 1-indexed in GSheet. Header row skipped. Top-to-bottom execution.

#### formatNamesInRow_(row)

Wrapper function for `formatAttendeeNamesInRow` and `formatHeadRunnerInRow`.
Formats headrunner and attendee names in target `row`.

Params:

- `row=ATTENDANCE_SHEET.getLastRow()` (integer) - The row in the `ATTENDANCE_SHEET` sheet (1-indexed).
                                                      Defaults to the last row in the sheet.

#### formatAttendeeNamesInRow_(row)

Formats attendee names from `row` into uniform view, sorted and separated by newline.

Params:

- `row=ATTENDANCE_SHEET.getLastRow()` (integer) - The row in the `ATTENDANCE_SHEET` sheet (1-indexed).
                                                      Defaults to the last row in the sheet.

Example:

```javascript
// Sample Script ➜ Format names in row `13`.
const rowToFormat = 13;
formatNamesInRow(rowToFormat);
```

#### formatHeadrunnersInRow_(startRow, numRow)

Formats headrunner names from `row` into uniform view, separated by newline.
Updated format is '`${firstName} ${lastNameLetter}.`'

Params:

- `row=ATTENDANCE_SHEET.getLastRow()` (integer) - The row in the `ATTENDANCE_SHEET` sheet (1-indexed).
                                                      Defaults to the last row in the sheet.
- `numRow` (integer) - Number of rows to format from `startRow`.

Example:

```javascript
// Sample Script ➜ Format names in row `7`.
const rowToFormat = 7;
formatHeadrunnerInRow(rowToFormat);
// Sample Script ➜ Format names from row `3` to `9`.
const startRow = 3;
const numRow = 9 - startRow;
formatHeadrunnerInRow(startRow, numRow);
```

#### formatHeadrunnerName_(name)

Callback function to clean and format a single headrunner name

Params:

- `name` (string) - Original string

Returns:

- (string) - Formatted string

#### formatHeadrunInRow_(startRow, numRow)

Removes hyphen-space in headrun from `row` if applicable.
                     The row in the `ATTENDANCE_SHEET` sheet (1-indexed).
                     Defaults to the last row in the sheet.

Params:

- `numRow=1` (integer) - Number of rows to format from `startRow`

#### runOnSheet_(functionName, functionName2)

Boiler plate function `functionName` to execute on complete sheet.
Also executes `functionName2` if non-empty.

Params:

- `functionName` (string) - Name of function to execute.
- `functionName2=""` (string) - Name of function to execute.
                                     Defaults to empty string.

#### sortSemesterAttendance()

Sorts the `ATTENDANCE_SHEET` by submission time.
Excludes the header row from sorting.

#### removePresenceChecks()

Changes the attendance status of all members to "not present."
Helper function for `consolidateMemberData()`.

#### formatSpecificColumns_()

Formats specific columns of the `HR Attendance` sheet for better readability.
Includes freezing panes, bold formatting, text wrapping, alignment, and column resizing.

