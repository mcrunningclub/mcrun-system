### Formatting.gs

- *function* [`removeDiacritics_(str)`](#removediacritics_str)
- *function* [`formatSpecificColumns()`](#formatspecificcolumns)
- *function* [`addMissingCheckboxes_(sheet)`](#addmissingcheckboxes_sheet)
- *function* [`safeJSONParse(raw)`](#safejsonparseraw)

#### removeDiacritics_(str)

Removes diacritics (accents) from a given string.

Params:

- `str` (string) - The string to normalize and strip of diacritics.

Returns:

- (string) - The normalized string without diacritics.


#### formatSpecificColumns()

Formats the registration sheet by:
1. Freezing panes
2. Setting text wrapping
3. Setting vertical alignment
4. Setting number formatting
5. Adding checkboxes to non-empty rows
6. Updating banding by increasing range


#### addMissingCheckboxes_(sheet)

Adds checkboxes to the `paymentConfirmed` column for all non-empty rows.

Params:

- `[sheet=GET_REGISTRATION_SHEET_()]` (SpreadsheetApp.Sheet) - The sheet to add checkboxes to. Defaults to the registration sheet.

#### safeJSONParse(raw)

Sanitizes JSON-like string to prevent `SyntaxError`

Params:

- `raw` (string) - The string to safely parse.

Returns:

- (JSON) - Legal JSON object


