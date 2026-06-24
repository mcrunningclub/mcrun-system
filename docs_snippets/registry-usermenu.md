### User Menu.gs

#### logMenuAttempt_(`email`)

Logs user attempting to use custom McRUN menu.

If input empty, then extract email using `getCurrentUserEmail_()`.

Params:

- `email` (string) - Email of active user. Defaults to empty string.


#### onOpen()

Creates custom menu to run frequently used scripts in Google App Script.

Extracting function name using `name` property to allow for refactoring.

Cannot check if user authorized, or custom menu will not be displayed.
This is due to Google App Script limitation.


#### helpUI_()

Displays a help message for the custom McRUN menu.

Accessible to all users.

#### confirmAndRunUserChoice_(`functionName`, `sheetName`, `additionalMsg`, `funcArg`)

Boiler plate function to display custom UI to run scripts.

Verifies if user is authorized before executing script.

Params:

- `functionName` (string) - Name of function to execute.
- `sheetName` (string) - Name of sheet where `functionName` will run.
- `additionaMsg` (string) - Custom message for executing function. Defaults to empty string.
- `funcArg` (string) - Function argument to pass with `functionName`. Defaults to empty string.

Returns:

- (string) - Return value of the executed function.


#### isValidRow_(`row`, `sheet`)

Returns true if row is int and found in given sheet.
Helper function for UI functions for McRUN menu.

Params:

- `row` (integer) - The row number in `sheet` 1-indexed.
- `sheet` (SpreadsheetApp.Sheet) - The sheet to search in.

Returns:

- (boolean) - The input is a number.

#### sortByNameUI_()

Scripts for semester sheet menu items: sort by name

#### onFormSubmitUI_()

Scripts for semester sheet menu items: run submit form function

#### prettifyMainUI_()

Scripts for semester sheet menu items: format sheet

#### encodeLastRowUI_()

Scripts for semester sheet menu items: encode last row

#### findWaiverLinkUI_()

Scripts for semester sheet menu items: ask for row and find waiver for
that member

#### createMemberIDFromInputUI_()

Scripts for semester sheet menu items: ask for text and encode it

#### createMasterUI_()

Scripts for master sheet menu items: overwrite master sheet with a new one

#### prettifyMasterUI_()

Scripts for master sheet menu items: format sheet

#### addLastSubmissionToMasterUI_()

Scripts for master sheet menu items: add last submission from semester sheet

#### sortMasterByEmailUI_()

Scripts for master sheet menu items: sort by email