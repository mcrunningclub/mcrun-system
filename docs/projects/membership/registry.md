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

### Libraries and Services

- [New Member Communications](./communications.md) library
- Gmail service


---

## Constants

### Semester Variables.gs

There are constants for important sheets within the Google Sheet file:

 - `SHEET_NAME`, `SEMESTER_SHEET` - Sheet name and object corresponding to current semester. MUST UPDATE EVERY SEMESTER!
 - `IMPORT_NAME`, `IMPORT_SHEET`, `IMPORT_SHEET_ID` - Sheet name, object, and ID with imports from registration form
 - `MASTER_NAME`, `MASTER_SHEET` - Sheet name and object corresponding to the master sheet
 - `MASTER_COL_SIZE` - Number of (relevant???) columns in the master sheet

The columns in each sheet, as well as in the imported JSON strings and semester codes, have mapping constants:

 - `SEMESTER_COLS`, `MASTER_COLS` - Latest column mapping for semester sheet
 - `IMPORT_MAP` - Mapping from Fillout registration object to semester sheet
 - `PROCESSED_ARR` - Fields in array from processing last row in semester sheet (0-indexed)
 - `SEMESTER_CODE_MAP` - Mapping from semesters names to semester codes e.g. Winter 2025 -> W25
 - `ALL_SEMESTERS` - List of all semesters (names) which have sheets

There are also constants for required columns in the semester sheet:

 - `REGISTRATION_DATE_COL`, `EMAIL_COL`, `FIRST_NAME_COL`, `LAST_NAME_COL`, `PREFERRED_NAME_COL`, `YEAR_COL`, `PROGRAM_COL`, `DESCRIPTION_COL`, `REFERRAL_COL`, `WAIVER_COL`, `PAYMENT_METHOD_COL`, `INTERAC_REF_COL`, `IS_FEE_PAID_COL`, `COLLECTION_DATE_COL`, `COLLECTION_PERSON_COL`, `IS_INTERNAL_COLLECTED_COL`, `COMMENTS_COL`, `ATTENDANCE_STATUS_COL`, `MEMBER_ID_COL`

Same for the master sheet:

 - `MASTER_EMAIL_COL`, `MASTER_FIRST_NAME_COL`, `MASTER_LAST_NAME_COL`, `MASTER_LAST_REG_SEM`, `MASTER_FEE_STATUS`, `MASTER_FEE_EXPIRATION`, `MASTER_FEE_COLLECTOR`, `MASTER_COLLECTION_DATE`, `MASTER_IS_INTERNAL_COLLECTED`, `MASTER_PAYMENT_HIST`, `MASTER_MEMBER_ID_COL`

Other constants:

 - `TIMEZONE` - Current (user) timezone
 - `MCRUN_EMAIL` - Club email
 - `INTERAC_EMAIL`, `ZEFFY_EMAIL`, `STRIPE_EMAIL` - Email addresses for each type of payment
 - `ONLINE_LABEL`, `INTERAC_LABEL` - Gmail labels for each type of payment
 - `INTERAC_ITEM_COL`, `ONLINE_PAYMENT_ITEM_COL`, `FEE_WAIVED_ITEM_COL` - Cells for each payment method. Found in `Internal Fee Collection` sheet.
 - `MEMBERSHIP_DURATION` - Length of membership in years
 - `WAIVER_DRIVE_ID` - Drive URL containing waivers. NOT CONFIDENTIAL
 - `isFeePaidFormula` - GSheet formula for IS_FEE_PAID_COL in master sheet

Finally, there is a function:

#### GET_COL_MAP_(sheet)

Retrieves the column mapping for a given sheet.

This function returns the column mapping object for the specified sheet name.
If the sheet name is not found in the mapping, it returns `null`.

Params:

- `sheet` (string) - The name of the sheet to retrieve the column mapping for.

Returns:

- (Object|null) - The column mapping object for the sheet, or `null` if not found

---

## Functions

--8<-- "registry-formatting.md"
--8<-- "registry-masterscripts.md"
--8<-- "registry-memberfee.md"
--8<-- "registry-memberships.md"
--8<-- "registry-utils.md"

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