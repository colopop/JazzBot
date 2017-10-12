from fbchat import Client
from fbchat.models import *

playlist = []

#for testing -- this will end up adding the link to a youtube playlist.
def add_to_playlist(link):
	playlist.append(link)
	with open("info/links","a") as pl:
		pl.write("1"+playlist[-1])

#subclass Client to have the behavior we want when receiving a message
class YouTubeLinkGrabber(Client):
	def onMessage(self,mid=None, author_id=None, message=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg={}):
		#checks attachments for youtube links
		#if thread_id == group.uid: #not implemented for testing
		if len(msg['delta']['attachments']) > 0: #time to navigate the absurd structure of a facebook message. this checks for attachments.
			for item in msg['delta']['attachments']:
				if "youtu" in item['mercury']['share']['media']['source']: #catches youtube and youtu.be links
					add_to_playlist(item['mercury']['share']['media']['source']) 


with open("info/fblogin","r") as userinfo:
	email = userinfo.readline()
	password = userinfo.readline()

client = YouTubeLinkGrabber(email, password)

with open("info/group","r") as gname:
  group = client.searchForGroups(gname.read())[0]

client.listen()
