import requests
import re

pattern = r'(<a.*?href=)([\"\']\w*://)?[\"\']?([\w\.\-]*\w)?'

urls = requests.get(input()).text
res = re.findall(pattern, urls)
ans = sorted(list(set(url[-1] for url in res)))
print(*ans, sep='\n')



