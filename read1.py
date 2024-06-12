# review analytics
data = []
count = 0 #計數
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0: # % 是用來求餘數的, 意思是count 跟1000 求餘數 =0, 等於是1000的倍數
			print (len(data)) #每讀一行就把長度印出來
# print (len(data))
# print (data[0])
# print ('--------------------------')
# print (data[1])

print ('total', len(data), 'datas')
print (data[0])


wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print (word, wc[word])

print(len(wc))
print (wc['Allen'])
#print (wc)
	
while True:
	word = input ('input your word: ')
	if word == 'q':
		break
	if word in wc:
		print (word, 'got', wc[word], 'times')
	else:
		print ('no this word')

print ('thanks')








# 1000000筆平均長度

sum_len = 0
for d in data:
	sum_len += len(d)
print ('average is', sum_len/len(data))

list filter (filet out work <100)
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print ('total', len(new), 'less then 100')
print (new[0])
print (new[1])

# filter "good"
good = []
for d in data:
	if 'good' in d:
		good.append(d)

# #快寫法
good = [1 for d in data if 'good' in d]
print (good)

bad = ['bad' in d for d in data]


print ('total', len(good), 'mention good')
print (good[0])

