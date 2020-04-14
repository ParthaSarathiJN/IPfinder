from bs4 import BeautifulSoup
import requests
import pprint


URL = 'https://ipinfo.io/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#pprint.pprint(soup)


	# If you want to create a txt file with the all the values stored there.
#with open('ipCodeWithPostalCode.txt', 'w') as ipCodeWithPostal:
#	ipCodeWithPostal.write(str(soup))


resultList = throwawayList = []
resultDictionary = {}


replaceList = ['\n', '{', '}', '\t', '"']

for i in str(soup).split(','):

	for i2 in replaceList:
		i = i.rstrip(' ')
		i = i.lstrip(' ')

		if i2 in i: i = i.replace(i2, '')

	resultList.append(i)


throwawayList = [i.split(': ') for i in resultList]


resultList = []

for i in throwawayList:
	if len(i) == 2:
		for i2 in i:
			resultList.append(i2)
	elif len(i) == 1:
		pass
		#print('HAS ONE ITEM!!!')
		#another_list.append(i)
	else:
		pass


def dictConverter(resultList):

	for i in range(0, len(resultList),2):

		resultDictionary[resultList[i]] = (resultList[i+1])

	return resultDictionary

print(dictConverter(resultList))
#resultDictionary = dictConverter(resultList)



	# Uncomment for not showing all the fields visible
#print(resultList)


	# Add appropriate function with correct key and refrence in different file.
#def fullPinFromIP():
#	return resultDictionary.get('postal')
#def fullCountryFromIP():
#	return resultDictionary.get('country')
