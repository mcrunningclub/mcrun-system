### Transfer Scripts.md

#### onChange(e)

When a sheet is changed, check if a row was added and process it accordingly.

If new row added to Import sheet, try to add the data to the semester sheet, format
it, and add to master sheet. If new row added to master sheet by the app, try to format it and add the data to the semester sheet.

Params:

- `e` (Event) - Edit event

#### isNewMemberViaApp_(row)

Checks whether a row (in the master sheet) was added from the app or not.

Registrations added from the app do not have the registration semester, so it needs to be added.

Params:

- `row` (number) -   Row to check.

Returns:

- (boolean) - True if row was added from app, false if not.

#### setMemberId_(sheet, row)

Encode member's email from given sheet and row, and sets it in the Member ID column.

Params:

- `sheet` (SpreadsheetApp.Sheet) - Sheet object that row is from.
- `row` (number) - Row of member to make ID for.


#### onEdit(e)

If master or semester sheet is edited, copies changes to the other sheet as well.

When a sheet is edited, check whether it was the master or semester sheet, 
and if the edited range was within bounds of sheet contents. If so, get
member row in source (edited) and target (other) sheet, and call updateFeeInfo

Params:

- `e` (Event) - Edit event

#### isLegalEdit_(range, sheet)

Check whether the given range is within valid range of the given sheet.

Valid range includes all rows except header rows, and all columns from leftmost
until the "Internal Collected" column

Params:

- `range` (Range) - Range from Event Object from `onEdit`.
- `sheet` (SpreadsheetApp.Sheet) - Sheet where edit occurred.

Returns:

- (boolean) - True if range and sheet are valid, False otherwise

#### updateFeeInfo_(range, sourceSheetName, targetRow, targetSheet)

Update fee status from `sourceSheet` to `targetSheet`.

Includes handling the different ways of storing fee payment (boolean in semester sheet,
list of semesters in master sheet)

Params:

- `range` (Range) - Range from Event Object from `onEdit`.
- `sourceSheetName` (string) - Name of source sheet to extract fee info.
- `targetRow` (number) - Target row to update.
- `targetSheet` (SpreadsheetApp.Sheet) - Target sheet to update fee info.

#### copyFilloutRegToSemester_(registration, row)

Transfer new member registration from `Import` to semester sheet.

Params:

- `registration` (Object) - Information on member registration.
- `row` (number) - Gsheet row number to target,  defaults to last row

#### packageMemberInfo_(row)

Creates an object containing member information for creating membership pass

Gets member's email, first and last name, member ID, membership status, and
membership expiration.

Params:

- `row` (number) - Row of member to package information for

Returns:

- (Object) - Member information