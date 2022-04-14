import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Ultra").teaching()
elif 'aarch' in arc:
	__import__("Ultra64").teaching()
else:
	exit(f' Unknow device machine {arc}')