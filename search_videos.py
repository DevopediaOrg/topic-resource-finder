import urllib.request
import urllib.parse
import re

search_param = input("Enter search param\n")
query_string = urllib.parse.urlencode({"search_query" : search_param})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print ("Fetching the videos for keyword : "+search_param)
for result in search_results:
    print("http://www.youtube.com/watch?v=" + result)

# just list of URLs, duplicates
