### Import.gs

- *function* [`processImportFromApp(importObj)`](#processimportfromappimportobj)
- *function* [`transferLastImportToSemester()`](#transferlastimporttosemester)
- *function* [`transferImportToSemester_(row)`](#transferimporttosemester_row)
- *function* [`toggleIsImported_(row, colIndex)`](#toggleisimported_row-colindex)
- *function* [`timestampExistsInSemester_(timestampToCompare, numOfRow)`](#timestampexistsinsemester_timestamptocompare-numofrow)
- *function* [`copyObjToSemesterSheet_(attendanceJSON, row)`](#copyobjtosemestersheet_attendancejson-row)
- *function* [`packageAttendance_(keyArr, valArr)`](#packageattendance_keyarr-valarr)

#### processImportFromApp(importObj)

Process latest imported attendance submission via McRUN app.

Params:

- `importObj` (Object) - Data to process (as JSON-formatted string?)


#### transferLastImportToSemester()

Transfers the last imported attendance submission to the semester sheet.

#### transferImportToSemester_(row)

Copies row from import sheet to semester attendance sheet if it doesn't already exist.

Params:

- `row` (number) - Number of the row to transfer

#### toggleIsImported_(row, colIndex)

Changes value of isImported column in import sheet to True.
If column number is not provided, finds it using sheet header row.

Params:

- `row` (number) - Number of row to change.
- `colIndex` (number) - *(Optional)* Number of column corresponding to isImported column. Defaults to 5

#### timestampExistsInSemester_(timestampToCompare, numOfRow)

Check is submission already added by comparing timestamps.

Params:

- `timestampToCompare` (string) - Input timestamp
- `numOfRow` (integer) - *Optional* Number of rows to check from the bottom.
                                 Defaults to 5.

Returns:

- (Boolean) - Returns true if found in attendance sheet.


#### copyObjToSemesterSheet_(attendanceJSON, row)

Transfer new attendance submission from `Import` to semester sheet.

Params:

- `attendanceJSON` (Object<JSON>) - Attendance information as JSON object.
- `row` (integer) - *Optional* Target row in `Attendance_Sheet`. Defaults to last row.

Returns:

- (integer) - Latest row in `Attendance_Sheet`.


#### packageAttendance_(keyArr, valArr)

Create JSON-formatted string of key-value pairs for attendance submission.

Params:

- `keyArr` (string[]) - Array of keys storing header row values.
- `valArr` (string[]) - Values of attendance submission to map.

Returns:

- (string) - A JSON string of attendance submission as key-value pairs.


