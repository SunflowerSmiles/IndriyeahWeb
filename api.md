# API paths

## **POST** `/api/register`
> to register a device which has not been registered yet
### Body
No Body
### Successful Response (200)
returns a secure cookie encoding the user identity

## **POST** `/api/append_history/<history item>`
> appends the `history item` to `HISTORY.log` dedicated to the user
### Body
No Body
### Successful Response (200)
No response

## **GET** `/api/get_history/<start line>/<end line>`
> gets the history, the `start` and `end` index follow the same logic as substrings/slicing, i.e.
> the range of lines which the api returns is [start line, end line), where line numbers start from `0`
> so to get the first 30 lines, one would query `/api/get_history/0/30`
### Body
No Body
### Successful Response (200)
```json
{
	"src" : [
		...              CONTAINS an array of all the lines written in history
	]
}
```
<!---
<br><br><br><br><br>
.
## **POST** /api/text-to-speech
> you post a string containg the text to be converted to speech
<br>
### Body
```json
{
	"src"  : ...,         
	
	"lang" : ...,         OPTIONAL, DEFAULT 'en', change narration language
	"slow" : ...,         OPTIONAL, defines if narration should be slow
}
```
<br>
### Successful Response (200)
returns a BLOB/file containing the speech mp3 file
<br>
## **POST** /api/speech-to-text
> you post the speech file in the body as a BLOB/Large Binary Object
<br>
### Body
<.ogg blob>
### Successful Response (200)
```json
{
	"status" : "OK"
	"src"    : ...,        CONTAINS the text from speech
}
```
-->
