import git
import datetime
import os

from pytz import timezone

tm = datetime.datetime.today()


def tru_month(
    months={
        "1": "Jan",
        "2": "Feb",
        "3": "Mar",
        "4": "Apr",
        "5": "May",
        "6": "Jun",
        "7": "Jul",
        "8": "Aug",
        "9": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec",
    },
    month=str(tm.month),
):
    return months[month]


def info(path="", path2=""):
    os.system(f"cd {path2} && git fetch && git pull")
    g = git.Git(path)
    loginfo = (g.log()).split()
    return loginfo


def check_commits(
    loginfo="",
    commits=0,
    dictionary_of_commits={},
    times="",
):
    # print(loginfo)
    dictionary_of_commits = {}
    # int(((loginfo[i + 4]).split(":"))[0])

    for i in range(len(loginfo)):
        if loginfo[i] == "Date:":
            for b in range(5):
                times += f"{loginfo[(i+2)+b]} "
            times = (
                datetime.datetime.strptime(times, f"%b %d %H:%M:%S %Y %z ")
            ).astimezone(timezone("UTC"))

            if (datetime.datetime.now(timezone("UTC")) - times).days < 1:
                if loginfo[i - 2] in dictionary_of_commits.keys():
                    dictionary_of_commits[loginfo[i - 2]] += 1
                else:
                    dictionary_of_commits[loginfo[i - 2]] = 1
                commits += 1
        times = ""

    if "vons_s" not in dictionary_of_commits.keys():
        dictionary_of_commits["vons_s"] = 0
    return dictionary_of_commits, commits


if __name__ == "__main__":
    ...
