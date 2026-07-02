### Variables.gs

- *constant* [`MASTER_ATTENDANCE_SHEET_ID`](#master_attendance_sheet_id)
- *constant* [`MASTER_ATTENDANCE_SHEET`](#master_attendance_sheet)
- *constant* [`SEMESTER_ATTENDANCE_SHEET_ID`](#semester_attendance_sheet_id)
- *constant* [`SEMESTER_ATTENDANCE_URL`](#semester_attendance_url)
- *constant* [`COL`](#col)
- *constant* [`MASTER_ATTENDANCE_COLS`](#master_attendance_cols)
- *constant* [`TIMEZONE`](#timezone)
- *function* [`getUserTimeZone_()`](#getusertimezone_)

#### MASTER_ATTENDANCE_SHEET_ID

Master attendance sheet id

#### MASTER_ATTENDANCE_SHEET

Master attendance sheet object

#### SEMESTER_ATTENDANCE_SHEET_ID

ID of semester attendance sheet

#### SEMESTER_ATTENDANCE_URL

URL of sememseter attendance sheet

#### COL

Mapping of column letters to numbers

#### MASTER_ATTENDANCE_COLS

Indices of columns in attendance sheet

#### TIMEZONE

Timezone of script

#### getUserTimeZone_()

Returns the timezone for the currently running script as a geographical location string.
This function ensures that all date and time formatting operations use the correct timezone,
preventing issues such as incorrect time display during Daylight Savings Time transitions.

Returns:

- (string) - The timezone in IANA format (e.g., 'America/Montreal').


