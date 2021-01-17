#!/usr/bin/python3

import os


### making necessary folders to store respective files.

username = os.getlogin()
#print(username)
home_dir = f'/home/{username}'
sourceDir = f'{home_dir}/Downloads/'
folders = {
	'document': f'{home_dir}/Documents/Downloaded_Documents/', 
	'picture': f'{home_dir}/Pictures/Downloaded_Pictures/',
	'music': f'{home_dir}/Music/Downloaded_Music/',
	'video': f'{home_dir}/Videos/Downloaded_Videos/',
}

for i in folders.values():
	if not os.path.exists(i):
		os.system(f'mkdir {i}')

files = [f"{sourceDir}{f}" for f in os.listdir(f'{home_dir}/Downloads/')]
#print(files)

print("\n\033[31m Moving Files ... Don't exit !!! ")
print('\n\033[39m')
#print(files)
for f in files:

	# Kickout Documents
	if f.endswith(('.pdf', '.doc', '.docx', '.xls', '.odt', '.ppt')):
		print(f, end=" ... ")
		os.system(f"mv \"{f}\" {folders['document']}")
		print("\033[32m Done")
		print('\n\033[39m')

	# kickout Pictures
	if f.endswith(('.jpg', '.JPG', '.png', '.PNG', '.jpeg', '.JPEG', '.gif', '.GIF', '.svg', '.SVG')):
		print(f, end=" ...")
		os.system(f"mv \"{f}\" {folders['picture']}")
		print("\033[32m Done")
		print('\n\033[39m')
	
	# kickout Music
	if f.endswith(('.mp3', '.aac', '.opus', '.ogg')):
		print(f, end=" ...")
		os.system(f"mv \"{f}\" {folders['music']}")
		print("\033[32m Done")
		print('\n\033[39m')

	# kickout videos
	if f.endswith(('.mp4', '.webm', '.mkv', '.avi', '.flv', '.mov')):
		print(f, end=" ...")
		os.system(f"mv \"{f}\" {folders['video']}")
		print("\033[32m Done")
		print('\n\033[39m')

print('\033[93m All moving Done !!!')
