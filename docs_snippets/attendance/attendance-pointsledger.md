### Points-Ledger.gs

- *function* [`appendAttendeeEmails_(row, registered, unregistered)`](#appendattendeeemails_row-registered-unregistered)
- *function* [`transferSubmissionToLedger(row)`](#transfersubmissiontoledgerrow)
- *function* [`packageSubmissionForLedger_(row)`](#packagesubmissionforledger_row)
- *function* [`sendNewSubmission_(submissionArr)`](#sendnewsubmission_submissionarr)
- *function* [`setNewStravaTrigger_(ledgerRow)`](#setnewstravatrigger_ledgerrow)
- *function* [`executePointsLedgerFunction_(funcName, args)`](#executepointsledgerfunction_funcname-args)

#### appendAttendeeEmails_(row, registered, unregistered)

Appends attendee emails to names for each run level in specified
row of attendance (if found). 

Params:

- `row` (integer) - Row in `ATTENDANCE_SHEET` to append email.
- `registered` (string[][]) - All search keys of registered members (sorted) and emails.
- `unregistered` (string[][]) - All unregistered attendees grouped by levels.

#### transferSubmissionToLedger(row)

Transfers a submission from the attendance sheet to the Points Ledger.
Packages all non-empty submission levels into a 2D array and sends it to the ledger.
If the transfer fails, it retries using `openByUrl`. Also sets a trigger to search for
the Strava activity.

Params:

- `row` (integer) - *Optional* The row in the attendance sheet to transfer. Defaults to last row.

#### packageSubmissionForLedger_(row)

Packages a row from the attendance sheet for transfer to the Points Ledger.

Params:

- `row` (integer) - The row in the attendance sheet to package.

Returns:

- (Array<Array<string>>) - A 2D array of packaged event data.

#### sendNewSubmission_(submissionArr)

Sends a new submission to the Points Ledger using the library function.

Params:

- `submissionArr` (Array<Array<string>>) - The submission data to send.

Returns:

- (integer) - The row index in the Points Ledger where the submission was logged.

#### setNewStravaTrigger_(ledgerRow)

Sets a new trigger to find and store Strava activity for a row in the Points Ledger.

Params:

- `ledgerRow` (integer) - The row index in the Points Ledger to set the trigger for.

#### executePointsLedgerFunction_(funcName, args)

Executes a function from the Points Ledger library with the given arguments.

Params:

- `funcName` (string) - The name of the function to execute.
- `args` (Array) - The arguments to pass to the function.

Returns:

- (*) - The return value of the executed function.

