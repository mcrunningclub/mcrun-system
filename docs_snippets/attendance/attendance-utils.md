### Utils.gs

- *function* [`getUserTimeZone_()`](#getusertimezone_)
- *function* [`getStartOfDay_(date)`](#getstartofday_date)
- *function* [`getEndOfDay_(date)`](#getendofday_date)
- *function* [`getCurrentUserEmail_()`](#getcurrentuseremail_)
- *function* [`logAsAC_(msg, funcName, useLogger)`](#logasac_msg-funcname-uselogger)
- *function* [`toTitleCase_(inputString)`](#totitlecase_inputstring)
- *function* [`getLastRow_(sheet)`](#getlastrow_sheet)
- *function* [`runOnSheet_(functionName, functionName2)`](#runonsheet_functionname-functionname2)
- *function* [`formatTimestamp_(raw)`](#formattimestamp_raw)
- *function* [`isSameTimestamp_(timestamp1, timestamp2)`](#issametimestamp_timestamp1-timestamp2)
- *function* [`isValidRow_(row)`](#isvalidrow_row)
- *function* [`checkValidScriptProperties()`](#checkvalidscriptproperties)

#### getUserTimeZone_()

Returns timezone for currently running script.
Prevents incorrect time formatting during time changes like Daylight Savings Time.

Returns:

- (string) - Timezone as a geographical location (e.g., `'America/Montreal'`).

#### getStartOfDay_(date)

Gets the start of the day for a given date.

Params:

- `date` (Date) - The date for which to get the start of the day.

Returns:

- (Date) - A new Date object set to the start of the given day.

#### getEndOfDay_(date)

Gets the end of the day for a given date.

Params:

- `date` (Date) - The date for which to get the end of the day.

Returns:

- (Date) - A new Date object set to the end of the given day.

#### getCurrentUserEmail_()

Returns the email of the current user executing Google Apps Script functions.
Useful for ensuring the correct account is executing Google automations.

Returns:

- (string) - Email of the current user.

#### logAsAC_(msg, funcName, useLogger)

Logs message in a standard and comprehensible format.

Params:

- `msg` (string) - Message to log
- `funcName` (string) - *Optional* Name of the function to log if applicable. Defaults to "".
- `useLogger` (boolean) - *Optional* If true, use the Logger class, otherwise use console. Defaults to true.

#### toTitleCase_(inputString)

Converts a string to title case.

Params:

- `inputString` (string) - The string to be converted to title case.

Returns:

- (string) - The title-cased string.

#### getLastRow_(sheet)

Find row index of last submission in reverse using while-loop.

Used to prevent native `sheet.getLastRow()` from returning empty row.

Params:

- `sheet` (Spreadsheet.sheet) - *Optional*  Target sheet. Defaults to attendance sheet.

Returns:

- (integer) - Returns 1-index of last row in GSheet.


#### runOnSheet_(functionName, functionName2)

Boiler plate function `functionName` to execute on complete sheet.
Also executes `functionName2` if non-empty.

Params:

- `functionName` (string) - Name of function to execute.
- `functionName2` (string) - *Optional* Name of function to execute.
                                     Defaults to empty string.

#### formatTimestamp_(raw)

Format timestamp to format as `yyyy-MM-dd hh:mm:ss`.

Raw format cannot be understood by GSheet.

Params:

- `raw` (string) - Datetime value to be formatted.

Returns:

- (Date) - A Date object with correct format.


#### isSameTimestamp_(timestamp1, timestamp2)

Compare the input timestamps.

Params:

- `timestamp1` (string) - Timestamp 1
- `timestamp2` (string) - Timestamp 2

Returns:

- (Boolean) - Returns result of comparaison.


#### isValidRow_(row)

Returns true if row is int and found in `ATTENDANCE_SHEET`.
Helper function for UI functions for McRUN menu.

Params:

- `row` (number) - The row number in `ATTENDANCE_SHEET` 1-indexed.

Returns:

- (boolean) - Returns true if valid row in sheet.

#### checkValidScriptProperties()

Verifies that `SCRIPT_PROPERTY` bank matches script properties in 'Project Settings'.

