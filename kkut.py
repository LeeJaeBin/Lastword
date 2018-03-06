from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
from random import *
import time

start_time = time.time()
inputString = '안녕'
nounList = []
cntCheck = 0
test = 0
wrngCheck = 0
realNoun = []
comusedList = []
userusedList = []
i = 0
comTried = 0
j = 0
lose = 0

while True:

	if wrngCheck == 5:
		print("5번 연속으로 틀렸습니다. 상당히 못하시는군요...\n")
		break

	inputString = input("단어를 입력하세요(항복 하시려면 '재빈이가 최고야' 를 입력하세요): ")

	delayedTime = (time.time() - start_time)
	if delayedTime>30:
		print("30초 이상 지연되어 패배로 처리됩니다.\n")
		break

	if cntCheck!=0:
		if inputString[0]!=randWord[ranwordLen-1]:
			print(randWord[ranwordLen-1]+"\n")
			print("규칙에 맞지 않는 단어입니다.\n")
			wrngCheck+=1
			continue
		else:
			wrngCheck = 0

	if wrngCheck==0:
		length = len(inputString)
		test = parse.quote(inputString[length-1])

		print("입력한 값 : "+inputString+"\n")

		userLen = len(userusedList)

		while i!=userLen:
			if userusedList[i]==inputString:
				break
			i+=1
		if i==userLen:
			userusedList.append(inputString)
		else:
			print("이미 사용한 단어입니다.\n")
			continue
		i=0

		if inputString=='재빈이가 최고야':
			print("\nYou resigned")
			break
	
		html = urlopen("http://wordrow.kr/%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-%EB%A7%90/"+test+"/")
		bsobj = BeautifulSoup(html, "html.parser")
		wordList = bsobj.findAll("span", {"class" : "label-info"})#.find("span", {"class" : "label-info"})
		infoList = bsobj.findAll("div", {"class" : "col-xs-6"})

		count = 0
		cnt = 0
		listLen = len(infoList)
	
		if listLen==0:
			print("재빈이가 최고야\n")
			break

		while cnt!=listLen-1:
			infoString = infoList[cnt].get_text()
			Noun = wordList[cnt].get_text()
			if '명사' in infoString:
				nounList.append(infoString)
				realNoun.append(Noun)
				count+=1
			cnt+=1

		if count==0:
			print("재빈이가 최고야\n")
			break

		cntCheck+=1
		comLen = len(comusedList)
		comTried = 0

		while True:
			comTried+=1
			randNum = randint(0, count-1)
			randWord = realNoun[randNum]

			while j!=comLen:
			
				if comusedList[j]==randWord:
					break
			
				j+=1

				if comTried>=50:
					print("재빈이가 최고야")
					lose = 1
					break
			
			if lose==1:
				break

			if j==comLen:
				comusedList.append(randWord)
				break
			j=0
		j=0
		if lose==1:
			break

		ranwordLen = len(randWord)
		print(nounList[randNum]+"\n")
		print(randWord[ranwordLen-1]+"\n")
		start_time = time.time()
		del nounList[:]
		del realNoun[:]
