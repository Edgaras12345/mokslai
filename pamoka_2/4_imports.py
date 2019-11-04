"""
"I always choose a lazy person to do a hard job, because a lazy person will find an easy way to do it." - Bill Gates

Import'ai - vienas is lengviausiu budu rasyti greita koda. Kodo importavimas yra mechanizmas, kurio pagalba galima greitai
pernaudoti jau parasyta koda.
"""

# Import the requests library. Essentially, this https://pypi.org/project/requests/
import requests

# use one of the functions in requests library called "get()". It takes a string as a parameter. pass google.
# Return is a response object
response = requests.get("http://www.google.com")
print(response)


print(response.text)


print("==== autogidas.lt ====")
# https://autogidas.lt/skelbimas/mitsubishi-pajero-dyzelinas--2002-m-visureigis-0132415742.html
autogidas_url = "https://autogidas.lt/skelbimas/mitsubishi-pajero-dyzelinas--2002-m-visureigis-0132415742.html"
autogidas_response = requests.get(autogidas_url)

print("response is:")
print(autogidas_response.content)
