### Formatting.gs

- *function* [`sortLogsByTimestamp()`](#sortlogsbytimestamp)
- *function* [`toTitleCase_(inputString)`](#totitlecase_inputstring)
- *function* [`convertAndFormatStats_(activity)`](#convertandformatstats_activity)
- *function* [`toFixedTruncate_(num, digits)`](#tofixedtruncate_num-digits)
- *function* [`toMinuteSeconds_(t)`](#tominuteseconds_t)

#### sortLogsByTimestamp()

Sorts log sheet by event timestamp ascending.


#### toTitleCase_(inputString)

Formats string to Title Case.

Params:

- `inputString` (string) - String to format.

Returns:

- (string) - String in title case.


#### convertAndFormatStats_(activity)

Change the units in Strava activity to user-friendly values and format them.

Params:

- `activity` (Object) - Strava activity.

Returns:

- (Object) - Converted Strava activity in metric and US imperial values.


#### toFixedTruncate_(num, digits)

Truncate decimal number to given number of digits (for Strava stats).

Replaced .toFixed() to improve accuracy, e.g. 5.9989 -> 5.99 instead of 6.00

Params:

- `num` (float) - The number to truncate
- `digits` (integer) - Number of decimal places to keep

Returns:

- (float) - Truncated number

#### toMinuteSeconds_(t)

Format duration as 'mm:ss' (for Strava stats).

Params:

- `t` (number) - Duration in seconds

Returns:

- (string) - Duration in format mm:ss

