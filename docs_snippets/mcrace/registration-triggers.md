### Triggers.gs

- *constant* [`TRIGGER_FUNC`](#trigger_func)
- *constant* [`TRIGGER_BASE_ID`](#trigger_base_id)
- *constant* [`FEE_MAX_CHECKS`](#fee_max_checks)
- *constant* [`TRIGGER_FREQUENCY`](#trigger_frequency)
- *function* [`createNewFeeTrigger_(row, feeDetails)`](#createnewfeetrigger_row-feedetails)
- *function* [`runFeeChecker()`](#runfeechecker)
- *function* [`isPaymentFound(memberRow)`](#ispaymentfoundmemberrow)
- *function* [`incrementTries(key, triggerData)`](#incrementtrieskey-triggerdata)
- *function* [`checkThisFeeAgain(feeDetails, rowNum)`](#checkthisfeeagainfeedetails-rownum)
- *function* [`cleanUpTrigger(key, triggerId)`](#cleanuptriggerkey-triggerid)
- *function* [`deleteTriggerById(triggerId)`](#deletetriggerbyidtriggerid)

#### TRIGGER_FUNC

Function to run when trigger is called

#### TRIGGER_BASE_ID

Name to include in all payment check triggers

#### FEE_MAX_CHECKS

Maximum number of attempts to find payment before trigger is deleted

#### TRIGGER_FREQUENCY

Time between trigger calls (in minutes)

#### createNewFeeTrigger_(row, feeDetails)

Creates a new time-based trigger to check fee payment for a specific member.

The trigger runs periodically and stores the member's details in script properties.
If the payment is not found after a maximum number of attempts, an email notification is sent.

Params:

- `row` (number) - The row number in the `Registration` sheet for the member.
- `feeDetails` (Object) - The member's payment details.
    - `feeDetails.fullName` (string) - The member's full name.
    - `feeDetails.email` (string) - The member's email address.
    - `feeDetails.paymentMethod` (string) - The payment method used by the member.


#### runFeeChecker()

Handler function for time-based triggers to check fee payment.

This function processes all active triggers, checking if the payment has been confirmed.
If the payment is found, the trigger is cleaned up. If the maximum number of attempts is reached,
an email notification is sent to notify about the unidentified payment.


#### isPaymentFound(memberRow)

Checks if the payment has already been confirmed for a member.

Params:

- `memberRow` (integer) - The row number in the `Registration` sheet for the member.

Returns:

- (boolean) - True if the payment is confirmed, otherwise false.

#### incrementTries(key, triggerData)

Increments the number of attempts for a trigger and updates the script properties.

Params:

- `key` (string) - The key for the trigger in script properties.
- `triggerData` (Object) - The trigger data to update.

#### checkThisFeeAgain(feeDetails, rowNum)

Checks the payment status for a member again.

Params:

- `feeDetails` (Object) - The member's payment details.
- `rowNum` (number) - The row number in GSheet.

#### cleanUpTrigger(key, triggerId)

Cleans up a trigger by deleting it and removing its data from script properties.

Params:

- `key` (string) - The key for the trigger in script properties.
- `triggerId` (string) - The unique ID of the trigger to delete.

#### deleteTriggerById(triggerId)

Deletes a trigger by its unique ID.

Params:

- `triggerId` (string) - The unique ID of the trigger to delete.

