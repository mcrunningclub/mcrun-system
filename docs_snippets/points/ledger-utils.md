### Utils.gs

- *function* [`getUserTimeZone_()`](#getusertimezone_)
- *function* [`getCurrentUserEmail_()`](#getcurrentuseremail_)
- *function* [`getFileByName_(name)`](#getfilebyname_name)
- *function* [`getFileById_(id)`](#getfilebyid_id)
- *function* [`logAsPL_(msg, funcName, useLogger)`](#logaspl_msg-funcname-uselogger)
- *function* [`getValidLastRow_(sheet)`](#getvalidlastrow_sheet)
- *function* [`escapeData_(str)`](#escapedata_str)
- *function* [`fillInTemplateFromObject_(template, data)`](#fillintemplatefromobject_template-data)
- *constant* [`prettyLog_`](#prettylog_)
- *function* [`getUnixEpochTimestamp_(timestamp)`](#getunixepochtimestamp_timestamp)

#### getUserTimeZone_()

Gets the timezone of the script

Returns:

- (string) - Time zone

#### getCurrentUserEmail_()

Gets the email of the user accessing the script

Returns:

- (string) - Email address

#### getFileByName_(name)

Tries to find a file in Google Drive by its name

May have an error if there are no results?

Params:

- `name` (string) - Name of the file to find

Returns:

- (File) - The first result of the search

#### getFileById_(id)

Tries to find a file in Google Drive by its ID

May have an error if there are no results?

Params:

- `id` (string) - ID of the file to find

Returns:

- (File) - The first result of the search

#### logAsPL_(msg, funcName, useLogger)

Creates log in the console with specific formatting

Params:

- `msg` (string) - The message to log
- `funcName` (string) - *Optional* Name of the function returning the message, if applicable. Defaults to ""
- `useLogger` (boolean) - *Optional* Whether to use the logger (true) or console.log (false). Defaults to true.

#### getValidLastRow_(sheet)

Find row index of last entry, starting from bottom using while-loop.

Used to prevent native `sheet.getLastRow()` from returning empty row.

Params:

- `sheet` (SpreadsheetApp.Sheet) - Target sheet.

Returns:

- (integer) - Returns 1-index of last row in `sheet`.


#### escapeData_(str)

Escape cell data to make JSON safe

Params:

- `str` (string) - to escape JSON special characters from

Returns:

- (string) - escaped string

#### fillInTemplateFromObject_(template, data)

Fill template string with data object

Params:

- `template` (string) - string containing {{}} markers which are replaced with data
- `data` (object) - object used to replace {{}} markers

Returns:

- (object) - message replaced with data


#### prettyLog_

Simple logging of multi-line message. Improves readability in code.

Params:

- `msg` (string) - The message(s) to log

#### getUnixEpochTimestamp_(timestamp)

Convert a Date timestamp to a Unix Epoch timestamp.

Params:

- `timestamp` (Date) - Timestamp to convert.

Returns:

- (integer) - Number of seconds elapsed since January 1, 1970.


