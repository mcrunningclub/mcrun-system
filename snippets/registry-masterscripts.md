### Master Scripts.gs

#### addLastSubmissionToMaster_(`lastRow`)

Adds the last submission from semester sheet to the master sheet.

This function processes the last row of the semester sheet, consolidates the data,
and ensures the master sheet is sorted by email after the new entry is added.

Params:

- `lastRow` (number) - The row number of the last submission in the semester. Defaults to the last row.

#### addPaidSemesterToMaster_(`memberRow`, `semesterSheetName`)

Updates Payment History in master sheet from the member's semester sheet where they registered.

Appends the semester code to the payment history column if it is not already present.

Params:

- `memberRow` (number) - The 1-indexed row number of the member in master sheet.
- `semesterSheetName` (string) - The name of the member's latest registration semester sheet.

#### updateFeeStatusSemester_(`payHistory`, `memberRow`, `isFeePaidCol`, `semesterSheet`)

Updates the `isFeePaid` status in the member's semester sheet.

This function checks if the member's semester code is present in their payment history.
If the code is found, it sets `isFeePaid` to `true`; otherwise, it sets it to `false`.

Params:

- `payHistory` (string) - The payment history of the member, stored as newline-separated semester codes.
- `memberRow` (number) - The 1-indexed row number of the member in the semester sheet.
- `isFeePaidCol` (number) - The 1-indexed column number of the `isFeePaid` field in the semester sheet.
- `semesterSheet` (SpreadsheetApp.Sheet) - The member's latest registration sheet (e.g., "Fall 2024").

#### processLastSubmission_(`lastRow`)

Processes the last submitted row from the semester, adding semester codes to relevant fields like `MEMBER_DESCR`, `REFERRAL`, `COMMENTS`, and payment history.

Params:

- `lastRow` (number) - The row number of the last submission in the semester. Defaults to the last row.

Returns:

- (string[]) - Array of processed values for the last submission.

#### consolidateLastSubmission_(`lastRow`)

Consolidates the last submitted row from semester into master sheet.

Checks if an existing entry with the same email exists in the MASTER sheet:

 - If found, updates specific fields with concatenated data from both entries.
 - If not found, appends the new data as a fresh row.

Params:

- `lastRow` (number) - The row number of the last submission in the semester. Defaults to the last row.

#### processSemesterData_(`sheetName`)

Processes data for a given semester sheet, adding semester codes to selected
fields and returning the formatted data. 

Helper function for `consolidateMemberData()`.

`const processedData = processSemesterData('Fall 2024');`

Params:

- `sheetName` (string) - The name of the semester sheet to process (e.g., 'Fall 2024').

Returns:

- (string[][] ?) - Returns an array of processed row data for the given semester.

#### consolidateMemberData_()

Combines data from 2024 semesters into new master sheet (overwrites existing)

Get and process semester data and concatenate, then create a map indexed by emails
to make sure entries are unique/combine entries with the same email. Sorts output by first name.

#### getSemesterCode_(`semester`)

Get semester code from semester sheet name in map, or creates if not found.

First letter of code is W/F/S corresponding to first letter of semester
and next two are digits YY corresponding to the year.

Params:

- `semester` (string) - Semester name e.g. Fall 2024

Returns:

- (string) - Semester code e.g. F24


#### sortUniqueData()

Combine data from 2024 and sort it into a new master sheet (overwrites existing)

Combines sheet values with their sheet name, then removes duplicates and sorts by
first name.