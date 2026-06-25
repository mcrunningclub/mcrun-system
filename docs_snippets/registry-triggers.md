### Triggers.gs

#### createNewFeeTrigger_(row, feeDetails)

Create time-based trigger to check fee payment.


#### runFeeChecker()

Handler function for time-based trigger to check fee payment.

Includes helper functions to check for payment, increment the
number of times checked, and clean up/delete the trigger.

No arguments allowed since trigger does not accept any.
Workaround: store member details in script properties.