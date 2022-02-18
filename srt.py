#PATH = "draft_content.json"
PATH = r"C:\Users\23027\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\202202011537\draft_content.json"
import json
import datetime


def srttime(t):
    ms = str(0)
    s = str(0)
    m = str(0)
    h = str(0)

    if t < 1000:
        ms = str(t)
    elif t >= 1000 and t < 60000:
        s = str(t // 1000)
        ms = str(t % 1000)
    elif t >= 60000 and t < 3600000:
        m = str(t // 60000)
        s = str(t % 60000 // 1000)
        ms = str(t % 60000 % 1000)
    elif t >= 3600000:
        h = str(t // 3600000)
        m = str(t % 3600000 // 60000)
        s = str(t % 3600000 % 60000 // 1000)
        ms = str(t % 3600000 % 60000 % 1000)

    if len(s) == 1:
        s = "0" + s
    if len(m) == 1:
        m = "0" + m
    if len(h) == 1:
        h = "0" + h
    while len(ms) < 3:
        ms = "0" + ms

    return h + ":" + m + ":" + s + "," + ms


with open(PATH, "r", encoding="utf-8") as f:
    line = f.readline()
    dict = json.loads(line)
    text = dict["materials"]["texts"]
    time = dict["tracks"]
    f.close()


with open(
    datetime.datetime.now().strftime("%F")
    + "-"
    + datetime.datetime.now().strftime("%T").replace(":", "-")
    + ".srt",
    "w",
    encoding="utf-8",
) as f:
    for num in range(len(time[1])):
        start = int(int(time[1]["segments"][num]["target_timerange"]["start"]) / 1000)
        duration = int(
            int(time[1]["segments"][num]["target_timerange"]["duration"]) / 1000
        )
        end = start + duration

        sub = text[num]["content"]

        content = (
            str(num + 1)
            + "\n"
            + srttime(start)
            + " --> "
            + srttime(end)
            + "\n"
            + sub
            + "\n"
            + "\n"
        )
        f.write(content)
    f.close()
print("ok")
