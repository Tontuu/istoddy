# IsToddy

IsToddy is an app to interact with [Todoist API](https://todoist.com) and extract all the tasks.

## Usage

### First you need to retrieve your user token
You can find your token from the Todoist App at [Todoist Integrations](https://todoist.com/prefs/integrations). Create a file called .env with this exact structure:

```env
TOKEN = "YOUR TOKEN HERE"
```

You can setup a default to-do file adding the TODO_FILEPATH variable with the exact filepath to your file, e.g:
```env
TODO_FILEPATH = "/path/to/my/file.md"
```
...
