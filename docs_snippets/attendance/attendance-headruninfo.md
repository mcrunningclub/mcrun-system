### Headrun-Info.gs

- *function* [`storeProperty_(key, obj)`](#storeproperty_key-obj)
- *function* [`getAllHeadruns_()`](#getallheadruns_)
- *function* [`getAllHeadrunners_()`](#getallheadrunners_)
- *function* [`getWeekdayAsString_(index)`](#getweekdayasstring_index)
- *function* [`getScheduleFromStore_(weekday)`](#getschedulefromstore_weekday)
- *function* [`getMatchedTimeKey_(submissionDate, runSchedule, offsetHours)`](#getmatchedtimekey_submissiondate-runschedule-offsethours)
- *function* [`getHeadrunnerEmailsFromSchedule_(runLevels)`](#getheadrunneremailsfromschedule_runlevels)
- *function* [`getHeadrunnerEmailsFromNames_(names)`](#getheadrunneremailsfromnames_names)
- *function* [`appendHeadrunnerEmail_(namesStr, delimiter)`](#appendheadrunneremail_namesstr-delimiter)
- *function* [`prettyPrintRunData()`](#prettyprintrundata)
- *function* [`readAndStoreRunData()`](#readandstorerundata)
- *function* [`appendHeadrunInfo_(levelsStr, thisHeadrunner, headrunObj)`](#appendheadruninfo_levelsstr-thisheadrunner-headrunobj)

#### storeProperty_(key, obj)

Stores an object in the document properties store.

Params:

- `key` (string) - The key under which the object will be stored.
- `obj` (Object) - The object to store.

#### getAllHeadruns_()

Retrieves all headruns from the properties store.

Returns:

- (Object) - An object containing all headruns.

#### getAllHeadrunners_()

Retrieves headrunners from the properties store

Returns:

- (Object) - An object containing all headrunners

#### getWeekdayAsString_(index)

Returns day of week (starting on Sunday) given index of the day

Params:

- `index` (number) - Index of weekday to get, eg. 1

Returns:

- (string) - Name of weekday, eg. "Monday"

#### getScheduleFromStore_(weekday)

Return headrun schedule for given day of week.

Params:

- `weekday` (string|number) - Day of week to get schedule for. Can be string representation or js equivalent (1 = 'monday').

Returns:

- (Object) - JSON of run schedule for the given weekday. null if getAllHeadruns_ doesn't return anything


#### getMatchedTimeKey_(submissionDate, runSchedule, offsetHours)

Finds timekey in runSchedule within [submissionDate - offsetHours, submissionDate + offsetHours].

Params:

- `submissionDate` (Date) - Date object of submission time.
- `runSchedule` (Object) - Run schedule to search.
- `offsetHours` (integer) - *Optional* Offset time to search for submission.
                                  Defaults to 2 (hours).

Returns:

- (string) - Matched time key. e.g. `'6pm'`

#### getHeadrunnerEmailsFromSchedule_(runLevels)

Returns email address of headrunners for a run, divided by levels.

Replaced initial `getHeadRunnerEmail()`, which was hard-coded and required updating.

Params:

- `runLevels` (string[]) - Headrun levels to get headrunner emails for.

Returns:

- (Object) - Given run levels as keys and list of emails as values.

Example:

```js
const runs = getScheduleFromStore_('monday');
const emails = getHeadrunnerEmailsFromSchedule_(runs['8am']);
Logger.log(emails)   // { beginner : ['bob@mail.com'], advanced : ['jane@mail.com'] };
```

#### getHeadrunnerEmailsFromNames_(names)

Iterates array of headrunner names and returns array of email address if found.
Names are formatted as `firstName [middleName] initialLastName.`

Params:

- `names` (string[]) - Names of headrunners to get emails for.

Returns:

- (string[]) - List of emails found. If no emails found, return empty list.

Example:

```js
const headrunners = ['Bob B.', 'Jane D.', 'Bart S.'];
const emails = getHeadrunnerEmailFromName_(headrunners);
Logger.log(emails)   // ['bob@mail.com', 'bart@mail.com'] };
```

#### appendHeadrunnerEmail_(namesStr, delimiter)

Adds emails to string with headrunner names.

Params:

- `names` (string) - Headrunner names delimited by newlines
- `delimiter` (string) - *Optional*  Delimiter used to separate headrunners, default \n. 

Returns:

- (string) - Headrunner info as `name:email` delimited by newlines.

Example:

```js
const headrunners = "Bob B.\nJane D.\nBart S.";
const nameEmails = appendHeadrunnerEmail_(headrunners);
Logger.log(nameEmails)   // "Bob B.:bob@mail.com\nJane D.\nBart S.:bart@mail.com";
```

#### prettyPrintRunData()

Display all headrun and headrunner data in user-friendly log

#### readAndStoreRunData()

Parses headrunner information in Headrunner sheet and stores it in Properties store.

Sample data structures:

```js
{ sunday : {
   '10:00am' : { 'easy' : ['Bob B.', 'Jane D.'] },
   '2:15pm': { 'intermediate' : ['Jane D.'] }
}}
{ 'Bob B.' : { email : 'bob.burger@mail.com', strava : '123456789'} }
```

#### appendHeadrunInfo_(levelsStr, thisHeadrunner, headrunObj)

Appends a headrunner to a nested schedule object.

Helper function for `readAndStoreRunData`.

Params:

- `levelsStr` (string) - Headrun schedule string delimited by `;`.
- `thisHeadrunner` (string) - The name of the headrunner to add.
- `headrunObj` (Object) - Stores all headrun information (day, time, level, headrunners).

Example:

```javascript
// Sample Script ➜ Stores headrunner schedule with name.
var headrunnerSchedule = 'Wednesday 6pm (Beginner); Sunday 8am (Intermediate); Sunday 6pm (Beginner)';
appendHeadrunInfo(headrunnerSchedule, 'Bob');   // Appends to `headrunObj`

Logger.log(headrunObj);
// { 'wednesday' : { '6pm' : { 'beginner' : ['Bob'] } },
//   'sunday' : { '8am' : { 'intermediate' : ['Bob'] }, '6pm' : { 'beginner' : ['Bob'] }  }
```

