### Send-Email.gs

- *function* [`logStatus_(messages, logSheet, row)`](#logstatus_messages-logsheet-row)
- *function* [`isEmailSendingAllowed_()`](#isemailsendingallowed_)
- *function* [`checkAndSendPostRunEmail(logSheet, row)`](#checkandsendpostrunemaillogsheet-row)
- *function* [`sendPostRunEmailsForActivity_(recipients, activity)`](#sendpostrunemailsforactivity_recipients-activity)
- *function* [`sendPostRunEmail_(email, memberStats)`](#sendpostrunemail_email-memberstats)
- *function* [`checkAndSendWinBackEmail()`](#checkandsendwinbackemail)
- *function* [`sendWinBackEmail_(email, name)`](#sendwinbackemail_email-name)

#### logStatus_(messages, logSheet, row)

Puts given messages (status of sending email) into the log sheet in the Email Status column

Params:

- `messages` (string[]) - Array of messages to log
- `logSheet` (SpreadsheetApp.Sheet) - Log sheet object
- `row` (integer) - Row to log messages in

#### isEmailSendingAllowed_()

Checks if email sending is allowed according to script properties and throws error if not.

#### checkAndSendPostRunEmail(logSheet, row)

Function to send email to each member updating them on their points

Params:

- `logSheet` (Spreadsheet.sheet) - *Optional* Log sheet object
- `row` (integer) - *Optional* Row with the activity to send email for


#### sendPostRunEmailsForActivity_(recipients, activity)

Sends post run email to all recipients for the specified activity

Params:

- `recipients` (string[]) - Email addresses to send email to
- `activity` (Object) - Activity stats

Returns:

- (string[]) - List of status messages indicating whether each email was sent successfully

#### sendPostRunEmail_(email, memberStats)

Creates post run email from member stats and template,
sends it to given email address

Params:

- `email` (string) - Email address of member

Returns:

- (string) - Confirmation message

#### checkAndSendWinBackEmail()

Automatically triggered to send win back email to members whose
"last run" date is over 2 weeks ago


#### sendWinBackEmail_(email, name)

Creates win back email from member name and template,
sends it to given address

Params:

- `name` (String) - Member's first name
- `email` (String) - Member's email address