### Member Fee.gs

#### getPaymentItem_(`cell`)

Retrieves the payment item from the "Internal Fee Collection" sheet.

Params:

- `cell` (string) - The cell reference (e.g., 'A3') to retrieve the payment item from.

Returns:

- (string) - The payment item value (e.g. "(Online Payment)") from the specified cell.

#### getGmailLabel_(`labelName`)

Retrieves a Gmail label by its name.

This function fetches a Gmail label object based on the provided label name.

Params:

 - `labelName` (string) - The name of the Gmail label to retrieve.

Returns:

- (GmailApp.GmailLabel) - The Gmail label object corresponding to the provided name.

#### checkPaymentForSemester(`row`)

Verify if member has paid fee using notification email sent by Interac, Stripe or Zeffy

Update member's information in the semester sheet as required.

Params:

 - `row` (number) - index of member. Defaults to last row.

#### isPaid_(`row`, `feeDetails`)'

Helper function for Stripe/Zeffy and Interac cases

Calls necessary function to check whether payment has been
made depending on type of payment

Params:

- `row` (number) - Row of the member to check payment for
- `feeDetails` (struct) - struct of fee information from sheet??

Returns:

- (bool) - Whether member's fee has been paid or not

#### setFeeDetailsInSemester_(`row`, `collectedBy`)

Updates member's fee information.

Params:

- `row` (number) - The index to enter information.
- `collectedBy` (string) - The list item from `Internal Fee Collection` to put in 'Collection Person' col.

####  setFeeDetailsInMaster_(`row`, `paymentMethod`, `collectedBy`, `date`)

Updates member's fee information in the master sheet.

Params:

- `row` (number) - The index of the row with member's information.
- `paymentMethod` (string) - How the fee was paid
- `collectedBy` (string) - How the fee was collected
- `date` (string) - Date of collection. Defaults to null (will be set to current date)

#### updateMasterPayment_(`email`, `paymentMethod`, `row`)

Updates fee payment information in master sheet given member's email.

Params:

- `email` (string) - Email address of member to update info for.
- `paymentMethod` (string) - How fee was paid
- `row` (number) - Row of member (if known). Defaults to null.

#### checkExistingPaymentInSemester()

For members whose fee is not paid in the master sheet, check whether
they have paid the fee in the semester sheet. Update master sheet if necessary.

Loop through every member in the master sheet. If their fee status is not paid,
check whether registration date is within the last semester and whether the semester
sheet contains their payment. If found, add to master sheet. If not found, add to
list of "unpaid" emails that is logged in console.

#### getMatchingEmails_(`sender`, `maxMatches`, `subject`)

Return latest emails of payment notification.

If not found, wait multiple times for email to arrive in McRUN inbox. Must use club email.

Params:

- `sender` (string) - Email of sender (Interac, Stripe or Zeffy).
- `maxMatches` (integer) - Number of max tries.
- `subject` (string) - Email subject to filter by. Defaults to empty string

Returns:

- (GmailThread[]) - Gmail threads matching the search

#### createGmailSearchString_(`sender`, `subject`)

Create search string given sender and optional subject

In the form (from:sender, starting:yesterday, in:inbox, \[subject:partial-email-match\])

#### cleanUpMatchedThread_(`thread`, `label`)

Marks a fully processed thread as read, archives it, and moves it to the `label` folder.

#### searchInEmail_(`searchTerms`, `emailBody`)

Checks if a member's information is present in the email body.

Params:

- `searchTerms` (string[]) - Search terms for match regex.
- `emailBody` (string) - The body of the email.

Returns:

- (boolean) - True if a match is found, false otherwise.

#### createSearchTerms_(`member`)

Creates search terms for regex matching using a member's information.

Handles optional hyphens/spaces in last names, and removes diacritics for better matching.
Improves matching accuracy in `searchInEmail_`.

Params:

- member (Object) - Member information. Contains attributes member.firstname, member.lastname, member.email (if applicable), member.interacRef (if applicable).

Returns:

- (string[]) - An array of search terms for regex matching.

#### paymentMethodToItem_(`paymentMethod`)

Get payment item eg. "(Online Payment)" from payment method string.

Gets standardized item from list in Internal Memberships Collected spreadsheet based on keywords in payment method. 

#### setFeeWaived_(`row`)

Sets fee status as waived in member registration.

Params:

- `row` (integer) - The index to enter information.

#### setOnlinePaid_(`row`)

Sets fee status as paid online in member registration.

Params:

- `row` (integer) - The index to enter information.

#### checkAndSetOnlinePayment_(`row`, `member`)

Verify Stripe/Zeffy payment transaction for latest registration.

Must have the member submission in last row of main sheet to work.

- `row` (integer) - Member's row index in GSheet.
- `member` (Object) - Member information.
    - `member.firstName` (string) - First name of member.
    - `member.lastName` (string) - Last name of member.
    - `member.email` (string) - Email of member.

Returns:

- (boolean) - True if payment was found in emails.

#### processOnlineThread_(`thread`, `searchTerms`)

Process a single Gmail thread to find a matching member's payment.

#### setInteracPaid_(`row`)

Sets fee status as paid through Interac in member registration.

Params:

- `row` (integer) - The index to enter information.

#### checkAndSetInteracRef_(`row`, `member`)

Look for new emails from Interac starting yesterday (cannot search from same day) and extract ref number.

Send notification email to McRUN if no ref number found.

#### extractInteracRef_(`emailBody`)

Extract Interac e-Transfer reference string.

Params:

- `emailBody` (string) - The body of the Interac e-Transfer email.

Returns:

 - (string) - Returns extracted Interac Ref from `emailBody`, otherwise empty string.

#### notifyUnidentifiedInteracRef_(`references`)

Sends an email to the club with a list of Interac references that have not
been matched to a member registration.


#### notifyUnidentifiedPayment_(`name`)

Sends an email to the club with member whose payment emails has not been found.