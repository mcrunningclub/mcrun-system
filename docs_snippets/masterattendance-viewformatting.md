### View-Formatting.gs
- **sortAttendanceForm()**: Sorts the master attendance sheet by timestamp (ascending).
- **prettifySheet()**: Applies formatting to the master attendance sheet for improved readability.
- **formatSpecificColumns_()**: Applies font, alignment, number format, and column width settings to key columns.


<br>
<!-- 
    🔴 View-Formatting.gs
-->

### # <big> View-Formatting.gs </big>
- [`sortAttendanceForm()`](#sortattendanceform) → Sorts sheet by timestamp ascending
- [`prettifySheet()`](#prettifysheet) → Calls column formatting function
- [`formatSpecificColumns()`](#formatspecificcolumns) → Applies formatting to key columns

---

#### ## <big> sortAttendanceForm() </big>

Sorts all rows (except the header) by the Timestamp column in ascending order.

```js
sortAttendanceForm();
```

| Name | Type | Description |
|------|------|-------------|
| —    | —    | No parameters |

**Output:** None (sorts in-place)

**Pitfalls:** Assumes Timestamp is in COLUMN_MAP.TIMESTAMP.

---

#### ## <big> prettifySheet() </big>

Applies master formatting to the sheet for better readability.

```js
prettifySheet();
```

**Output:** None

---

#### ## <big> formatSpecificColumns() </big>

Applies font, size, bold, italics, number format, alignment, and checkboxes to specific columns.

```js
formatSpecificColumns();
```

**Output:** None

**Pitfalls:** Hardcoded ranges; will fail if columns/names change.
