### Ledger-Variables.gs

- *constant* [`LEDGER_SS`](#ledger_ss)
- *constant* [`LEDGER_SS_ID`](#ledger_ss_id)
- *constant* [`LEDGER_SHEET_NAME`](#ledger_sheet_name)
- *constant* [`LEDGER_SHEET`](#ledger_sheet)
- *constant* [`LOG_SHEET_NAME`](#log_sheet_name)
- *constant* [`LOG_SHEET`](#log_sheet)
- *constant* [`GET_LEDGER`](#get_ledger)
- *constant* [`GET_LOG_SHEET`](#get_log_sheet)
- *constant* [`GET_LEDGER_SHEET`](#get_ledger_sheet)
- *constant* [`TIMEZONE`](#timezone)
- *constant* [`MCRUN_EMAIL`](#mcrun_email)
- *constant* [`SCRIPT_PROPERTY_KEYS`](#script_property_keys)
- *constant* [`LEDGER_COL`](#ledger_col)
- *constant* [`LEDGER_COL_COUNT`](#ledger_col_count)
- *constant* [`LOG_COL`](#log_col)
- *constant* [`NUMBER_FORMAT_MAP`](#number_format_map)
- *constant* [`UNITS_MAP`](#units_map)
- *constant* [`LOG_TARGETS`](#log_targets)
- *constant* [`STRAVA_BASE_URL`](#strava_base_url)
- *constant* [`ACTIVITIES_ENDPOINT`](#activities_endpoint)
- *constant* [`MAPS_FOLDER`](#maps_folder)
- *constant* [`MAPS_BASE_URL`](#maps_base_url)
- *constant* [`BASE_UPLOAD_URL`](#base_upload_url)
- *constant* [`STORAGE_BUCKET_NAME`](#storage_bucket_name)
- *constant* [`EMAIL_SENDER_NAME`](#email_sender_name)
- *constant* [`POST_RUN_TEMPLATE`](#post_run_template)
- *constant* [`SUBJECT_LINE_ARR`](#subject_line_arr)
- *constant* [`POINTS_EMAIL_SUBJECT_LINE`](#points_email_subject_line)
- *constant* [`HIDDEN_PREHEADER_ARR`](#hidden_preheader_arr)
- *constant* [`WINBACKEMAIL_SUBJECT`](#winbackemail_subject)
- *constant* [`WINBACKEMAIL_TEMPLATE`](#winbackemail_template)
- *constant* [`EMAIL_LEDGER_TARGETS`](#email_ledger_targets)
- *constant* [`EMAIL_PLACEHOLDER_LABELS`](#email_placeholder_labels)
- *constant* [`TRIGGER_BASE_ID`](#trigger_base_id)
- *constant* [`MAX_STRAVA_CHECKS`](#max_strava_checks)
- *constant* [`TRIGGER_FREQUENCY`](#trigger_frequency)

#### LEDGER_SS

Ledger spreadsheet (entire file) object

#### LEDGER_SS_ID

ID for the ledger spreadsheet (entire file)

#### LEDGER_SHEET_NAME

Name of the ledger sheet

#### LEDGER_SHEET

Ledger sheet object

#### LOG_SHEET_NAME

Name for event log sheet

#### LOG_SHEET

Event log sheet object

#### GET_LEDGER

Ledger spreadsheet (entire file)
Gets contents of points ledger and stores it in the LEDGER_DATA constant

#### GET_LOG_SHEET

Gets the log sheet by ID/name
ALLOWS PROPER SHEET REF WHEN ACCESSING AS LIBRARY FROM EXTERNAL SCRIPT
SpreadsheetApp.getActiveSpreadsheet() DOES NOT WORK IN EXTERNAL SCRIPT

#### GET_LEDGER_SHEET

Gets the ledger sheet by ID/name
ALLOWS PROPER SHEET REF WHEN ACCESSING AS LIBRARY FROM EXTERNAL SCRIPT
SpreadsheetApp.getActiveSpreadsheet() DOES NOT WORK IN EXTERNAL SCRIPT

#### TIMEZONE

Timezone of the script
IMPORTANT FOR DATETIME FORMATTING AND SENDING EMAILS 

#### MCRUN_EMAIL

Official club email
IMPORTANT FOR DATETIME FORMATTING AND SENDING EMAILS

#### SCRIPT_PROPERTY_KEYS

Keys of properties in script properties (MAKE SURE NAMES MATCHES ACTUAL STORE) 

#### LEDGER_COL

Maps columns to column number in points ledger sheet
Col 16+ store event-specific points

#### LEDGER_COL_COUNT

LEDGER SHEET COL SIZE (WITHOUT EVENT-SPECIFIC POINTS COL)

#### LOG_COL

Maps columns to column number in log sheet

#### NUMBER_FORMAT_MAP

Maps Strava stats to their formatting functions

#### UNITS_MAP

Maps Strava stats to unit conversion factors for metric and imperial system

Distance -> convert meters to km or mile. 
Moving time -> keep the same.
Average speed -> convert meters/sec to km/sec or mi/sec. 
Max speed -> convert meters/sec to km/h or mph. 
Total elevation gain -> convert meters to feet for imperial.

#### LOG_TARGETS

Maps Strava stats to their target column in the event log sheet.

#### STRAVA_BASE_URL

Base url for the Strava API

#### ACTIVITIES_ENDPOINT

Endpoint for Strava activities for the Strava API

#### MAPS_FOLDER

Google Drive folder to store maps in

#### MAPS_BASE_URL

Base URL for Google Maps API

#### BASE_UPLOAD_URL

Base URL of the Google Cloud Storage API

#### STORAGE_BUCKET_NAME

Name of bucket in Google Cloud Storage

#### EMAIL_SENDER_NAME

Name (of club) as it should appear on the email sender information

#### POST_RUN_TEMPLATE

Name of the file containing template for post-run email (WITHOUT .html extension)

#### SUBJECT_LINE_ARR

List of subject lines to choose from for post-run emails

#### POINTS_EMAIL_SUBJECT_LINE

Randomly selected subject line at run-time

#### HIDDEN_PREHEADER_ARR

Hidden text for post-run emails (to display in preview?)

#### WINBACKEMAIL_SUBJECT

Subject line for win-back emails

#### WINBACKEMAIL_TEMPLATE

Name of the file containing template for win-back email (WITHOUT .html extension)

#### EMAIL_LEDGER_TARGETS

Mapping from certain email placeholder fields to the column in the ledger
that contains data for that field

#### EMAIL_PLACEHOLDER_LABELS

Mapping keys in the Strava activity object to the corresponding email placeholder fields

#### TRIGGER_BASE_ID

String to put in the key of all script properties relating to a Strava trigger

#### MAX_STRAVA_CHECKS

Maximum number of tries to find a Strava activity before triggers get deleted

#### TRIGGER_FREQUENCY

Strava trigger frequency in minutes

