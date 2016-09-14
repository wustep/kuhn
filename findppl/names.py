import urllib.request, json, csv
from urllib.request import urlopen

url = "https://directory.osu.edu/fpjson.php?name_n="
read = open("data.txt", "r").read().split('\n')
with open("out.csv", "w", newline='') as file:
    out = csv.writer(file)
    for line in read:
        name = line
        link = (url+name)
        r = urlopen(link)
        d = json.loads(r.read().decode("utf-8"))
        if (len(d) > 0):
            if (len(d[0]["appointments"]) > 0):
                print(name + "," + d[0]["appointments"][0]["organization"] + "," + d[0]["appointments"][0]["job_title"])
                out.writerow([name, d[0]["appointments"][0]["organization"], d[0]["appointments"][0]["job_title"]])
            else:
                print(name + ",-");
                out.writerow([name, "-"]);
        else:
            print(name + ",--");
            out.writerow([name, "--"])
