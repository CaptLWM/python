import webbrowser

urls = ['http://www.naver.com', 'http://www.daum.net', 'http://www.google.com']

for url in urls:
    webbrowser.open_new(url)


google_url = "http://www.google.com/search?q="
search_words = ['python web scraping', 'python webbrowser']

for search_word in search_words:
    webbrowser.open_new(google_url + search_word)
