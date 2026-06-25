### Utils.gs

#### removeDiacritics_(str)

Removes diacritics (accents) from a string.

This function normalizes the input string and removes any diacritical marks,
ensuring a clean, ASCII-compatible output.

Params:

 - `str` (string) - The string to normalize and strip of diacritics.

Returns:

 - (string) - The normalized string without diacritics.


#### getSemesterCode_(semester)

Get semester code from semester sheet name in map, or creates if not found.

First letter of code is W/F/S corresponding to first letter of semester
and next two are digits YY corresponding to the year.

Params:

- `semester` (string) - Semester name e.g. Fall 2024

Returns:

- (string) - Semester code e.g. F24

#### getLastSubmissionInSemester()

Find row index of last submission, starting from bottom using while-loop.

Used to prevent native `sheet.getLastRow()` from returning empty row.

Returns:

- (number) - Returns 1-index of last row in GSheet.

#### getUserTimeZone_()

Returns timezone for currently running script.

Prevents incorrect time formatting during time changes like Daylight Savings Time.

Returns:

- (string) - Timezone as geographical location (e.g.`'America/Montreal').

#### getCurrentUserEmail_()

Returns email of current user executing Google Apps Script functions.

Prevents incorrect account executing Google automations (e.g. McRUN bot.)

Returns:

- (string) - Email of current user.

#### parseBool_(val)

Converts a string to a boolean value.

Params:

- `val` (string) - A string that contains a boolean.

Returns:

- (boolean) - Parsed value.

#### changeSheetView_(sheetName)

Activate the sheet `sheetName` in Google Spreadsheet.

Changes view to `sheetName`.

Params:

- `sheetName` (string) - Name of target sheet.
