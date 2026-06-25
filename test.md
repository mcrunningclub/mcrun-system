#### trimWhitespaceSemester_(row = getLastSubmissionInSemester())

Trims whitespace from specific columns in the last row of the semester sheet.

This function targets the range from `SEMESTER_COLS.FIRST_NAME` to `REFERRAL_COL` (7 columns).
It ensures that unnecessary whitespace is removed from the latest member entry.

Params:

- `[row=SEMESTER_SHEET.getLastRow()]` (number) - The row number to target for trimming.
                                                    Defaults to the last row in semester sheet.


#### sortSemesterByName_()

Sorts semester sheet by first name, then last name.

This function organizes the data in the semester sheet by sorting rows alphabetically
based on the `First Name` column and then the `Last Name` column.


#### tryAndSortSemester()

Sorts semester sheet only if the lock is free.

This function prevents concurrent processes from interfering with sorting
by acquiring a script lock before proceeding. If the lock is unavailable,
it logs a message and exits gracefully.


#### formatSemester()

Formats semester sheet for a simple and uniform user experience.

- Freezing panes
- Adjusting font styles, sizes, and weights
- Setting column widths
- Applying number formats and text wrapping
- Aligning text horizontally and vertically
- Adding checkboxes to specific columns
- Ensuring proper letter casing for names and email addresses * 
- Adding hyperlinks to waivers
- Formatting collection dates


#### addCheckboxSemester_(row)

Adds checkboxes to specific columns in the last row of semester sheet.

This function is used to ensure that the last row of semester sheet has checkboxes
in the `Fee Paid`, `Given to Internal`, and `Attendance Status` columns.

Params:

- `row` (number) - Row number to target for formatting.


#### fixRowCaseSemester_(row = getLastSubmissionInSemester())

Set letter case of specific columns in member entry as following:
 - Lower Case: [McGill Email Address] 
 - Capitalized: [First Name, Last Name, Preferred Name/Pronouns, Year, Program]

Params:

- `[row=getLastSubmissionInMain()]` (number) - Row number to target fix.
                                                 Defaults to last row (1-indexed).


#### sortMasterByEmail()

Sorts master sheet by email instead of first name.
Required to ensure `findSubmissionByEmail` works properly.


#### formatMaster()

Formats master sheet for simple and uniform UX.

Remove whitespace from `McGill Email Address` to `Referral`


#### cleanLastRowMaster()

Clean latest member registration in master sheet.

Data normalization includes:

 - Trim whitespace
 - Capitalize selected values e.g. name, year, program
 - Insert fee status formula in `Fee Paid` col
 - Format collection date correctly; append semester code if applicable


#### formatFeeCollection_(row = MASTER_SHEET.getLastRow())

Formats fee collection date and semester for the specified row of the master sheet.

Changes date to 'yyyy-MM-dd'. No formatting is done if fee is not paid.

Params:

- `[row=MASTER_SHEET.getLastRow()]` (number) - The starting row index for the search (1-indexed). 
                                                 Defaults to last row.

#### insertRegistrationSem_(row = MASTER_SHEET.getLastRow())

Inserts the 3-char semester code for the registration in the specified row of the master sheet.

                   The row number to target for inserting the semester code.
                   Defaults to the last row.


#### encodeFromInput_(input)

Create Member ID from input.

Params:

- `input` (string) - Usually email

Returns:

- (string) - Hash of input


#### encodeRowSemester_(row = getLastSubmissionInSemester())

Create Member ID in specified row of semester sheet.

Params:

- `row` (number) - Row to encode. Defaults to last row.


#### encodeList_(sheet)

Create Member ID for every member in given sheet.

Params:

- `sheet` (SpreadsheetApp.Sheet) - Sheet reference to encode


#### encodeByRow_(sheet, row = sheet.getLastRow())

Create single Member ID using specified row number and sheet.

Params:

- `sheet` (SpreadsheetApp.Sheet) - Sheet reference to target
- `[row=sheet.getLastRow()]` (integer) - The 1-indexed row in input `sheet`. 
                                             Defaults to the last row in the sheet.


