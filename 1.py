PATH = r"C:\Users\23027\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\202202011537\draft_content.json"

with open(PATH, "r", encoding="utf-8") as f:
    line = f.readline()
    print(type(line))
    f.close()