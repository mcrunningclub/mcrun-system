### Variables.gs

- *constant* [`LITERAL_SHEET_NAME`](#literal_sheet_name)
- *constant* [`SPREADSHEET_ID`](#spreadsheet_id)
- *constant* [`LITERAL_SHEET`](#literal_sheet)
- *constant* [`PAYMENT_LOG_SHEET_NAME`](#payment_log_sheet_name)
- *constant* [`PAYMENT_LOG_SHEET`](#payment_log_sheet)
- *constant* [`WELCOME_EMAIL_DRAFT_ID`](#welcome_email_draft_id)
- *constant* [`PASS_TEMPLATE_ID`](#pass_template_id)
- *constant* [`PASS_FOLDER_ID`](#pass_folder_id)
- *constant* [`TIMEZONE`](#timezone)
- *constant* [`MCRUN_EMAIL`](#mcrun_email)
- *constant* [`CLUB_NAME`](#club_name)
- *constant* [`GET_LITERAL_SHEET_`](#get_literal_sheet_)
- *constant* [`GET_PAYMENT_LOG_SHEET_`](#get_payment_log_sheet_)
- *constant* [`COL`](#col)
- *constant* [`LITERALS`](#literals)
- *constant* [`IMPORT_MAP`](#import_map)
- *constant* [`PAYMENT_LOGS`](#payment_logs)
- *constant* [`PAYMENT_LOG_MAP`](#payment_log_map)

#### LITERAL_SHEET_NAME

Name of Literals sheet

#### SPREADSHEET_ID

ID of New member comms spreadsheet

#### LITERAL_SHEET

Spreadsheet object of Literals sheet

#### PAYMENT_LOG_SHEET_NAME

Name of Payment Logs sheet

#### PAYMENT_LOG_SHEET

Spreadsheet object of Payment Logs sheet

#### WELCOME_EMAIL_DRAFT_ID

ID of email draft with welcome email template

#### PASS_TEMPLATE_ID

ID of file with pass template

#### PASS_FOLDER_ID

ID of folder to save passes in

#### TIMEZONE

Timezone of script

#### MCRUN_EMAIL

Club email

#### CLUB_NAME

Club name to include in "From" field for emails

#### GET_LITERAL_SHEET_

Gets Literals sheet using spreadsheet ID if needed.

ALLOWS PROPER SHEET REF WHEN ACCESSING AS LIBRARY FROM EXTERNAL SCRIPT
SpreadsheetApp.getActiveSpreadsheet() DOES NOT WORK IN EXTERNAL SCRIPT

Returns:

- (SpreadsheetApp.Sheet) - Literals sheet object

#### GET_PAYMENT_LOG_SHEET_

Gets Payment Logs sheet using spreadsheet ID if needed.

ALLOWS PROPER SHEET REF WHEN ACCESSING AS LIBRARY FROM EXTERNAL SCRIPT
SpreadsheetApp.getActiveSpreadsheet() DOES NOT WORK IN EXTERNAL SCRIPT

Returns:

- (SpreadsheetApp.Sheet) - Payment Logs sheet object

#### COL

Mapping column letters to numbers

#### LITERALS

Mapping columns in Literals sheet

#### IMPORT_MAP

Mapping from keys in import object (from Membership Registry)
to columns in Literals sheet

#### PAYMENT_LOGS

Mapping columns in Payment Logs sheet

#### PAYMENT_LOG_MAP

Mapping from fields in payment status object to columns in Payment Log sheet

