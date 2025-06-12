---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRUN Points System

---

## About

The **McRUN Points System** is a Google Apps Script codebase designed to automate, calculate, and manage member points and event logs for the McGill Students Running Club. This system integrates with Google Sheets to record and tally participation, interfaces with Strava to extract running data, and automates communications and formatting via Gmail and Google Drive.

The project's purpose is to streamline the tracking of club events, automate member points calculation, and enhance the club's engagement and reporting using cloud tools and APIs.

### Files

- **Github Repo:** [points-system](https://github.com/mcrunningclub/points-system)
- **Google Sheets:** [Points Ledger - 2024/2025](https://docs.google.com/spreadsheets/d/1DwmnZgLftSqegfsoFA5fekuT0sosgCntVMmTylbj8o4)
- **Apps Script Project:** [Points Ledger Code (McRUN)](https://script.google.com/u/0/home/projects/1S77DvcDMmE9Z9ScZKV4xIHnRZY6DCA74I-lcqMY-8Ts8cALDENK_nibF/edit) _(Accessible via Extensions > Apps Script in the Google Sheet)_

### Key Features

- **Automated points calculation** and event logging for club activities.
- **Strava API integration** to auto-import running data.
- **Dynamic email generation** for reporting and member notifications.
- **Custom formatting** of event and points ledger sheets.
- **Time-based and web triggers** for scheduled automation.
- **Script property storage** for secure handling of credentials.
- **Tools for extracting and formatting HTML email templates.**
- **Map image generation** for event routes.
- **Robust logging and error handling.**


### Tools Used

- Google Apps Script (Sheets, Drive, Gmail, Calendar)
- Strava API (OAuth2)
- Google Cloud APIs (Maps, Storage)
- Make.com automations
- HTML template processing for emails

---

## Function Docs

This section is divided by project file (in alphabetical order). Each file includes a list of all its functions and a detailed entry for each.

> **Note:** Functions named with a trailing underscore (`_`) are internal but documented here with the underscore removed.

<br>
<!-- 
    🔴 FORMATTING.GS
-->

### # <big> Formatting.gs </big>
- [`sortTimestampByAscending()`](#sorttimestampbyascending) → Sorts event log by timestamp ascending
- [`formatSpecificColumns()`](#formatspecificcolumns) → Formats columns in Head Run Attendance sheet
- [`toTitleCase(inputString)`](#totitlecaseinputstring) → Converts a string to title case

---

#### ## <big> sortTimestampByAscending() </big>
Sorts the event log sheet by event timestamp (ascending, skipping headers).

```js
sortTimestampByAscending();
```

**Pitfalls:** Assumes event timestamp is in column 3 and headers are at row 1.

---

#### ## <big> formatSpecificColumns() </big>
Applies formatting (bold, wrap, checkbox, font size) to columns in the "Head Run Attendance" sheet.

```js
formatSpecificColumns();
```

**Pitfalls:** Sheet/range must exist; formatting is hardcoded.

---

#### ## <big> toTitleCase(inputString) </big>
Converts a string to title case.

```js
const result = toTitleCase("hello world");
```

| Name        | Type   | Description         |
|-------------|--------|---------------------|
| inputString | String | String to format    |

**Output:** String (title-cased)

---

<br>
<!-- 
    🔴 HTML-EXTRACTION.GS
-->

### # <big> HTML-Extraction.gs </big>
- [`extractTagsFromProjectFile()`](#extracttagsfromprojectfile) → Extracts placeholder tags from HTML template
- [`extractPlaceholders()`](#extractplaceholders) → Extracts double-curly placeholders from email text
- [`createInlineImage(fileUrl, blobKey)`](#createinlineimagefileurl-blobkey) → Creates inline image blob
- [`saveDraftAsHtml()`](#savedraftashtml) → Saves a Gmail draft as an HTML file in Drive

---

#### ## <big> extractTagsFromProjectFile() </big>
Extracts all placeholder tags (e.g., `<?= TAG ?>`) from a named HTML file in the project.

```js
extractTagsFromProjectFile();
```

**Output:** In Logger.

---

#### ## <big> extractPlaceholders() </big>
Extracts all `{{placeholder}}` tags from the email template text.

```js
extractPlaceholders();
```

**Output:** Logs placeholder list

**Pitfalls:** Requires `STATS_EMAIL_OBJ.text` to be defined.

---

#### ## <big> createInlineImage(fileUrl, blobKey) </big>
Creates a blob for an image file from its Google Drive URL and assigns a content ID.

```js
const blob = createInlineImage('https://drive.google.com/file/d/FILE_ID/view', 'mapCid');
```

| Name    | Type   | Description             |
|---------|--------|-------------------------|
| fileUrl | String | Drive file URL          |
| blobKey | String | Blob name/content ID    |

**Output:** Blob (image for inline email attachment)

**Pitfalls:** File must exist and be accessible.

---

#### ## <big> saveDraftAsHtml() </big>
Saves the body of a Gmail draft (by subject line) as an HTML file in Drive.

```js
saveDraftAsHtml();
```

**Output:** Creates file in Drive

**Pitfalls:** Draft with the specified subject must exist.

---

<br>
<!-- 
    🔴 LEDGER-CODE.GS
-->

### # <big> Ledger-Code.gs </big>
- [`newSubmission()`](#newsubmission) → Formats and sorts a new event submission
- [`getLatestSubmissionTimestamp()`](#getlatestsubmissiontimestamp) → Gets latest event timestamp (Date)
- [`getSubmissionTimestamp(row)`](#getsubmissiontimestamprow) → Gets event timestamp for a row
- [`getValidLastRow(sheet)`](#getvalidlastrowsheet) → Gets last non-empty row in a sheet
- [`getLatestLog()`](#getlatestlog) → Gets the latest log row data
- [`getLogInRow(row)`](#getloginrowrow) → Gets data for a specific row
- [`getAttendeesInLog(row)`](#getattendeesinlogrow) → Gets attendees for a log row

---

#### ## <big> newSubmission() </big>
Formats the columns and sorts timestamps for a new event submission.

```js
newSubmission();
```

**Output:** None

---

#### ## <big> getLatestSubmissionTimestamp() </big>
Returns the latest event timestamp as a Date object.

```js
const latest = getLatestSubmissionTimestamp();
```

**Output:** Date

---

#### ## <big> getSubmissionTimestamp(row) </big>
Returns the timestamp of a submission for a given row.

```js
const ts = getSubmissionTimestamp(7);
```

| Name | Type    | Description      |
|------|---------|------------------|
| row  | Integer | Row in sheet     |

**Output:** Date

---

#### ## <big> getValidLastRow(sheet) </big>
Finds the last non-empty row in a sheet.

```js
const lastRow = getValidLastRow(LOG_SHEET);
```

| Name | Type  | Description    |
|------|-------|----------------|
| sheet| Sheet | Sheet to check |

**Output:** Integer (row index)

---

#### ## <big> getLatestLog() </big>
Returns the data (array) from the latest log row.

```js
const log = getLatestLog();
```

---

#### ## <big> getLogInRow(row) </big>
Returns log row data as array for a specific row.

```js
const rowData = getLogInRow(10);
```

| Name | Type    | Description      |
|------|---------|------------------|
| row  | Integer | Row in sheet     |

**Output:** Array

---

#### ## <big> getAttendeesInLog(row) </big>
Gets the list of attendees for a given log row.

```js
const attendees = getAttendeesInLog(5);
```

| Name | Type    | Description      |
|------|---------|------------------|
| row  | Integer | Row in sheet     |

---

<br>
<!-- 
    🔴 LEDGER-VARIABLES.GS
-->

### # <big> Ledger-Variables.gs </big>
- [`getLedger()`](#getledger) → Returns cached ledger data
- [`getLogSheet()`](#getlogsheet) → Returns Event Log sheet object
- [`getLedgerSheet()`](#getledgersheet) → Returns Member Points sheet object

---

#### ## <big> getLedger() </big>
Returns or initializes the cached ledger data.

```js
const data = getLedger();
```

**Output:** Array/object

---

#### ## <big> getLogSheet() </big>
Returns the Event Log sheet object.

```js
const sheet = getLogSheet();
```

**Output:** Sheet

---

#### ## <big> getLedgerSheet() </big>
Returns the Member Points sheet object.

```js
const sheet = getLedgerSheet();
```

**Output:** Sheet

---

<br>
<!-- 
    🔴 MAP-GENERATION.GS
-->

### # <big> Map-Generation.gs </big>
- [`createAndAppendMap(timestamp, activity)`](#createandappendmaptimestamp-activity) → Generates and appends map URL to activity
- [`createStravaMap(activity, name)`](#createstravamapactivity-name) → Creates PNG map image from Strava activity
- [`saveMapForRun(polyline, name)`](#savemapforrunpolyline-name) → Saves map for run to storage

---

#### ## <big> createAndAppendMap(timestamp, activity) </big>
Creates and stores a PNG map from Strava activity, appending the URL to the activity.

```js
const updatedActivity = createAndAppendMap(new Date(), activityObj);
```

| Name      | Type   | Description          |
|-----------|--------|----------------------|
| timestamp | Date   | Event timestamp      |
| activity  | Object | Strava activity data |

**Output:** Object (activity with `mapUrl` property)

---

#### ## <big> createStravaMap(activity, name) </big>
Creates a PNG map image from a Strava activity and returns the blob.

```js
const blob = createStravaMap(activityObj, 'run-map.png');
```

| Name     | Type   | Description        |
|----------|--------|--------------------|
| activity | Object | Strava activity    |
| name     | String | Map file name      |

**Output:** Blob

---

#### ## <big> saveMapForRun(polyline, name) </big>
Saves a polyline as a map image using Google Maps API and automation.

```js
const resp = saveMapForRun('encoded_polyline', 'run-map.png');
```

| Name     | Type   | Description        |
|----------|--------|--------------------|
| polyline | String | Encoded polyline   |
| name     | String | Map file name      |

**Output:** API response

---

<br>
<!-- 
    🔴 SEND-EMAIL.GS
-->

### # <big> Send-Email.gs </big>
- [`logStatus(messageArr, logSheet, thisRow)`](#logstatusmessagearr-logsheet-thisrow) → Logs email sending status

---

#### ## <big> logStatus(messageArr, logSheet, thisRow) </big>
Logs the email sending/update status for a given row.

```js
logStatus(['Sent', 'Success'], LOG_SHEET, 5);
```

| Name       | Type     | Description                   |
|------------|----------|-------------------------------|
| messageArr | String[] | Array of status messages      |
| logSheet   | Sheet    | Log sheet object (default: `LOG_SHEET`) |
| thisRow    | Integer  | Row number (default: last row)|

**Output:** None (status appended in sheet)

---

<br>
<!-- 
    🔴 STRAVA-CODE.GS
-->

### # <big> Strava-Code.gs </big>
- [`findAndStoreStravaActivity(row)`](#findandstorestravaactivityrow) → Finds and stores Strava activity for a log row
- [`prettyLog(msg)`](#prettylogmsg) → Multi-line log utility

---

#### ## <big> findAndStoreStravaActivity(row) </big>
Finds Strava activity for a row (from log or API), stores it, and returns the activity.

```js
const activity = findAndStoreStravaActivity(10);
```

| Name | Type    | Description                       |
|------|---------|-----------------------------------|
| row  | Integer | Row to process (default: last log)|

**Output:** Object (Strava activity)

**Pitfalls:** User must be logged in as club; Strava API may rate limit.

---

#### ## <big> prettyLog(...msg) </big>
Logs multiple lines for better readability.

```js
prettyLog('line1', 'line2', 'line3');
```

| Name | Type    | Description           |
|-----|----------|-----------------------|
| msg | String[] | Messages to log       |

---

<br>
<!-- 
    🔴 STRAVA-SERVICE.GS
-->

### # <big> Strava-Service.gs </big>
- [`reset()`](#reset) → Resets Strava OAuth2 authorization state
- [`safeReset()`](#safereset) → Conditionally resets OAuth2 state
- [`getStravaActivity(fromTimestamp, toTimestamp)`](#getstravaactivityfromtimestamp-totimestamp) → Fetches Strava activities in a time range
- [`getStravaService()`](#getstravaservice) → Configures and returns the OAuth2 service

---

#### ## <big> reset() </big>
Resets the Strava OAuth2 authorization state.

```js
reset();
```

**Output:** None

---

#### ## <big> safeReset() </big>
Resets Strava OAuth2 authorization if allowed in script properties.

```js
safeReset();
```

**Output:** None

---

#### ## <big> getStravaActivity(fromTimestamp, toTimestamp) </big>
Fetches Strava activities in the given time range.

```js
const activities = getStravaActivity(unixStart, unixEnd);
```

| Name          | Type    | Description     |
|---------------|---------|-----------------|
| fromTimestamp | Integer | Start Unix time |
| toTimestamp   | Integer | End Unix time   |

**Output:** Array of Strava activities

---

#### ## <big> getStravaService() </big>
Configures and returns the OAuth2 service for Strava.

```js
const service = getStravaService();
```

**Output:** OAuth2 service object

---

<br>
<!-- 
    🔴 TRIGGERS.GS
-->

### # <big> Triggers.gs </big>
- [`doGet(e)`](#dogete) → Handles GET requests for Strava triggers
- [`createNewStravaTrigger(row)`](#createnewstravatriggerrow) → Creates a time-based Strava trigger for a row
- [`runStravaChecker()`](#runstravachecker) → Checks for Strava activity and cleans up triggers

---

#### ## <big> doGet(e) </big>
Handles GET requests to set up Strava triggers via web endpoint.

```js
doGet(e);
```

| Name | Type   | Description                                |
|------|--------|--------------------------------------------|
| e    | Object | Event object from web request              |

**Output:** ContentService TextOutput

**Pitfalls:** Requires correct API key in `e.parameter.key`.

---

#### ## <big> createNewStravaTrigger(row) </big>
Creates a new time-based trigger for checking Strava for a row.

```js
createNewStravaTrigger(5);
```

| Name | Type    | Description                       |
|------|---------|-----------------------------------|
| row  | Integer | Row to associate with the trigger |

**Output:** None (side effect: creates trigger and script property)

---

#### ## <big> runStravaChecker() </big>
Checks all active Strava triggers, verifies activities, and cleans up when found.

```js
runStravaChecker();
```

**Output:** None

---

## Triggers

The project uses several types of triggers:

- **Time-based triggers**: Scheduled (e.g., every 30 minutes) for checking Strava activities, sending emails, and formatting sheets.
- **Web app triggers**: The `doGet(e)` function can be deployed as a web app endpoint for remote automation.
- **Manual triggers**: Functions like `newSubmission()` or `safeReset()` may be called manually for setup or maintenance.

**Purpose:**  
Triggers automate the periodic checking for new Strava runs, update points, send notifications, and keep the points ledger up to date without human intervention.

## Troubleshooting & FAQ

| Issue/Error | Cause | Solution |
|-------------|-------|----------|
| "Unauthorized! Please verify key." | Wrong API key | Set correct key in script properties and request |
| "No permission" | Missing OAuth scopes | Ensure all required Apps Script scopes are granted |
| "Cannot read property 'getRange' of null" | Missing or renamed sheet/range | Double-check all sheet names and constants |
| "Rate limit exceeded" | Strava API throttling | Wait and retry, ensure efficient API use |
| "OAuth error" | Strava authorization failed | Use `reset()` or `safeReset()` to reauthorize |

**FAQ**

- **How do I update Strava credentials?**  
  Update `CLIENT_ID` and `CLIENT_SECRET` in Apps Script > Project Properties.

- **How do I add a new event type?**  
  Update constants in `Ledger-Variables.gs` and related logic in points calculation.

- **How do I test a function?**  
  Use the Apps Script IDE's “Run” feature; check the logs/output in Execution Log.

---

## See Also

- [McRUN Attendance](https://github.com/mcrunningclub/mcrun-attendance)
- [Strava API Docs](https://developers.strava.com/docs/)
- [Google Apps Script OAuth2 Library](https://github.com/googleworkspace/apps-script-oauth2)
- [Apps Script Properties Service](https://developers.google.com/apps-script/guides/properties)

---

_Last updated: 2025-06-12_