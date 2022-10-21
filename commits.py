import git
import datetime
import os

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
    today=str(tm.day), month=tru_month(), year=str(tm.year), loginfo="", commits=0
):
    for i in range(len(loginfo)):
        if loginfo[i] == "Date:":
            if loginfo[i + 5] == year:
                if loginfo[i + 2] == month:
                    if loginfo[i + 3] == today:
                        print(loginfo[i + 2], loginfo[i + 3], loginfo[i + 5])
                        commits += 1
    return commits


if __name__ == "__main__":
    print(info())
    print(check_commits(loginfo=info()))
