### Data-Formatting.gs
- **getLastSubmission_()**: Returns the last non-empty row index in the master attendance sheet.
- **formatNamesInRow_(targetCols, startRow, numRow)**: Formats names in specified columns and rows, separating names by newlines.
- **formatAllNamesInRow()**: Formats all relevant name columns (headrunners and attendees) in the last submission row.



<!-- 
    🔴 Data-Formatting.gs
-->

### # <big> Data-Formatting.gs </big>
- [`getLastSubmission()`](#getlastsubmission) → Gets the last non-empty row in the sheet
- [`formatNamesInRow(targetCols, startRow, numRow)`](#formatnamesinrowtargetcols-startrow-numrow) → Formats and normalizes names in specific columns/rows


#### ## <big> getLastSubmission() </big>

Finds the row index of the last non-empty submission (by timestamp) in the master attendance sheet.

```js
const idx = getLastSubmission();
```

| Name | Type | Description |
|------|------|-------------|
| —    | —    | No parameters |

**Output:** Number (1-based index of last non-empty row)

**Pitfalls:** If all rows are empty, may return 0 or error.

---

#### ## <big> formatNamesInRow(targetCols, startRow, numRow) </big>

Formats headrunner or attendee names in the specified columns for a given row or range, normalizing apostrophes and splitting by commas/newline.

```js
formatNamesInRow([2, 7], 7, 1);
```

| Name       | Type          | Description                                      |
|------------|---------------|--------------------------------------------------|
| targetCols | Array<Integer>| Columns to format                                |
| startRow   | Integer       | Row to start formatting (default: last row)      |
| numRow     | Integer       | Number of rows to format (default: 1)            |

**Output:** None (in-place formatting in sheet)

**Pitfalls:** Out-of-range columns/rows may cause errors.
