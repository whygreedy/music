import os

# 讀取檔案
music = []
if os.path.isfile('platform.csv'):
	print('Yeah! Find the file.')
	with open('platform.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'platform, length' in line:
				continue
			platform, length = line.strip().split(',')
			music.append([platform, length])
else: 
	print('Oh no...the file can not be found.')
	
# 請使用者輸入
while True:
	platform = input('Which platform did you use for listening to music? ')
	if platform == 'q':
		break
	length = input('How many hours did you spend on this platform to listen to music per day? ')
	music.append([platform, length])

# 印出各平台使用量
for m in music:
	print('Playing music on', m[0], 'for about', m[1], 'hours per day')

# 寫入檔案
with open('platform.csv', 'w', encoding='utf-8') as f:
	f.write('platform, hours\n')
	for m in music:
		f.write(m[0] + ',' + m[1] + '\n')