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

### Files

- **Github Repo:** [points-system](https://github.com/mcrunningclub/points-system)
- **Google Sheets:** [Points Ledger - 2025/2026](https://docs.google.com/spreadsheets/d/1sar-Pmfb_Nar0Lc9u8-rXyllLvQMqBFlSwolCoHX-_4/edit?gid=1311788414#gid=1311788414)
- **Apps Script Project:** [Points Ledger Code (McRUN)](https://script.google.com/u/0/home/projects/1S77DvcDMmE9Z9ScZKV4xIHnRZY6DCA74I-lcqMY-8Ts8cALDENK_nibF/edit)

### Libraries and Services

- OAuth2 library
- Gmail service

### Permissions

You must have edit access to the points spreadsheet (club email).

| Description | URL |
| --- | --- |
| See, edit, create, and delete all your Google Sheets spreadsheets | https://www.googleapis.com/auth/spreadsheets |
| Connect to an external service | https://www.googleapis.com/auth/script.external_request |
| See, edit, create, and delete all of your Google Drive files | https://www.googleapis.com/auth/drive |
| Send email as you | https://www.googleapis.com/auth/script.send_mail |
| Allow this application to run when you are not present | https://www.googleapis.com/auth/script.scriptapp |
| Read, compose, send, and permanently delete all your email from Gmail | https://mail.google.com/ |
| See your primary Google Account email address | https://www.googleapis.com/auth/userinfo.email |

---

## Constants

--8<-- "points/ledger-constants.md"

---

## Functions

--8<-- "points/ledger-ledgercode.md"
--8<-- "points/ledger-formatting.md"
--8<-- "points/ledger-stravacode.md"
--8<-- "points/ledger-stravaservice.md"
--8<-- "points/ledger-mapgeneration.md"
--8<-- "points/ledger-sendemail.md"
--8<-- "points/ledger-triggers.md"
--8<-- "points/ledger-htmlextraction.md"
--8<-- "points/ledger-utils.md"

---

## Triggers

### Time-based

- Created and deleted by the script for checking Strava activities, sending emails, etc.

### Other

- The `doGet(e)` function is used as a web app endpoint for remote automation.

---

## Troubleshooting & FAQ

| Issue/Error | Cause | Solution |
|-------------|-------|----------|
| "Unauthorized! Please verify key." | Wrong API key | Set correct key in script properties and request |
| "No permission" | Missing OAuth scopes | Ensure all required Apps Script scopes are granted |
| "Cannot read property 'getRange' of null" | Missing or renamed sheet/range | Double-check all sheet names and constants |
| "Rate limit exceeded" | Strava API throttling | Wait and retry, ensure efficient API use |
| "OAuth error" | Strava authorization failed | Use `reset()` or `safeReset()` to reauthorize |

- **How do I update Strava credentials?**  
  Update `CLIENT_ID` and `CLIENT_SECRET` in Apps Script > Project Properties.

- **How do I add a new event type?**  
  Update constants in `Ledger-Variables.gs` and related logic in points calculation.

- **How do I test a function?**  
  Use the Apps Script IDE's “Run” feature; check the logs/output in Execution Log.