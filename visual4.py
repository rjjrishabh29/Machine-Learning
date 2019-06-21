from collections import Counter
import bs4
import requests
import matplotlib.pyplot as plt
web=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup=bs4.BeautifulSoup(web.content, 'html.parser')
textcontent=[]

for i in range(0,20):
	para=soup.find_all("p")[i].text
	textcontent.append(para)
with open("webdata.txt",'w') as f:
	for i in textcontent:
		f.write('%s' % i)
f=open("webdata.txt",'r')  #open the file in read mode
data=f.read()
num_words=len(data.split()) #counts the number of words in the scraped data
print("Number of words:",num_words)


with open("webdata.txt",'r') as f:
	list1=[word for line in f for word in line.split()]
word_count=Counter(list1)
word1=[]
count1=[]
word2=[]
count2=[]

#this for loop will fetch the word which are repeated more then 3 times
for i in word_count:       
  if word_count[i]>=4:
    word2.append(i)
    count2.append(word_count[i])

plt.figure()
plt.xlabel("words that appear more then 3 times")
plt.ylabel("No of times the word appear")
plt.grid(color='green')
plt.scatter(word2,count2)

#this loop will fetch the top 20 repeated words
for word, count in word_count.most_common(20): 
	word1.append(word)
	count1.append(count)

plt.figure()  
plt.xlabel("Top 20 repeated words")
plt.ylabel("No of times the word is repeated")
plt.bar(word1,count1)

plt.figure()  	
plt.pie(count1,labels=word1,autopct='%1.1f%%') 

plt.show()
