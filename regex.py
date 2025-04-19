import re

s = "Ak@1\23ash"

r = re.sub("[^a-zA-Z]",'',s)

print(r)