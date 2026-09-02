### Menu.gs

- *function* [`onOpen()`](#onopen)
- *function* [`helpUI_()`](#helpui_)
- *function* [`confirmAndRunUserChoice_(functionName, additionalMsg, funcArg)`](#confirmandrunuserchoice_functionname-additionalmsg-funcarg)
- *function* [`requestRowInput_()`](#requestrowinput_)
- *function* [`processRowInput_(userResponse, ui)`](#processrowinput_userresponse-ui)
- *function* [`isValidRow_(row)`](#isvalidrow_row)
- *function* [`addImportTriggerUI_()`](#addimporttriggerui_)
- *function* [`processThisImportUI_()`](#processthisimportui_)
- *function* [`prettifySheetUI_()`](#prettifysheetui_)
- *function* [`verifyPaymentUI_()`](#verifypaymentui_)

#### onOpen()

Creates a custom menu to run frequently used scripts in Google Apps Script.
The menu includes options for importing data, formatting sheets, and verifying payments.
Function names are extracted dynamically using the `name` property to allow for easier refactoring.

#### helpUI_()

Displays a help message for the custom McRUN menu.
The help message provides guidance on how to use the menu options and contact information for assistance.

#### confirmAndRunUserChoice_(functionName, additionalMsg, funcArg)

Displays a confirmation dialog and executes a user-selected function.
This function is used to confirm user actions before executing a specific function.
It dynamically calls the specified function by its name and passes an optional argument.

Params:

- `functionName` (string) - The name of the function to execute.
- `[additionalMsg=""]` (string) - A custom message to display during execution. Defaults to empty string.
- `[funcArg=""]` (string) - An optional argument to pass to the function. Defaults to empty string.

Returns:

- (string) - Return value of the executed function.

#### requestRowInput_()

Prompts the user to input a row number and processes the response.
This function is used to get user input for targeting a specific row in the sheet.

Returns:

- (Object) - An object containing the row number and a message.

#### processRowInput_(userResponse, ui)

Processes the user's row input and returns the result.
This function validates the user's input and determines the row to target.

Params:

- `userResponse` (string) - User response text from `SpreadsheetApp.getUi().prompt`
- `ui` (GoogleAppsScript.Base.Ui) - User interface in Google Sheets

Returns:

- `Result` (Object) - An object containing the parsed row number and a message.
    - `Result.row` (integer) - Parsed integer value of `userResponse`.
    - `Result.msg` (string) - Custom message to display to the user.

#### isValidRow_(row)

Validates if the given row number exists in the registration sheet.

Params:

- `row` (integer) - The row number to validate.

Returns:

- (boolean) - True if the row is valid, otherwise false.

#### addImportTriggerUI_()

Adds a trigger to process a specific row from the import sheet.

#### processThisImportUI_()

Adds a trigger to process a specific row from the import sheet.

#### prettifySheetUI_()

Prettifies the registration sheet by applying formatting rules.

#### verifyPaymentUI_()

Verifies the payment status for a specific row in the registration sheet.

