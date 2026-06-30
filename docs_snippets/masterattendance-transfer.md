### Transfer.gs
- **onChange(e)**: Triggered on sheet changes; handles new submissions, exports, and maintenance formatting.
- **transferToSemesterSheet(row)**: Transfers the latest submission to the semester attendance sheet and marks it as exported.
- **prepareAttendanceSubmission(values)**: Converts a row of attendance data into a JSON-formatted string for export.


<br>
<!-- 
    🔴 Transfer.gs
-->

### # <big> Transfer.gs </big>
- [`onChange(e)`](#onchangee) → Main trigger handler for sheet edits/changes
- [`transferToSemesterSheet(row)`](#transfertosemestersheetrow) → Transfers the latest submission to the semester sheet

---

#### ## <big> onChange(e) </big>

Handles all sheet onChange events. Transfers new submissions to the semester sheet and triggers formatting.

```js
function onChange(e) {
  // Called automatically by trigger
}
```

| Name | Type   | Description                |
|------|--------|----------------------------|
| e    | Object | Sheets event object         |

**Output:** None (side effects: transfers data, runs formatting)

**Pitfalls:** Only processes EDIT events and correct sheet ID; errors logged.

---

#### ## <big> transferToSemesterSheet(row) </big>

Transfers the latest submission (or specified row) to the semester attendance sheet, marking it as exported.

```js
transferToSemesterSheet(5);
```

| Name | Type    | Description                                    |
|------|---------|------------------------------------------------|
| row  | Integer | Row to transfer (default: last submission)     |

**Output:** None

**Pitfalls:** Requires valid sheet IDs and permissions; falls back to direct access if library fails.
