### Triggers.gs

- *function* [`doGet(e)`](#dogete)
- *function* [`createStravaTrigger_(row)`](#createstravatrigger_row)
- *function* [`checkForStravaActivities()`](#checkforstravaactivities)
- *function* [`cleanUpTrigger(propertyKey)`](#cleanuptriggerpropertykey)
- *function* [`deleteTriggerById_(id)`](#deletetriggerbyid_id)
- *function* [`deleteAllStravaTriggers()`](#deleteallstravatriggers)
- *function* [`alertTriggerNotFound_(triggerData)`](#alerttriggernotfound_triggerdata)
- *function* [`alertStravaActivityNotFound_(rowNumber, tries)`](#alertstravaactivitynotfound_rownumber-tries)

#### doGet(e)

Handler for GET events sent to web app deployment of this script

Checks for authorization, then sets trigger to check for Strava activity
for the row specified in the request.

Params:

- `e` (Object) - GET request object, should contain keys 'key' and 'rowNum

Returns:

- (TextOutput) - Message indicating status of request

#### createStravaTrigger_(row)

Creates a trigger to check for Strava activity for a given row, and stores its information
in script properties. The property key includes the row number and its values contains the 
number of tries, trigger ID, and row number.

Params:

- `row` (integer) - *Optional* Row to check for activity for. Defaults to last row

#### checkForStravaActivities()

Function called by Strava triggers. Checks for Strava activity for all the rows that currently
have active triggers according to script properties, and increments the number of runs for 
each one. If max number of tries reached, deletes the trigger.

#### cleanUpTrigger(propertyKey)

Remove trigger and its property in script properties 

Params:

- `propertyKey` (string) - Key of the script property corresponding to the trigger to delete

#### deleteTriggerById_(id)

Delete a trigger given its ID 

Params:

- `id` (string) - ID of the trigger to delete

Returns:

- (boolean) - True if successfully deleted, otherwise false

#### deleteAllStravaTriggers()

Removes all Strava triggers in ScriptApp.

#### alertTriggerNotFound_(triggerData)

Sends email to club account saying that a (Strava) trigger was not found and
so could not be deleted.

Params:

- `triggerData` (Object) - Script property value corresponding to the trigger

#### alertStravaActivityNotFound_(rowNumber, tries)

Sends email to club account saying that a Strava activity could not be found.

Params:

- `rowNumber` (integer) - Row that the activity was supposed to be added to
- `tries` (integer) - Number of attempts that the script made to find the activity

