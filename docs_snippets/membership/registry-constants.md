### Semester Variables.gs

#### ADMINS_

Users authorized to use the McRUN menu.

Prevents unwanted data overwrite in Gsheet.


#### SHEET_NAME

Sheet name corresponding to current semester

MUST UPDATE EVERY SEMESTER!


#### SEMESTER_SHEET

Sheet object corresponding to current semester


#### IMPORT_NAME

Name of sheet with imports from registration form


#### IMPORT_SHEET

Sheet object corresponding to imports from registration form


#### IMPORT_SHEET_ID

ID of sheet with imports from registration form


#### MASTER_NAME

Name of master sheet

#### MASTER_SHEET

Sheet object of master sheet

#### TIMEZONE

Current timezone

#### MCRUN_EMAIL

Club email

#### ZEFFY_EMAIL

Email address of Zeffy emails

#### INTERAC_EMAIL

Email address (ending) of Interac emails

#### STRIPE_EMAIL

Email address (ending) of Stripe emails

#### ONLINE_LABEL

Gmail label for online payment emails

#### INTERAC_LABEL

Gmail label for Interac payment emails

#### INTERAC_ITEM_COL

Cells for each payment method. Found in `Internal Fee Collection` sheet.

#### MEMBERSHIP_DURATION

Length of membership in years

#### WAIVER_DRIVE_ID

DRIVE URL CONTAINING WAIVERS; NOT CONFIDENTIAL


#### COL

Maps column letters to numbers (1-indexed)

#### SEMESTER_COLS

LATEST COLUMN MAPPING FOR SEMESTER SHEET (S26)
If REMOVING A CONSTANT, ENSURE IT IS NOT USED IN THE SCRIPTS!!

#### MASTER_COLS

LATEST COLUMN MAPPING FOR MASTER SHEET (S26)
If REMOVING A CONSTANT, ENSURE IT IS NOT USED IN THE SCRIPTS!!

#### IMPORT_MAP

MAPPING FROM FILLOUT REGISTRATION OBJ TO SEMESTER SHEET

#### PROCESSED_ARR

Fields in array from processing last row in semester sheet (semester columns but 0-indexed)
NOT ALL FIELDS ARE IN THIS MAPPING, only the ones needed to move to master sheet

#### CELL_EDIT_LIMIT

Number of cells that can be edited at once (for onEdit function)

#### SEMESTER_CODE_MAP

Mapping from semesters names to semester codes e.g. Winter 2025 -> W25

#### ALL_SEMESTERS

List of all semesters (names) which have sheets


#### isFeePaidFormula

GSheet formula for IS_FEE_PAID_COL in master sheet


#### INDEX_STORE_NAME

Name of property that index store is saved under

#### GET_COL_MAP_(sheet)


Retrieves the column mapping for a given sheet.
This function returns the column mapping object for the specified sheet name.
If the sheet name is not found in the mapping, it returns `null`.
Params:

- `sheet` (string) - The name of the sheet to retrieve the column mapping for.

Returns:

- (Object|null) - The column mapping object for the sheet, or `null` if not found


#### TRIGGER_FUNC

Name of fee payment check trigger

#### TRIGGER_BASE_ID

ID of fee payment check trigger

#### FEE_MAX_CHECKS

Max number of times to check for fee payment

#### TRIGGER_FREQUENCY

Trigger frequency in minutes