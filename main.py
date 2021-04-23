import requests
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
domain_url = 'https://www.sunhome.ru/'
parent_url = 'dreams/'
main_page = requests.get(domain_url + parent_url, headers={'User-Agent': user_agent})

soup_main_page = BeautifulSoup(main_page.content, 'html.parser')
letters_urls = []
word_link_dict = {}
records = []
for link in soup_main_page.find(id='search-form').find_all('a'):
    letter = link.get('href').split('/')[-1]
    letters_urls.append(letter + '/')
for url in letters_urls:
    letter_page = requests.get(domain_url + parent_url + url, headers={'User-Agent': user_agent})
    soup_letter_page = BeautifulSoup(letter_page.content, 'html.parser')
    for link in soup_letter_page.find(id='word-list').find_all('a'):
        path = link.get('href').split('/')[-1]
        word_link_dict[link.get('title')] = path + '/'
    break

for word, path in word_link_dict.items():
    print(word)
    word_page = requests.get(domain_url + parent_url + path, headers={'User-Agent': user_agent})
    soup_word_page = BeautifulSoup(word_page.content, 'html.parser')
    for content_block in soup_word_page.find_all('div', class_='big-frame shadow-preview'):
        records.append({'Word': word,
                        'Content': content_block.find('div').text,
                        'Source': content_block.find('span').text.strip()
                        })
    print('end')
    break
print(len(records))
print(records)
for item in records:
    print(item['Source'])


