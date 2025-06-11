# Setup

## Quick Start

This guide is for contributors and club admins to get up and running with the McRUN Attendance scripts.

## Permissions
- Google Sheets: Edit access
- Gmail: Read access
- Calendar: Read/write access


## Edit Scripts
- Open the Google Sheet and ensure you are signed in with the correct Google account.
- Authorize the Apps Script project when prompted (first use or after script changes).
- If using scheduled triggers, ensure you have permission to create time-based triggers in Apps Script.
- Open the Apps Script editor (Extensions > Apps Script) to view or modify scripts.

## Run Scripts
- Most scripts run automatically on form submission or via custom menu in the Sheet.
- Manual triggers can be run from the Apps Script editor if needed.


### 1. Prerequisites

- A Google Workspace (Gmail) account with edit access to the [Attendance Sheet](https://docs.google.com/spreadsheets/d/1SnaD9UO4idXXb07X8EakiItOOORw5UuEOg0dX_an3T4/).
- Permissions to view and edit Google Apps Script attached to this Sheet.
- Club admin email(s) must be added to the `PERM_USER_` constant in the code.

### 2. Setup Steps

- **Open Google Sheet**: Open the [Attendance Sheet](https://docs.google.com/spreadsheets/d/1SnaD9UO4idXXb07X8EakiItOOORw5UuEOg0dX_an3T4/) and go to Extensions > Apps Script.
- **Add/Update Scripts**: Copy script files from this repo into the Apps Script editor.
- **Deploy Triggers**:  
  - In Apps Script, go to Triggers.
  - Set up triggers for functions like `onFormSubmission`, `onAppSubmission`, and any scheduled calendar checks as described in this documentation.
- **Test Automation**:  
  - Submit a test attendance form.
  - Confirm attendance is processed, formatted, and transferred to the Points Ledger.
  - Check logs (View > Executions) for errors.

### 3. Permissions for Contributors

- Add your Google account to the Editors list for the Sheet.
- Request admin to whitelist your email in the `PERM_USER` array.

---

## Environment & Permissions

### Google Account Permissions

- **Sheets API**: Read and write access to the Attendance Sheet and Points Ledger.
- **Gmail API**: (If using email features) Send and read email.
- **Calendar API**: For time-based and event-based triggers.
- **Properties Service**: Store persistent data (e.g., headrunners, headruns).

### Apps Script Scopes

Be sure to grant the following scopes when authorizing for the first time:

- `https://www.googleapis.com/auth/spreadsheets`
- `https://www.googleapis.com/auth/script.external_request`
- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/gmail.send` (if emailing)
- `https://www.googleapis.com/auth/script.properties`
- `https://www.googleapis.com/auth/userinfo.email`

### Setting Up Triggers

1. **Form Submission**: Set up a trigger for `onFormSubmission` (From form).
2. **App Submission**: Set up a trigger for `onAppSubmission` (From event or manual).
3. **Scheduled Checks**:  
   - Use time-driven triggers (e.g., weekly, daily) for functions like `updateWeeklyCalendarTriggers`.
   - Calendar event-based triggers for event-driven attendance checks.
