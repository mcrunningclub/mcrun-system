### Send Email.gs

- *function* [`sendWelcomeEmailInRow(row)`](#sendwelcomeemailinrowrow)
- *function* [`sendWelcomeEmail_(memberInformation)`](#sendwelcomeemail_memberinformation)
- *function* [`sendUpdatedPass_(memberInformation)`](#sendupdatedpass_memberinformation)
- *function* [`quickPassUpdate(row)`](#quickpassupdaterow)
- *function* [`triggerUpdateAndSendPass(row)`](#triggerupdateandsendpassrow)
- *function* [`updateAndSendPass_(statusObj, isLogged)`](#updateandsendpass_statusobj-islogged)
- *function* [`sendEmail_(memberInformation, draftSubject)`](#sendemail_memberinformation-draftsubject)

#### sendWelcomeEmailInRow(row)

Sends email using member information in `row`.
Logs email status in column `EMAIL_STATUS`

Params:

- `row` (integer) - Row to target for information

#### sendWelcomeEmail_(memberInformation)

Sends welcome email to member using template and member info.

Gets member information and image blobs stored in script properties,
populates template, and sends email.

Params:

- `memberInformation` (Object) - Object containing member information from Literals

Returns:

- (string) - "Successfully sent!" if email sent, otherwise error message

#### sendUpdatedPass_(memberInformation)

Sends updated pass email to member using template and member info.

Gets member information and image blobs stored in script properties,
populates template, sends email, and log to console if successful or not.

Params:

- `memberInformation` (Object) - Object containing member information from Literals

#### quickPassUpdate(row)

Update pass using member information from given row in Literals sheet,
and sends an email with the new pass.

Params:

- `row` (number) - Row of member to update pass for. Defaults to 15 (dunno why)

#### triggerUpdateAndSendPass(row)

Sends new pass to member from given row in Payment Logs sheet.

Params:

- `row` (number) - Row of member to update pass for. Defaults to 2 (???)

#### updateAndSendPass_(statusObj, isLogged)

Sends pass given payment status object.

Finds existing member data from literals sheet, deletes old pass
and creates new one, and sends email to member

Params:

- `statusObj` (Object) - Payment status, including 'email' and 'fee status'
- `isLogged` (boolean) - Whether the status has been added to Payment Logs sheet.
                             Determines whether to add it or not. Default false.

#### sendEmail_(memberInformation, draftSubject)

Sends email from template in drafts using member information.

Finds draft using subject and gets template from it, then fills
in member information and creates a new email to send.
Throws error and logs it in console if error occurs during sending. 

Params:

- `memberInformation` (Object) - Information to populate email draft
- `draftSubject` (string) - Subject line of the email draft to use as template

