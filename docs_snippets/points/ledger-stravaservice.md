### Strava-Service.gs

- *function* [`reset_()`](#reset_)
- *function* [`safeReset()`](#safereset)
- *function* [`getStravaActivity_(fromTimestamp, toTimestamp)`](#getstravaactivity_fromtimestamp-totimestamp)
- *function* [`getStravaService_()`](#getstravaservice_)
- *function* [`authCallback_(request)`](#authcallback_request)
- *function* [`callStravaAPI_(query_object)`](#callstravaapi_query_object)
- *function* [`queryObjToString_(query_object)`](#queryobjtostring_query_object)

#### reset_()

Reset the authorization state, so that it can be re-tested.

#### safeReset()

Run `reset` safely using script property flag `IS_RESET_ALLOWED`.

Must manually change value before running. Once allowed, flag toggles back to false.


#### getStravaActivity_(fromTimestamp, toTimestamp)

Get Strava activities within the given time frame

Params:

- `fromTimestamp` (integer?) - Start of time frame, in Unix epoch time
- `toTimestamp` (integer?) - End of time frame, in Unix epoch time

Returns:

- (Object[]) - Returns array of Strava activities

#### getStravaService_()

Configures the Strava service using the OAuth2 library.

Three required and optional parameters are not specified
because the library creates the authorization URL with them
automatically: `redirect_url`, `response_type`, and `state`.

*APPENDED COMMENTS BY USER*

Client ID and Secret stored in script properties. *(Mar 23, 2025)*


#### authCallback_(request)

Handles the OAuth callback.

*APPENDED COMMENTS BY USER*

Must have global scope in project *(Mar 23, 2025)*


#### callStravaAPI_(query_object)

Makes an API request to the given endpoint with the given query.

Inspired by original function `run` in `apps-script-oauth2/samples/Strava.gs`

Params:

- `endpoint` (string) - Strava API endpoint.

Params:

- `query_object` (object) - *Optional* Param-value pair. Defaults to empty object.

Returns:

- (string) - Response of API call.

Example:

```javascript
const endpoint = 'clubs/693906/activities';
const queryObj = {"param1": val1, "param2": val2};
const response = callStravaAPI(endpoint, queryObj);
```

#### queryObjToString_(query_object)

Maps an Object containing param-value pairs to a query string.

Params:

- `query_object` (object) - Param-value pair.

Returns:

- (string) - String value of query object.

Example:

```javascript
const queryObj = {"param1": val1, "param2": val2};
const ret = queryObjToString(queryObj);
Logger.log(ret)  // "?param1=val1&param2=val2"
```