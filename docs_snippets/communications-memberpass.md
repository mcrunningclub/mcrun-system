### Member Pass.gs

- *function* [`createPassFile_(passInfo)`](#createpassfile_passinfo)
- *function* [`createPassFromRow(row)`](#createpassfromrowrow)
- *function* [`createQrCodeUrl_(memberID)`](#createqrcodeurl_memberid)

#### createPassFile_(passInfo)

Creates new pass from given member information

Add name, date, member ID, and QR code to copy of pass template,
saves in folder with other passes, and get share link

Params:

- `passInfo` (Object) - Member information to include in pass.
                           Should include firstName, lastName, memberId
Returns:

- (string) - Link to created pass

#### createPassFromRow(row = LITERAL_SHEET.getLastRow())

Creates new pass from row in the Literals sheet

Packages row values into an object and calls createPassFile_,
then adds created pass link into Literals sheet

Params:

- `row` (integer) - Row to create pass for. Defaults to last row

Returns:

- (string) - Link to created pass

#### createQrCodeUrl_(memberID)

Creates URL for QR code from given member ID

Uses quickchart.io

Params:

- `memberID` (string) - Member ID

Returns:

- (string) - URL for QR code

