### Attendance-Variables.gs

- *constant* [`ATTENDANCE_SHEET_NAME`](#attendance_sheet_name)
- *constant* [`SEMESTER_NAME`](#semester_name)
- *constant* [`ATTENDANCE_SHEET_ID`](#attendance_sheet_id)
- *constant* [`ATTENDANCE_SHEET`](#attendance_sheet)
- *constant* [`GET_ATTENDANCE_SHEET_`](#get_attendance_sheet_)
- *constant* [`COL`](#col)
- *constant* [`SEM_ATTENDANCE_COLS`](#sem_attendance_cols)
- *constant* [`TIMEZONE`](#timezone)
- *constant* [`ATTENDEE_MAP`](#attendee_map)
- *constant* [`NUM_LEVELS`](#num_levels)
- *constant* [`EMPTY_ATTENDEE_FLAG`](#empty_attendee_flag)
- *constant* [`MEMBERSHIP_SHEET_NAME`](#membership_sheet_name)
- *constant* [`MEMBERSHIP_URL`](#membership_url)
- *constant* [`MEMBER_EMAIL_COL`](#member_email_col)
- *constant* [`MEMBER_SEARCH_KEY_COL`](#member_search_key_col)
- *constant* [`LOG_SHEET_NAME`](#log_sheet_name)
- *constant* [`POINTS_LEDGER_URL`](#points_ledger_url)
- *constant* [`HEADRUN_SHEET_ID`](#headrun_sheet_id)
- *constant* [`COMPILED_SHEET_NAME`](#compiled_sheet_name)
- *constant* [`GET_COMPILED_SHEET_`](#get_compiled_sheet_)
- *constant* [`HEADRUNNER_SHEET_NAME`](#headrunner_sheet_name)
- *constant* [`GET_HEADRUNNER_SHEET_`](#get_headrunner_sheet_)
- *constant* [`SCRIPT_PROPERTY`](#script_property)
- *constant* [`GET_PROP_STORE_`](#get_prop_store_)
- *constant* [`COPY_EMAIL_TEMPLATE`](#copy_email_template)
- *constant* [`REMINDER_EMAIL_TEMPLATE`](#reminder_email_template)
- *constant* [`GET_ATTENDANCE_FORM_LINK_`](#get_attendance_form_link_)
- *constant* [`PRESIDENT_EMAIL`](#president_email)
- *constant* [`VP_INTERNAL_EMAIL`](#vp_internal_email)
- *constant* [`CLUB_EMAIL`](#club_email)
- *constant* [`APP_EMAIL`](#app_email)
- *constant* [`HEADRUNNER_STORE_NAME`](#headrunner_store_name)
- *constant* [`HEADRUN_STORE_NAME`](#headrun_store_name)
- *constant* [`IMPORT_SHEET_ID`](#import_sheet_id)
- *constant* [`IMPORT_SHEET`](#import_sheet)
- *constant* [`GET_IMPORT_SHEET_`](#get_import_sheet_)
- *constant* [`IMPORT_MAP`](#import_map)
- *constant* [`PERM_USER_`](#perm_user_)

#### ATTENDANCE_SHEET_NAME

Name of attendance sheet for the current semester
TO UPDATE EACH SEMESTER 

#### SEMESTER_NAME

Name of semester
TO UPDATE EACH SEMESTER 

#### ATTENDANCE_SHEET_ID

ID of attendance sheet for the current semester
TO UPDATE EACH SEMESTER 

#### ATTENDANCE_SHEET

Attendance sheet object for the current semester
TO UPDATE EACH SEMESTER 

#### GET_ATTENDANCE_SHEET_

Retrieves the attendance sheet for the current semester.
Ensures proper sheet reference when accessing as a library from an external script.

Returns:

- (GoogleAppsScript.Spreadsheet.Sheet) - The attendance sheet object.

#### COL

Mapping of column letters to numbers

#### SEM_ATTENDANCE_COLS

Mapping of columns in semester attendance sheet to column number (1-indexed)

#### TIMEZONE

Timezone of the script

#### ATTENDEE_MAP

Maps run levels to column with attendees for that level

#### NUM_LEVELS

Number of run levels

#### EMPTY_ATTENDEE_FLAG

String indicating that there are no attendees for a run level

#### MEMBERSHIP_SHEET_NAME

Name of sheet (in membership spreadsheet) with master registry

#### MEMBERSHIP_URL

URL of membership spreadsheet

#### MEMBER_EMAIL_COL

Column in membership list with member email

#### MEMBER_SEARCH_KEY_COL

Column in membership list with member key (ID?)

#### LOG_SHEET_NAME

Name of sheet with events log in points ledger spreadsheet

#### POINTS_LEDGER_URL

URL of points ledger spreadsheet

#### HEADRUN_SHEET_ID

ID of spreadsheet with head run schedule and list of head runners

#### COMPILED_SHEET_NAME

Name of sheet with compiled head runs and head runners

#### GET_COMPILED_SHEET_

Sheet object with compiled head runs and head runners

#### HEADRUNNER_SHEET_NAME

Name of sheet with list of head runners and their info

#### GET_HEADRUNNER_SHEET_

Sheet object with list of head runners and their info

#### SCRIPT_PROPERTY

Maps information to script property name with that information

#### GET_PROP_STORE_

Script properties
Get property store or create if not found

#### COPY_EMAIL_TEMPLATE

Name of email template used to send attendance copy (without '.html')

#### REMINDER_EMAIL_TEMPLATE

Name of email template used to send reminder (without '.html')

#### GET_ATTENDANCE_FORM_LINK_

Gets link of Google Form connected to attendance sheet

Returns:

- (string) - Link to attendance form

#### PRESIDENT_EMAIL

Email of club president

#### VP_INTERNAL_EMAIL

Email of club VP Internal (VP Headruns)

#### CLUB_EMAIL

Club email address

#### APP_EMAIL

Email address used to access the attendance app

#### HEADRUNNER_STORE_NAME

Name of script property that has headrunner info

#### HEADRUN_STORE_NAME

Name of script property that has headrun info/schedule

#### IMPORT_SHEET_ID

ID of sheet with app imports

#### IMPORT_SHEET

Sheet object with app imports

#### GET_IMPORT_SHEET_

ALLOWS PROPER SHEET REF WHEN ACCESSING AS LIBRARY FROM EXTERNAL SCRIPT
SpreadsheetApp.getActiveSpreadsheet() DOES NOT WORK IN EXTERNAL SCRIPT

#### IMPORT_MAP

MAPPING FROM MASTER ATTENDANCE SHEET TO SEMESTER SHEET

#### PERM_USER_

Users authorized to use the McRUN menu.
Prevents unwanted data overwrite in Gsheet.

