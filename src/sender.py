import fbchat as fb
import time
from getpass import getpass

with open("info/fblogin","r") as userinfo:
	email = userinfo.readline()
	password = userinfo.readline()
	
client = fb.Client(email,password)
with open("info/group","r") as gname:
  group = client.searchForGroups(gname.read())[0] #find the right group

target_time = time.time()
first_post_today = True #first post of the day
while True:

	if time.time() >= target_time: #if it's posting time

		with open("../info/MEMBERS", 'r+') as memfile: #repeatedly reading means we can update membership without restarting the bot
			mem = filter(None,memfile.read().split('\n'))

			client.sendMessage("Next up is "+mem[0],thread_id=group.uid,thread_type=fb.models.ThreadType.GROUP) #post the message

			target_time += 12 * 60 * 60 #next message in 12 hours

			if first_post_today:
				first_post_today = False

			else:
				mem.append(mem.pop(0)) #update the order
				mem.seek(0)
				for item in mem:
					memfile.write(item+'\n')
				first_post_today = True

	time.sleep(1 * 60 * 60) #wait an hour before trying again
		
