### Member Info.gs

- *function* [`createNewMemberCommunications(memberObj)`](#createnewmembercommunicationsmemberobj)
- *function* [`createNewMemberLiteral_(memberObj)`](#createnewmemberliteral_memberobj)
- *function* [`logPaymentStatus_(statusObj)`](#logpaymentstatus_statusobj)
- *function* [`logEmailStatus_(message, row)`](#logemailstatus_message-row)

#### createNewMemberCommunications(memberObj)

Workflow for when new member registers

Add new member's information to Literals sheet,
create a pass, save pass information, and send welcome email

Params:


- `memberObj` (Object) - Object containing member informations

#### createNewMemberLiteral_(memberObj)

Appends a member object as a new row in the sheet, mapping fields to correct columns.

Params:

- `memberData` (Object) - The member object (e.g., { email: '...', firstName : '...' })
- `literalsSheet` (SpreadsheetApp.Sheet) - The Literals sheet object

Returns:

- (number) - The row index of the newly appended row

#### logPaymentStatus_(statusObj)

Appends a new log to the Payment Logs sheet

Params:

- `statusObj` (Object) - Object containing payment information
                           Should include timestamp, email, feeStatus

#### logEmailStatus_(message, row)

Updates the Email Status column in the literals sheet with a new message

Includes date and time of the message

Params:

- `message` (string) - Message to log
- `row` (number) - Row to log email status for

