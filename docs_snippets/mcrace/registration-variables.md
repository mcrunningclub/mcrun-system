### Variables.gs

- *constant* [`SHEET_NAME`](#sheet_name)
- *constant* [`SHEET_ID`](#sheet_id)
- *constant* [`REGISTRATION_SHEET`](#registration_sheet)
- *constant* [`IMPORT_NAME`](#import_name)
- *constant* [`IMPORT_SHEET_ID`](#import_sheet_id)
- *constant* [`IMPORT_SHEET`](#import_sheet)
- *constant* [`GET_REGISTRATION_SHEET_`](#get_registration_sheet_)
- *constant* [`GET_IMPORT_SHEET_`](#get_import_sheet_)
- *constant* [`COL_MAP`](#col_map)
- *constant* [`isMemberCheckFormula`](#ismembercheckformula)
- *constant* [`getCurrentUserEmail_`](#getcurrentuseremail_)

#### SHEET_NAME

Name of sheet with registrations

#### SHEET_ID

ID of sheet with registrations

#### REGISTRATION_SHEET

Sheet with registrations

#### IMPORT_NAME

Name of sheet with imports from registration form

#### IMPORT_SHEET_ID

ID of sheet with imports from registration form

#### IMPORT_SHEET

Sheet with imports from registration form

#### GET_REGISTRATION_SHEET_

Returns the `Registration` sheet, falling back to the sheet ID if the name is unavailable.

Returns:

- (SpreadsheetApp.Sheet) - Registrations sheet

#### GET_IMPORT_SHEET_

Returns the `Import` sheet, falling back to the sheet ID if the name is unavailable.

Returns:

- (SpreadsheetApp.Sheet) - Import sheet

#### COL_MAP

Maps column names to their respective indices in the `Registration` sheet.
Keys must match the post data from the form submission.
Not in post data: column 11, 21, 22, 23


#### isMemberCheckFormula

GSheet formula to automatically confirm if registered is current McRUN member

#### getCurrentUserEmail_

Returns email of current user executing Google Apps Script functions.

Prevents incorrect account executing Google automations (e.g. McRUN bot.)

Returns:

- (string) - Email of current user.

