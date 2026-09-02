### Inbox.gs

- *constant* [`ONLINE_LABEL`](#online_label)
- *constant* [`INTERAC_LABEL`](#interac_label)
- *function* [`getGmailLabel_(labelName)`](#getgmaillabel_labelname)
- *function* [`getGmailSearchString_(sender, offset)`](#getgmailsearchstring_sender-offset)
- *function* [`cleanUpMatchedThread_(thread, label)`](#cleanupmatchedthread_thread-label)
- *function* [`matchMemberInPaymentEmail_(searchTerms, emailBody)`](#matchmemberinpaymentemail_searchterms-emailbody)
- *function* [`getMatchingPayments_(sender, maxMatches)`](#getmatchingpayments_sender-maxmatches)
- *function* [`processOnlineThread_(thread, searchTerms)`](#processonlinethread_thread-searchterms)
- *function* [`processInteracThreads_(thread, searchTerms)`](#processinteracthreads_thread-searchterms)
- *function* [`notifyUnidentifiedPayment_(fullName)`](#notifyunidentifiedpayment_fullname)

#### ONLINE_LABEL

Gmail label name for Stripe/Zeffy payment emails

#### INTERAC_LABEL

Gmail label name for Interac payment emails

#### getGmailLabel_(labelName)

Retrieves a Gmail label by its name.

Params:

- `labelName` (string) - The name of the Gmail label to retrieve.

Returns:

- (Gmail.GmailLabel) - The Gmail label object.


#### getGmailSearchString_(sender, offset)

Constructs a Gmail search string to find threads from a specific sender after a given date.

Params:

- `sender` (string) - The email address of the sender.
- `offset` (integer) - The time offset in milliseconds to calculate the minimum date.

Returns:

- (string) - The Gmail search string.


#### cleanUpMatchedThread_(thread, label)

Marks a Gmail thread as read, archives it, and moves it to a specified label.

Params:

- `thread` (Gmail.GmailThread) - The Gmail thread to process.
- `label` (Gmail.GmailLabel) - The Gmail label to apply to the thread.


#### matchMemberInPaymentEmail_(searchTerms, emailBody)

Checks if a member's information is present in the email body.

Params:

- `searchTerms` (string[]) - Search terms for match regex.
- `emailBody` (string) - The body of the payment.

Returns:

- (boolean) - True if a match is found, false otherwise.


#### getMatchingPayments_(sender, maxMatches)

Retrieves the latest payment notification emails from a specific sender.

If no emails are found, retries multiple times with exponential backoff.

Params:

- `sender` (string) - The email address of the sender (e.g., Interac or Zeffy).
- `maxMatches` (integer) - The maximum number of threads to retrieve.

Returns:

- (Gmail.GmailThread[]) - An array of Gmail threads matching the search criteria.


#### processOnlineThread_(thread, searchTerms)

Processes a Gmail thread to find a matching member's payment email.

Params:

- `thread` (Gmail.GmailThread) - The Gmail thread to process.
- `searchTerms` (string[]) - An array of search terms to match against the email body.

Returns:

- (boolean) - True if a match is found in the thread, otherwise false.


#### processInteracThreads_(thread, searchTerms)

Processes Interac e-Transfer threads to find a matching member's payment.
If found, it moves the thread to the specified label, else sends an email notification.

Params:

- `thread` (Gmail.GmailThread) - The Gmail thread to process.
- `searchTerms` (string[]) - An array of search terms to match against the email body.

Returns:

- (boolean) - True if a match is found in the thread, otherwise false.


#### notifyUnidentifiedPayment_(fullName)

Sends a notification email for an unidentified payment to the club's inbox.

Params:

- `fullName` (string) - The full name of the member whose payment could not be identified.


