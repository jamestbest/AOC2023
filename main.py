import re

digs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit = f"(?=({'|'.join(digs)}|1|2|3|4|5|6|7|8|9))"

tot = 0

while (inp := input()) is not None and inp != "":
    groups = re.findall(digit, inp)

    firstDig = groups[0]
    firstVal = int(firstDig) if firstDig.isdigit() else digs.index(firstDig) + 1

    lastDig = groups[len(groups) - 1]
    lastVal = int(lastDig) if lastDig.isdigit() else digs.index(lastDig) + 1

    whole = int(str(firstVal) + str(lastVal))
    tot += whole

print(tot)
