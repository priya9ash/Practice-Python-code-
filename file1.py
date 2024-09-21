import re

text = "Closing Thoughts: The film concludes at 00:20:00.000, reminding viewers of the importance of 00:20:00.000 preserving these natural wonders for future '\\n\\n1\\n00:05.080 --> 00:09.310\\n' generations."


pattern2search = r"\\n\\n\d\\n\d\d:\d\d.\d\d\d --> \d\d:\d\d.\d\d\d\\n"


reg = re.compile(pattern2search)


match = reg.search(text)  


if match:
    print(match.group())  
else:
    print("No match found.")