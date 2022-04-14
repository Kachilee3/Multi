import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("File").teaching()
elif 'aarch' in arc:
	__import__("File64").teaching()
else:
	exit(f' Unknow device machine {arc}')