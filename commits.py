import git
import datetime
import os

from pytz import timezone

tm = datetime.datetime.today()


def info(path=""):
    os.system(f"cd {path} && git fetch && git pull")
    g = git.Git(working_dir=path)
    loginfo = (g.log()).split()
    return loginfo


def check_commits(loginfo="", commits=0, dictionary_of_commits={}, times="", name=""):
    # print(loginfo)
    dictionary_of_commits = {}
    # int(((loginfo[i + 4]).split(":"))[0])

    for i in range(len(loginfo)):
        if loginfo[i] == "Date:":
            times = (
                datetime.datetime.strptime(
                    " ".join(loginfo[i + 2 : i + 7]),
                    f"%b %d %H:%M:%S %Y %z",  # С любовью от паши
                )
            ).astimezone(timezone("UTC"))
            if (datetime.datetime.now(timezone("UTC")) - times).days < 1:
                if loginfo[i - 3] == "Author:":
                    if loginfo[i - 2] in dictionary_of_commits.keys():
                        dictionary_of_commits[loginfo[i - 2]] += 1
                    else:
                        dictionary_of_commits[loginfo[i - 2]] = 1
                    commits += 1
                else:
                    ct = 0
                    count_names = []
                    while loginfo[i - (2 + ct)] != "Author:":
                        if loginfo[i - (2 + ct)] != "Author:":
                            print(loginfo[i - (2 + ct)])
                            count_names.append(loginfo[i - (2 + ct)])
                        ct += 1
                    for f in range(len(count_names)):
                        name += f"{count_names[-(f)]} "
                    if name in dictionary_of_commits.keys():
                        dictionary_of_commits[name] += 1
                    else:
                        dictionary_of_commits[name] = 1
                    commits += 1
                    name = ""

        times = ""

    if "vons_s" not in dictionary_of_commits.keys():
        dictionary_of_commits["vons_s"] = 0
    return dictionary_of_commits, commits


if __name__ == "__main__":
    ...
