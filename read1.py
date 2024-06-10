# review analytics
data = []
count = 0 #計數
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0: # % 是用來求餘數的, 意思是count 跟1000 求餘數 =0, 等於是1000的倍數
			print (len(data)) #每讀一行就把長度印出來
print (len(data))
print (data[0])
print ('--------------------------')
print (data[1])

print ('total', len(data), 'datas')

# 1000000筆平均長度

sum_len = 0
for d in data:
	sum_len += len(d)
print ('average is', sum_len/len(data))

#list filter (filet out work <100)
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print ('total', len(new), 'less then 100')
print (new[0])
print (new[1])