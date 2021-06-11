'''
	file containing definitions for users of discord chess, used to ref player usernames to query
	chess.com API

	created on: 06/10/21
	created by: CAT
'''
from enum import Enum 


class Users(Enum):
	'''
		enum containing users in discord chess chat
	'''
	COLIN = "ctarg"
	CONNOR = "cdunni"
	DEMETRIUS = "Stalemattic"