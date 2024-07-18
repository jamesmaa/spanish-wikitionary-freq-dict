import time
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
i0 = 0
delta = 5000
i1 = 225000
from pathlib import Path
p = Path('downloads')
p.mkdir(exist_ok=True)
while i0 < i1:
    inext = min(i0 + delta, i1)

    url =f'https://en.wiktionary.org/w/index.php?title=User:Matthias_Buchmeier/Spanish_frequency_list-{i0 + 1}-{inext}&action=raw'
    print(url)
    time.sleep(1)
    with open(p / f'spanish-{i0 + 1}-{inext}.md', 'w', encoding='utf8') as fd:
        fd.write(requests.get(url, headers=headers).text)

    i0 = inext
