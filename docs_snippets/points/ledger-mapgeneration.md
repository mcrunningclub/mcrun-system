### Map-Generation.gs

- *function* [`createMapForRow(row)`](#createmapforrowrow)
- *function* [`createMapForActivity_(activity, timestamp)`](#createmapforactivity_activity-timestamp)
- *function* [`convertPolylineToMap_(polyline, name, imgSize)`](#convertpolylinetomap_polyline-name-imgsize)
- *function* [`uploadImageToCloudStorageBucket_(imageBlob, imageName)`](#uploadimagetocloudstoragebucket_imageblob-imagename)
- *function* [`getServiceAccountAccessToken_(key)`](#getserviceaccountaccesstoken_key)

#### createMapForRow(row)

Create the PNG image of the run route from Strava activity from its polyline
data and saves the public image URL in the row.

Params:

- `row` (number) - *Optional* GSheet row to target. Defaults to last row.


#### createMapForActivity_(activity, timestamp)

Gets the polyline data from given activity and calls helper function to create a
PNG image for it, then adds the image URL to the activity.

Previous iterations of map creation include `MAP.newStaticMap()`, embedding GDrive download url
in email (access restricted after some time), and adding map as inline image (email becomes too heavy).

Params:

- `activity` (Object) - Strava activity with "map" key containing polyline data
- `timestamp` (Date) - Recorded timestamp of event.
- `fileName` (string) - Name to save map with

Returns:

- (Object) - Strava activity with appended map url under the "mapUrl" key (or '' if unsuccessful)


#### convertPolylineToMap_(polyline, name, imgSize)

Save polyline as image using Google Static Map API and Make.com automation.

Params:

- `polyline` (string) - Encoded Google Map polyline string.
- `name` (string) - Name for map.
- `imgSize` (string) - Size of map image, e.g "400x300"


#### uploadImageToCloudStorageBucket_(imageBlob, imageName)

Uploads given image blob to cloud storage under the provided name,
and returns the resulting URL.

Params:

- `imageBlob` (string) - Image data as a blob.
- `imageName` (string) - Name to save the image under.

Returns:

- (string|null) - URL of the image in cloud storage, or null if error occurred.

#### getServiceAccountAccessToken_(key)

Helper function to get an access token using the service account key

Params:

- `Key` (Object) - for service account for Google Cloud.

Returns:

- (string) - Access token to cloud storage.

