---
authors:
    - andrey
    - mona
date: 2026-06-09
---

# McRUN Membership List

---

## About


### Files

- **Github Repo:** [mcrun-membership-list](https://github.com/mcrunningclub/mcrun-membership-list)
- **Google Sheets:** [Memberships Collected (main)](https://docs.google.com/spreadsheets/d/1qvoL3mJXCvj3m7Y70sI-FAktCiSWqEmkDxfZWz0lFu4/edit?usp=sharing)
- **Apps Script Project:** [Membership Registry Code](https://script.google.com/home/projects)


---

## Constants

### Semester Variables.gs

 - `SHEET_NAME` - Sheet name corresponding to current semester. MUST UPDATE EVERY SEMESTER!
 - `SEMESTER_SHEET` - Sheet object corresponding to current semester
 - `IMPORT_NAME` - Name of sheet with imports from registration form
 - `IMPORT_SHEET` - Sheet object corresponding to imports from registration form
 - `IMPORT_SHEET_ID` - ID of sheet with imports from registration form
 - `MASTER_NAME` - Name of master sheet
 - `MASTER_SHEET` - Sheet object of master sheet
 - `MASTER_COL_SIZE` - Number of (relevant???) columns in the master sheet
 - `TIMEZONE` - Current (user) timezone
 - `MCRUN_EMAIL` - Club email
 - `MEMBERSHIP_DURATION` - Length of membership in years
 - `WAIVER_DRIVE_ID` - DRIVE URL CONTAINING WAIVERS; NOT CONFIDENTIAL

There are also constants for required columns in both the semester sheet and master sheet, as well as mappings for all the column in those sheets. UPDATE THESE AS NECESSARY!

---

## Functions

--8<-- "registry-formatting.md"

---

## Triggers

### Types of Triggers

- **onChange:**  
  - Handles new registration import, master updates, and triggers member processing.
- **Time-based triggers:**  
  - For periodic fee/payment checking; created as needed for follow-up.
- **onOpen:**  
  - Adds the custom admin menu for member management.

**Purpose:**  
- Ensures all new members are processed, formatted, verified, and onboarded automatically.
- Follows up on outstanding fee payments.

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Missing required fields" | Registration data not validated | Ensure all required fields are present in import |
| "Unauthorized" | Wrong or missing API key | Ensure correct API key when using web endpoints |
| "Failed to find payment" | Payment email not found | Wait for payment notification or check search terms |
| "Label does not exist" | Gmail label missing | Create Gmail label manually |
| "Script error during onFormSubmit" | Data/range not found or sheet structure changed | Check sheet structure, update code if needed |