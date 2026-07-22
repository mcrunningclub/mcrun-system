### Data-Formatting.gs

- *function* [`getLastSubmission_()`](#getlastsubmission_)
- *function* [`formatNamesInRange_(cols, startRow, numRows)`](#formatnamesinrange_cols-startrow-numrows)
- *function* [`formatNamesInLastSubmission()`](#formatnamesinlastsubmission)

#### getLastSubmission_()

Finds the row index of the last non-empty submission in the master attendance sheet.
This function iterates backwards through the TIMESTAMP column to find the last row
with a non-empty value, avoiding issues with getLastRow() returning empty rows.

Returns:

- (number) - The 1-based index of the last non-empty row in the sheet.


#### formatNamesInRange_(cols, startRow, numRows)

Formats headrunner names into uniform view, separated by newline.

Params:

- `cols` (Array<Integer>) - The column(s) with names to format.
- `startRow` (integer) - The row to start formatting at. (1-indexed).
                            Defaults to the last row in the sheet.
- `numRows` (integer) - Number of rows to format from `startRow`. Defaults to 1.

Examples:

```javascript
// Format names in last row for ATTENDEES.
formatHeadRunnerInRow([ATTENDEES_COL]);
```
```javascript
// Format names in row `7` in TIMESTAMP and ATTENDEES.
const targetCols = [HEADRUNNER_COL, ATTENDEES_COL]
const rowToFormat = 7;
formatHeadRunnerInRow(targetCols, rowToFormat);
```
```javascript
// Format names from row `3` to `9` in TIMESTAMP.
const targetCols = [HEADRUNNER_COL]
const startRow = 3;
const numRow = 9 - startRow;
formatHeadRunnerInRow(targetCols, startRow, numRow);
```

#### formatNamesInLastSubmission()

Formats all relevant name columns in the last submission row.
Calls formatNamesInRange_ for HEADRUNNERS and ATTENDEES columns.