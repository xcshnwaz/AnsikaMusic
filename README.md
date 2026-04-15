If you're on Heroku, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `sample.env` in the root directory and add all the variables there.
An example of `sample.env` file:

```py
API_ID=
API_HASH=
BOT_TOKEN=
LOGGER_ID=
MONGO_DB_URI=
OWNER_ID=
STRING_SESSION=
```
  </details>

<details>
  <summary><b>Vars and Details :</b></summary>

`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)
  
`OWNER_ID` : Your Telegram User ID

`LOGGER_ID` : Your Telegram Chat ID For logs Where Bot and Assistant Id Should Be AdMin! 

`STRING_SESSION` : Add String session for assistant to play songs on voice chat.

`DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can click on logo below!