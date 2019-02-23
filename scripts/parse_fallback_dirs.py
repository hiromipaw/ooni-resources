import urllib
import csv

link = "https://gitweb.torproject.org/tor.git/plain/src/app/config/fallback_dirs.inc"
f = urllib.request.urlopen(link)
myfile = f.read()

intext = str(myfile)
strings = intext.split("/* ===== */")[2:-1]
lines = []

for s in strings:
    line = []
    line.append(s.split(" ")[0].split("\\n\"")[1].split(":")[0])
    line.append(s.split("orport=")[1].split(" ")[0])
    line.append(s.split("nickname=")[1].split(" ")[0])
    line.append("or_port")
    lines.append(line)

with open('tor-bridges-ip-port-updated.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for l in lines:
        csv_writer.writerow(l)
