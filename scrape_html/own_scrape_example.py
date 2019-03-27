from bs4 import BeautifulSoup
import requests

page_link = 'https://en.wikipedia.org/wiki/VfB_Stuttgart'
# fetch the content from url
page_response = requests.get(page_link)
# parse html
page_content = BeautifulSoup(page_response.text, "html.parser")

get_title = page_content.find('h1')

# getting all html elements which == p (<p>)
getting_all_p = page_content.find_all('p')
# assigning and indexing to the second p on the page (the one I need)
get_p_needed = getting_all_p[1]

# getting all html elements which == ul (<ul>)
ul = page_content.find_all('ul')
# assigning and indexing to the eight ul on the page (the one I need)
my_ul = ul[8]

# printing them all in a nice readable format
print('\n' + get_title.string + '\n')
print('------------------------------------------------------------')
print('Description: ' + '\n' + '\n' + get_p_needed.get_text())
print('------------------------------------------------------------' + '\n')
print('National won Titles: ' + '\n' + '\n' + my_ul.get_text())
