### Ledger-Code.gs

- *function* [`getLatestTimestamp_()`](#getlatesttimestamp_)
- *function* [`getTimestampInRow_(row)`](#gettimestampinrow_row)
- *function* [`getLatestLog_()`](#getlatestlog_)
- *function* [`getLogInRow_(row)`](#getloginrow_row)
- *function* [`getAttendeesInRow_(row)`](#getattendeesinrow_row)
- *function* [`getDateAndLevelInRow_(row)`](#getdateandlevelinrow_row)
- *function* [`getMapUrlInRow_(row)`](#getmapurlinrow_row)
- *function* [`getEventPointsInRow_(row)`](#geteventpointsinrow_row)
- *function* [`getHeadrunnersInRow_(row)`](#getheadrunnersinrow_row)
- *function* [`getLogCell_(row, column)`](#getlogcell_row-column)
- *function* [`getLedgerData_(numCols)`](#getledgerdata_numcols)
- *function* [`getLedgerEntry_(email, ledgerData)`](#getledgerentry_email-ledgerdata)
- *function* [`findMemberInLedger_(email, ledger)`](#findmemberinledger_email-ledger)
- *function* [`storeImportFromAttendanceSheet(importArr)`](#storeimportfromattendancesheetimportarr)

#### getLatestTimestamp_()

Return latest head run submission timestamp in `LOG_SHEET`.

Returns:

- (Date) - Headrun submission timestamp as Date object.


#### getTimestampInRow_(row)

Return timestamp for a specified row in LOG_SHEET.

Params:

- `row` (integer) - Row number.

Returns:

- (Date) - Timestamp as Date object.

#### getLatestLog_()

Return content of latest row in log sheet.

Returns:

- (Array) - Values of each column in the last row.

#### getLogInRow_(row)

Return content of specified row in log sheet.

Params:

- `row` (integer) - Row number.

Returns:

- (Array) - Values of each column in the specified row.

#### getAttendeesInRow_(row)

Return list of attendees in specified row of log sheet.

Params:

- `row` (integer) - Row number.

Returns:

- (string) - Attendees, separated by newline.

#### getDateAndLevelInRow_(row)

Return date and level (of headruns) in specified row of log sheet.

Params:

- `row` (integer) - Row number.

#### getMapUrlInRow_(row)

Return map URL in specified row of log sheet.

Params:

- `row` (integer) - Row number.

Returns:

- (string) - Map URL, or emtpy string if not found.

#### getEventPointsInRow_(row)

Return points for the event in specified row of log sheet.

Params:

- `row` (integer) - Row number.

Returns:

- (number) - Number of points, or 0 if not found.

#### getHeadrunnersInRow_(row)

Return list of headrunners in specified row of log sheet.

Params:

- `row` (integer) - Row number.

Returns:

- (string) - Headrunners, separated by newline.

#### getLogCell_(row, column)

Returns value of specified cell in the log sheet.

Params:

- `row` (number) - Row number of cell.
- `column` (number) - Column number of cell.

Returns:

- (*) - Cell value.

#### getLedgerData_(numCols)

Get ledger data from `LEDGER_SHEET` to send emails.

Params:

- `numCols` (number) - *Optional* The number of rows to get starting from email col. 
                                              Defaults to last col before events (`LEDGER_COL_COUNT`).

Returns:

- (Object[][]) - Ledger data of col size `numCols`.


#### getLedgerEntry_(email, ledgerData)

Get ledger data of member using their email.

Params:

- `email` (string) - Member email address.
- `ledgerData` (Object[][]) - Ledger data object, from GET_LEDGER_()

Returns:

- (Array) - Values of the row corresponding to specified member, or empty array if not found.

#### findMemberInLedger_(email, ledger)

Recursive function to search for entry by email in `sheet` using binary search.
Returns row index of `email` in GSheet (1-indexed), or null if not found.

Params:

- `email` (string) - The email address to search for in `sheet`.
- `ledger` (Object[][]) - Array of rows in the ledger sheet.

Returns:

- (number|null) - Returns the 1-indexed row number where the email is found, 
                       or `null` if the email is not found.


#### storeImportFromAttendanceSheet(importArr)

Handles the transfered submission from Attendance Code and adds new row to log sheet.
Called from the Attendance Code script.

Params:

- `importArr` (Array[][]) - Submission array with non-empty run levels.

Returns:

- (integer) - The newly added row number in Log sheet


