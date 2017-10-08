from fbchat import Client
from fbchat.models import *

playlist = []


def add_to_playlist(link):
	playlist.append(link)
	print playlist

#subclass Client to have the behavior we want when receiving a message
class YouTubeLinkGrabber(Client):
	def onMessage(self,mid=None, author_id=None, message=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg={}):
		#checks attachments for youtube links
		#if thread_id == group.uid: #not implemented for testing
		if len(msg['delta']['attachments']) > 0:
			for item in msg['delta']['attachments']:
				if "youtu" in item['mercury']['share']['media']['source']: #catches youtube and youtu.be links
					add_to_playlist(item['mercury']['share']['media']['source'])


with open("../info/fblogin","r") as userinfo:
	email = userinfo.readline()
	password = userinfo.readline()

client = YouTubeLinkGrabber(email, password)

with open("../info/group","r") as gname:
  group = client.searchForGroups(gname)[0]

client.listen()
