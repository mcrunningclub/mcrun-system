### Payment.gs

- *constant* [`CLUB_EMAIL`](#club_email)
- *constant* [`INTERNAL_EMAIL`](#internal_email)
- *constant* [`ZEFFY_EMAIL`](#zeffy_email)
- *constant* [`INTERAC_EMAIL`](#interac_email)
- *constant* [`STRIPE_EMAIL`](#stripe_email)
- *function* [`checkAndSetPayment(row, feeDetails)`](#checkandsetpaymentrow-feedetails)
- *function* [`checkPayment_({ fName, lName, email, paymentMethod })`](#checkpayment_)
- *function* [`checkOnlinePayment_(member)`](#checkonlinepayment_member)
- *function* [`checkInteracPayment_(member)`](#checkinteracpayment_member)
- *function* [`setFeePaid_(row)`](#setfeepaid_row)
- *function* [`createSearchTerms_(member)`](#createsearchterms_member)

#### CLUB_EMAIL

Club email address

#### INTERNAL_EMAIL

Club internal email address

#### ZEFFY_EMAIL

Email address that Zeffy payment emails are sent from

#### INTERAC_EMAIL

Email address that Interac payment emails are sent from

#### STRIPE_EMAIL

Email address that Stripe payment emails are sent from

#### checkAndSetPayment(row, feeDetails)

Verifies and sets the payment status for a member in the `Registration` sheet.

If the payment is found, marks the payment as confirmed and sets the payment date.
If not found, schedules a trigger to recheck the inbox and sends a notification if necessary.

Params:

- `[row=getLastRowInReg_()]` (integer) - The row to update in the `Registration` sheet.
- `[feeDetails=extractFromSheet_()]` (Object) - The member's payment details.

Returns:

- (boolean) - True if the payment is found, otherwise false.


#### checkPayment_(\{ fName, lName, email, paymentMethod \}) {#checkpayment_}

Checks the payment status for a member based on their payment method.

If the payment method includes "CC", it checks online payments (e.g., Zeffy or Stripe).
If the payment method includes "Interac", it checks Interac payments.

Params:

- `member` (Member) - The member's information.

Returns:

- (boolean) - True if the payment is found, otherwise false.


#### checkOnlinePayment_(member)

Checks for online payments (e.g., Zeffy or Stripe) for a member.

Searches for matching payment emails using the member's information.

Params:

- `member` (Member) - The member's information.

Returns:

- (boolean) - True if a matching payment email is found, otherwise false.


#### checkInteracPayment_(member)

Checks for online payments (e.g., Zeffy or Stripe) for a member.

Searches for matching payment emails using the member's information.

Params:

- `member` (Member) - The member's information.

Returns:

- (boolean) - True if a matching payment email is found, otherwise false.


#### setFeePaid_(row)

Updates a member's fee information in the registration sheet.

Marks the payment as confirmed and sets the payment date to the current date.

Params:

- `row` (integer) - The row index to update in the registration sheet.


#### createSearchTerms_(member)

Creates search terms for regex matching using a member's information.

Handles optional hyphens/spaces in last names, and removes diacritics for better matching.
Improves matching accuracy in `matchMemberInPaymentEmail`.

Params:

- `member` (Member) - The member's information.

Returns:

- (string[]) - An array of search terms for regex matching.


