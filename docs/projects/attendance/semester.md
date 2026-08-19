---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRUN Attendance

---

## About

### Files

- **Github Repo:** [mcrun-attendance](https://github.com/mcrunningclub/mcrun-attendance)
- **Google Sheets:** [Head Run Attendance - 2025/26](https://docs.google.com/spreadsheets/d/1kUevgOCN1wCdbNiVY412-7ejnlSjtIyKNHFVLV9KK1Q/edit?gid=1289953364)
- **Apps Script Project:** [Attendance Code 2025/2026](https://script.google.com/home/projects/1Vu_Atd-PFXXXFbUL3qb8gH4ncFfAsAkWNsr4Adnavjk-JnqtvAa8v5u5/edit)

## Constants

--8<-- "attendance/attendance-constants.md"

## Functions

--8<-- "attendance/attendance-formatting.md"
--8<-- "attendance/attendance-headrunattendance.md"
--8<-- "attendance/attendance-headruninfo.md"
--8<-- "attendance/attendance-import.md"
--8<-- "attendance/attendance-pointsledger.md"
--8<-- "attendance/attendance-triggers.md"
--8<-- "attendance/attendance-unregistered.md"
--8<-- "attendance/attendance-usermenu.md"
--8<-- "attendance/attendance-utils.md"

## Triggers

### Time-based

- **updateWeeklyCalendarTriggers** runs every day(?) to update the triggers, and creates various time-based triggers which are later disabled 

### From spreadsheet

- **onOpen** runs when the spreadsheet is opened to create the usermenu

### From Calendar

- **updateCalendarTriggers** (now called cleanUpCalendarTriggersForToday) is supposed to run whenever the calendar is changed


## Example Usage

### Automating Attendance Processing
```javascript
onFormSubmission(); // Automatically processes a new Google Form submission.
```

### Formatting Data
```javascript
cleanSheetData(); // Formats all rows in the attendance sheet.
```

### Sending Notifications
```javascript
sendEmailReminder_({
  emailsByLevel: { beginner: ["headrunner@mail.com"] },
  headrunTitle: "Monday 6pm"
});
```

### Managing Triggers
```javascript
updateWeeklyCalendarTriggers(); // Updates triggers for the upcoming week.
```

## Troubleshooting

### Common Issues

| Issue/Error | Cause | Solution |
|-------------|-------|----------|
| "Exception: No permission" | Not authorized | Ensure proper account and OAuth scopes |
| "Cannot read property 'getRange' of null" | Sheet name or ID is wrong | Double-check constants in Attendance-Variables.gs |
| "Trigger not firing" | Trigger not set up | Manually add the trigger in Apps Script UI |
| "Malformed JSON" | Import data is not valid JSON | Validate data before import |

### FAQ

**Q:** How do I add a new admin?  
**A:** Add their email to `PERM_USER_` in `User-Menu.gs`.

**Q:** How do I change the active semester?  
**A:** Update `ATTENDANCE_SHEET_NAME` and related constants in `Attendance-Variables.gs`.

**Q:** Where are attendance logs stored?  
**A:** In the Points Ledger Google Sheet (see constants).
