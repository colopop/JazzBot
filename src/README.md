Both files are Python2 and must be run independently.

## sender.py
This is the reminder bot. It will read the MEMBERS list twice a day and send a notification every twelve hours regarding whose turn it is.
Unfortunately, it cannot send user notifications.

## listener.py
This is the listener bot. When a message is sent, it reads that message and determines if it contains a YouTube link. 
When complete, it will copy that link and add that video to a playlist. This may require another bot.
