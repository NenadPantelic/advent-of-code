# https://adventofcode.com/2015/day/4#part1
# https://adventofcode.com/2015/day/4#part2
from hashlib import md5

# SECRET_KEY = "pqrstuv"
SECRET_KEY = "bgvyzdsv"

part_1_prefix = "00000"  # part 1
part_2_prefix = "000000"  # part 2

i = 1
while True:
    plain_text = (SECRET_KEY + str(i)).encode('utf-8')
    digest = md5(plain_text).hexdigest()
    if digest.startswith(part_2_prefix):
        break
    i += 1

print(i)
