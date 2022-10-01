# API paths

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
	"status" : ..., 
	"src"    : ...,        CONTAINS the text from speech
}
```

