### Membership Collected.gs

#### onFormSubmit(`newRow`)

Handles the submission of a new registration form.

This function processes the latest submission in the semester sheet by:

- Trimming whitespace
- Fixing letter case
- Generating a unique member ID
- Adding missing items (e.g., checkboxes)
- Verifying payment information
- Sending communications to the new member

It also ensures that the data is added to the master sheet and sorted appropriately.

Params:

- `newRow` (number) - The row number of the new submission. Defaults to the last row in the semester sheet.

#### sendNewMemberCommunications(`row`)

Sends communications to a new member.

This function packages the member's information and transfers it to the New Member Communications sheet for further processing.

Params:

- `row` (number) - The row number of the new member in the semester.

#### MD5(`input`)

Hash function using modified MD5 algorithm.

Used for members' External ID.

Params:

- `input` (string) - The string to hash.

Returns:

- (string) - Returns MD5-hashed input.

#### setWaiverUrl_(`row`)

Find and set waiver url to new member registration.

Waiver is automatically saved by Fillout to folder with id `WAIVER_DRIVE_ID`.

Params:

- `row` (number) - Row index to find and set url. Defaults to the last row in main sheet.

#### findWaiverLink_(`name`)

Find waiver using member's name. Helper function for setWaiverUrl_.

Waiver is automatically saved by Fillout to folder with id `WAIVER_DRIVE_ID`.

Params:

- `name` (string) - The name of member.

#### getExpirationDate_(`semesterCode`)

Get expiration date of member fee from given semester code.

Depends on `MEMBERSHIP_DURATION`.

Params:

- `semesterCode` (string) - The 3-char code representing the semester and year.

Returns:

- (string) - Month and year of expiration e.g. Sep 2025