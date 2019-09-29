music = []
# 讀取檔案

# 請使用者輸入
while True:
	artist = input('Who/What is your favorite singer/band? ')
	if artist == 'q':
			break
	song = input('Which his/her/their song do you like the most? ')
	music.append([artist, song])
# 印出喜愛列表
for m in music:
	print('You are the fan of', m[0], 'and loving the song', m[1])
# 寫入檔案
with open('favorite.csv', 'w', encoding='utf-8') as f:
	f.write('artist, song\n')
	for m in music:
		f.write(m[0] + ',' + m[1] + '\n')