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
    today=str(tm.day),
    month=tru_month(),
    year=str(tm.year),
    loginfo="",
    commits=0,
    dictionary_of_commits={},
    time_del=0,
):
    # print(loginfo)
    dictionary_of_commits = {}
    for i in range(len(loginfo)):
        if (
            loginfo[i] == "Date:"
            and loginfo[i + 5] == year
            and loginfo[i + 2] == month
            and loginfo[i + 3] == today
        ):
            # print(loginfo[i + 2], loginfo[i + 3], loginfo[i + 5])
            if loginfo[i - 2] in dictionary_of_commits.keys():
                dictionary_of_commits[loginfo[i - 2]] += 1
            else:
                dictionary_of_commits[loginfo[i - 2]] = 1
            commits += 1
        if int(today) - 1 == 0:
            today = str((datetime.datetime.today() - datetime.timedelta(days=1)).day)
            month = tru_month(
                month=((datetime.datetime.today() - datetime.timedelta(days=1)).month)
            )
            year = (datetime.datetime.today() - datetime.timedelta(days=1)).year
        else:
            if (
                loginfo[i] == "Date:"
                and loginfo[i + 5]
                == str((datetime.datetime.today() - datetime.timedelta(days=1)).day)
                and loginfo[i + 2] == month
                and loginfo[i + 3] == today
                and int(((loginfo[i + 4]).split(":"))[0]) > time_del
            ):
                # print(loginfo[i + 2], loginfo[i + 3], loginfo[i + 5])
                if loginfo[i - 2] in dictionary_of_commits.keys():
                    dictionary_of_commits[loginfo[i - 2]] += 1
                else:
                    dictionary_of_commits[loginfo[i - 2]] = 1
                commits += 1

    if "vons_s" not in dictionary_of_commits.keys():
        dictionary_of_commits["vons_s"] = 0
    return dictionary_of_commits, commits


if __name__ == "__main__":
    ...
