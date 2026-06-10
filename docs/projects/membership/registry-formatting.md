### Formatting.gs

#### trimWhitespaceSemester_(`row`)

Trims whitespace from specific columns in the specified row of the semester sheet.

This function targets the range from `FIRST_NAME_COL` to `REFERRAL_COL` (7 columns).
It ensures that unnecessary whitespace is removed from the latest member entry.

Params:

 - `row` (number) - The row number to target for trimming. Defaults to the last row in semester sheet.

#### removeDiacritics_(`str`)

Removes diacritics (accents) from a string.

This function normalizes the input string and removes any diacritical marks,
ensuring a clean, ASCII-compatible output.

Params:

 - `str` (string) - The string to normalize and strip of diacritics.

Returns:

 - (string) - The normalized string without diacritics.

#### sortSemesterByName_()

Sorts semester sheet by first name, then last name.

This function organizes the data in the semester sheet by sorting rows alphabetically
based on the `First Name` column and then the `Last Name` column.

#### addCheckboxSemester_(`row`)

Adds checkboxes to specific columns in the last row of semester sheet.
 
This function is used to ensure that the last row of semester sheet has checkboxes
in the `Fee Paid`, `Given to Internal`, and `Attendance Status` columns.

Params:

- `row` (number) - Row number to target for formatting.

#### fixRowCaseSemester_(`row`)

Set letter case of specific columns in member entry as following:

 - Lower Case: [McGill Email Address] 
 - Capitalized: [First Name, Last Name, Preferred Name/Pronouns, Year, Program]

Params:

- `row` (number)

#### formatSemester()

Formats semester sheet for a simple and uniform user experience.

- Freezing panes
- Adjusting font styles, sizes, and weights
- Setting column widths
- Applying number formats and text wrapping
- Aligning text horizontally and vertically
- Adding checkboxes to specific columns
- Ensuring proper letter casing for names and email addresses
- Adding hyperlinks to waivers
- Formatting collection dates

#### tryAndSortSemester()

Sorts semester sheet only if the lock is free.

This function prevents concurrent processes from interfering with sorting
by acquiring a script lock before proceeding. If the lock is unavailable,
it logs a message and exits gracefully.

#### sortMasterByEmail()

Sorts master sheet by email instead of first name.
 
Required to ensure `findSubmissionByEmail` works properly.

#### formatMaster()

Formats `MASTER_SHEET` for simple and uniform UX.

Remove whitespace from `McGill Email Address` to  `Referral`

#### cleanLastRowMaster()

Clean latest member registration in master sheet.

Data normalization includes:

 - Trim whitespace
 - Capitalize selected values e.g. name, year, program
 - Insert fee status formula in `Fee Paid` col
 - Format collection date correctly; append semester code if applicable

#### formatFeeCollection_(`row`)

Formats fee collection date and semester for the specified row of the master sheet.

Changes date to 'yyyy-MM-dd'. No formatting is done if fee is not paid.

Params:

 - `row` (number) - The starting row index for the search (1-indexed). Defaults to last row.

#### insertRegistrationSem_(`row`)

Inserts the 3-char semester code for the registration in the specified row of the master sheet.

Params:

- `row` (number) - The row number to target for inserting the semester code. Defaults to the last row.

#### encodeFromInput_(`input`)

Create Member ID from input.

Params:

- `input` (string) - Usually email

Returns:

- (string) - Hash of input

#### encodeRowSemester_(`row`)

Create Member ID in specified row of semester sheet.

Params:

 - `row` (number) - Row to encode. Defaults to last row.

#### encodeList_(`sheet`)

Create Member ID for every member in given sheet.

Params:

 - `sheet` (SpreadsheetApp.Sheet) - Sheet reference to encode

#### encodeByRow_(`sheet`, `row`)

Create single Member ID using specified row number and sheet.

Params:

- `sheet` (SpreadsheetApp.Sheet) - Sheet reference to target
- `row` (integer) - The 1-indexed row in input `sheet`. Defaults to the last row in the sheet.