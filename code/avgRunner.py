N = 5# average of five
open("averageDataHook","w").close()# clear data
import prisonersDilemma
for _ in range(N):
    prisonersDilemma.runFullPairingTournament(prisonersDilemma.STRATEGY_FOLDER, "avgTesting")
data = {}
with open("averageDataHook") as rawData:
    for line in rawData:
        prog, score = line.split("⁰")
        if prog in data.keys():
            data[prog].append(float(score))
        else:
            data[prog] = [float(score),]

for key in data.keys():
    print(sum(data[key])/len(data[key]), key, sep="\t")
