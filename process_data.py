import itertools
import json
from pathlib import Path


def split_by_squarebracket(x):
    output = []
    i = 0
    while i < len(x):
        while i < len(x) and x[i].strip() == "":
            i += 1
        if x[i : i + 2] == "[[":
            j = i + 2
            while j + 1 < len(x) and x[j : j + 2] != "]]":
                j += 1
            output.append(x[i + 2 : j])
            i = j + 2
        else:
            j = i
            while j < len(x) and x[j] != "[":
                j += 1
            output.append(x[i:j])
            i = j
    return output


def wordsparser(x):
    x = split_by_squarebracket(x)
    x = [i for i in x if i]
    x = [i.split("|")[1] if "|" in i else i for i in x]
    return x


path = Path("downloads")
store = []
for i in path.glob("*.md"):
    with open(i) as fd:
        for line in fd.readlines():
            line = line.strip()
            line = line.split("[[")
            line = [i for i in line if i]
            # print(line)
            if len(line) != 2 or line[1][-2:] != "]]":
                print(line)
            else:
                store.append((int(line[0]), line[1][:-2]))
    store = sorted(store, reverse=True)
    with open("freq-both.json", "w", encoding="utf8") as fd:
        json.dump(
            [
                [word, "freq", {"value": i, "displayValue": f"{i} ({freq})"}]
                for i, (freq, word) in enumerate(store)
            ],
            fd,
            ensure_ascii=False,
        )

    with open("freq-freq.json", "w", encoding="utf8") as fd:
        json.dump(
            [
                [word, "freq", {"value": i, "displayValue": f"{i}"}]
                for i, (freq, word) in enumerate(store)
            ],
            fd,
            ensure_ascii=False,
        )

    with open("freq-occurence.json", "w", encoding="utf8") as fd:
        json.dump(
            [
                [word, "freq", {"value": i, "displayValue": f"{freq}"}]
                for i, (freq, word) in enumerate(store)
            ],
            fd,
            ensure_ascii=False,
        )

# with open('spanish.md') as fd:
#     data = [i.strip() for i in fd.readlines()]
#     data = [i for i in data if i]
#     data = [i[1:] if i[0] == '|' else [i] for i in data if i]
#     i = 0
#     output = []
#     while i < len(data) and data[i] == '-':
#         rank = int(data[i+1][:-1])
#         freq = int(data[i+3])
#         for l in set([*wordsparser(data[i+2]), *wordsparser(data[i+4])]):
#             x = [
#                 l,
#                 'freq',
#                 {
#                 'value': rank,
#                 'displayValue': f'{rank} ({freq})',
#                 }
#             ]
#             output.append(x)
#         i += 5
#     with open('spanish.json', 'w', encoding='utf8') as fd:
#         json.dump(output, fd, indent=4, ensure_ascii=False)
