# -*- coding: UTF-8 -*-

def getQuotation(filename,storytemp,story):
	with open(filename, 'r') as f:
		for line in f:
			line = line.replace('\u3000','').replace('\n','')
			#找出小說中所有包含在上下引號中的字
			while line.find('「') != -1 and line.find('」') != -1:
				storytemp.append(line[line.find('「')+1:line.find('」')])
				line = line[line.find('」')+1:]	#有時一段文字會有超過一個上引號

storytemp = []
story = []
#getQuotation('狐狸的故事.txt',storytemp,story)
getQuotation('歡樂頌.txt',storytemp,story)

#用句號將太長的句子分割
for i in range(len(storytemp)):
	sentence = storytemp[i].split('。')
	for s in sentence:
		if s != "":
			story.append(s)
'''
for i in range(len(story)):
	print(story[i])
'''

#讀取word2vec產生的文字檔，裡面有各種可能出現在回答中的詞
posibleAnswers = []
with open('AnswerWords.txt', 'r') as f:
	for line in f:
		line = line.replace('\n','')
		posibleAnswers.append(line)

#找到配對的問答句子
question = []
answer = []
with open('sentencePair.txt', 'a') as f:
	for num in range(len(posibleAnswers)):
		for index in range(1,len(story)):
			if posibleAnswers[num] in story[index] and len(story[index-1])>3:
				question.append(story[index-1])
				answer.append(story[index])
				print(story[index-1])
				print(story[index])
				print('----')
				f.write(story[index-1]+'\n')
				f.write(story[index]+'\n')
				f.write("----\n")
print(len(question))

