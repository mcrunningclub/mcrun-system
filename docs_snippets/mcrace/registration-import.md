### Import.gs

- *function* [`appendToImport(reg)`](#appendtoimportreg)
- *function* [`processThisImport(targetRow)`](#processthisimporttargetrow)
- *function* [`onChange(e)`](#onchangee)
- *function* [`doPost(e)`](#doposte)

#### appendToImport(reg)

Appends a registration object to the import sheet.

Params:

- `reg` (string) - The registration data in string format.

Returns:

- (integer) - The row number where the registration was appended.


#### processThisImport(targetRow)

Processes the last imported registration from the import sheet.


#### onChange(e)

Triggered when a change occurs in the spreadsheet.

Params:

- `e` (GoogleAppsScript.Events.SheetsOnChange) - The event object containing details of the change.


#### doPost(e)

Handles HTTP POST requests to process new registrations.

Params:

- `e` (GoogleAppsScript.Events.DoPost) - The event object containing POST data.

Returns:

- (GoogleAppsScript.Content.TextOutput) - A text output with the result of the operation.


