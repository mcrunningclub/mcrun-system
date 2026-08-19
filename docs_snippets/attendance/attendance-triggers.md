### Triggers.gs

- *function* [`updateWeeklyCalendarTriggers()`](#updateweeklycalendartriggers)
- *function* [`createCalendarTriggersForWeek_()`](#createcalendartriggersforweek_)
- *function* [`cleanUpCalendarTriggersForToday()`](#cleanupcalendartriggersfortoday)
- *function* [`createCalendarTriggersForToday()`](#createcalendartriggersfortoday)
- *function* [`createCalendarTrigger_(event)`](#createcalendartrigger_event)
- *function* [`runSubmissionChecker()`](#runsubmissionchecker)
- *function* [`deleteTrigger_(id, key)`](#deletetrigger_id-key)
- *function* [`deleteExpiredCalendarTriggers_()`](#deleteexpiredcalendartriggers_)

#### updateWeeklyCalendarTriggers()

Adds new events as time-based triggers and removed expired ones

#### createCalendarTriggersForWeek_()

Get events for current week from calendar and create time-based triggers.

#### cleanUpCalendarTriggersForToday()

Get cancelled events for today from calendar and remove their triggers.

#### createCalendarTriggersForToday()

Add new McRUN event(s) from calendar to Apps Script trigger for today.

#### createCalendarTrigger_(event)

Add time-based trigger using event information from Calendar.

Params:

- `event` (CalendarEvent) - Scheduled event as trigger target

#### runSubmissionChecker()

Check if attendance has been submitted and send reminder email if not.

#### deleteTrigger_(id, key)

Deletes a trigger by its unique ID and removes its data from script properties if needed.
This function iterates through all project triggers to find and delete the one
with the specified unique ID. If the trigger is not found, it throws an error.

Params:

- `id` (string) - The unique ID of the trigger to delete.
- `key` (string) - *Optional* The key of trigger's associated script property. Default to null.

#### deleteExpiredCalendarTriggers_()

Removes expired calendar triggers and updates store in Properties.

