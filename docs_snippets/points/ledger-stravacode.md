### Strava-Code.gs

- *function* [`findAndStoreStravaActivity(row)`](#findandstorestravaactivityrow)
- *function* [`getExistingStravaActivity_(row)`](#getexistingstravaactivity_row)
- *function* [`getRowLevel_(row)`](#getrowlevel_row)
- *function* [`getStravaStats_(submissionTimestamp, toTimestamp)`](#getstravastats_submissiontimestamp-totimestamp)
- *function* [`getMatchingStravaActivity_(level, activities)`](#getmatchingstravaactivity_level-activities)
- *function* [`removeActivityFromExtra_(activityId)`](#removeactivityfromextra_activityid)
- *function* [`getMatchingActivityFromExtra_(level)`](#getmatchingactivityfromextra_level)
- *function* [`setStravaStats_(row, activity)`](#setstravastats_row-activity)
- *function* [`extractRunStats_(activity, statsMap, offset)`](#extractrunstats_activity-statsmap-offset)

#### findAndStoreStravaActivity(row)

Return Strava activity in `row`. If Strava activity not found in `LOG_SHEET`,
call Strava API using `timestamp` as searching target.

Params:

- `row` (integer) - *Optional* Target row. Defaults to last valid row in `LOG_SHEET`.

Returns:

- (Object) - Strava activity.

#### getExistingStravaActivity_(row)

Verify if Strava activity already stored in log.

Prevents redundant Strava API call.

Params:

- `row` (integer) - *Optional* Target row. Defaults to last valid row in `LOG_SHEET`.

Returns:

- (Object) - Previously stored Strava activity.

#### getRowLevel_(row)

Gets the headrun level for a given row in the log sheet.

Params:

- `row` (integer) - Row of the activity.

Returns:

- (string|null) - Level as string, e.g. "beginner". Null if not found.

#### getStravaStats_(submissionTimestamp, toTimestamp)

Get Strava activity of most recent head run submission.

Params:

- `submissionTimestamp` (Date) - Date representation of headrun timestamp.
- `toTimestamp` (integer) - Max timestamp for map search in seconds.

Returns:

- (Object) - Strava activity with appended mapUrl


#### getMatchingStravaActivity_(level, activities)

Get Strava activity by level for multiple activities recorded at similar datetimes.
Try matching name of activity with level, or by distance otherwise.

This helps sending the correct post-run email stats to attendee's level.

Params:

- `level` (string) - Level of headrun (e.g. 'easy', 'intermediate').
- `activities` (Object[]) - Array of Strava activities occurring at similar times.

Returns:

- (Object|null) - Best-matching Strava activity, or null if none.

Example:

```js
const activities = [{name: 'Headrun Easy', distance: 7km}, {name: 'Morning run - Intermediate', distance: 3km}];
console.log(getActivityByLevel('Easy', activities))   // {name: 'Headrun Easy', distance: 7km}
```

#### removeActivityFromExtra_(activityId)

Remove a specific Strava activity from the extra activities stored for a level.

Params:

- `activityId` (number) - The Strava activity ID to remove.


#### getMatchingActivityFromExtra_(level)

Retrieve extra Strava activities saved from previous API call.

Params:

- `level` (string) - Level of headrun (e.g. 'easy', 'intermediate').

Returns:

- (Object[]) - Extra Strava activities, or empty array if none found.


#### setStravaStats_(row, activity)

Puts stats from specified Strava activity into the log sheet.

Params:

- `row` (number) - Row to save the activity in.
- `activity` (Object) - Strava activity to save stats from.

#### extractRunStats_(activity, statsMap, offset)

Extract target run stats from Strava activity.

Params:

- `activity` (object) - A Strava object `SummaryActivity` or `ClubActivity`.
- `offset` (number) - *Optional* The amount to subtract from the column number. Default to 0.

Returns:

- (object) - Extracted stats from `activity`.


