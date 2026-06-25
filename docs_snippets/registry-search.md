### Search.gs

#### getIndexStore()

Retrieves index store from script properties and parses it.

If store is not found, call function to create it.

Returns:

- (Object) - Mapping letters to the row with the first occurence of an email starting with that letter

#### setIndexStore()

Builds and sets index store as a script property.

Returns:

- (Object) - Mapping letters to the row with the first occurence of an email starting with that letter

#### buildIndexStore_()

Builds an index store mapping the first letter of a key (i.e. email) to 
its first occurrence index in the master sheet. e.g { 'a': 2, 'b' : 21, ... }

#### findMemberByEmail(email, sheet)

Searches for member entry by email in `sheet` by binary search.
If unsuccessful, searches again via top-to-bottom iteration.

Returns row index of `email` in GSheet (1-indexed), or null if not found.

Params:

- `email` (string) - The email address to search for in `sheet`.
- `sheet` (SpreadsheetApp.Sheet) The sheet to search in.

Returns:

- (number|null) - Returns the 1-indexed row number where the email is found, or `null` if the email is not found.

#### findMemberWithStore(email, store)

Finds a member in the master sheet by setting a stricter bound using an
index store of each letter, searching with binary search.

Returns row index of `email` in GSheet (1-indexed), or null if not found.

Params:

- `email` (string) - The email address to search for in `sheet`.
- `store` (Object) - Object mapping first letter to starting index, e.g. { 'a': 1, 'b': 21, ... }. Defaults to result of getIndexStore().

Returns:

- (number|null) - Returns the 1-indexed row number where the email is found, or `null` if the email is not found.

#### findMemberByIteration(email, sheet, startRow, endRow)

Searches for member entry by email in `sheet` using iteration.
Returns row index of `email` in GSheet (1-indexed), or null if not found.

See faster binary search function `findMemberByBinarySearch()`.

Params:

 - `email` (string) - The email address to search for in `sheet`.
 - `sheet` (SpreadsheetApp.Sheet) - The sheet to search in.
 - `startRow` (number) - The starting row index for the search (1-indexed). Defaults to 2 (the second row) to avoid the header row.
 - `endRow` (number) - The ending row index for the search. Defaults to the last row in the sheet.

Returns:

 - (number|null) - Returns the 1-indexed row number where the email is found, 
                       or `null` if the email is not found.

#### findMemberByBinarySearch(email, sheet, startRow, endRow)

Recursive function to search for entry by email in `sheet` using binary search.
Returns row index of `email` in GSheet (1-indexed), or null if not found.

Previously `findSubmissionFromEmail` in `Master Scripts.gs`.

Params:

- `email` (string) - The email address to search for in `sheet`.
- `sheet` (SpreadsheetApp.Sheet) - The sheet to search in.
- `startRow` (number) - The starting row index for the search (1-indexed). Defaults to 2 (the second row) to avoid the header row.
- `endRow`(number) - The ending row index for the search. Defaults to the last row in the sheet.

Returns:

- (number|null) - Returns the 1-indexed row number where the email is found, or `null` if the email is not found.

#### testRuntime()

Testing speed of different search functions.