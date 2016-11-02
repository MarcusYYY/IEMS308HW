library("arules")
tr <- read.transactions("Dillards POS/output_CA.csv", format = "basket", sep=",", skip = 1)
rules = apriori(tr,parameter=list(support=0.000086, confidence=0.5))
inspect(rules)
plot(rules)
plot(rules, method="graph")
subrules = rules[quality(rules)$confidence > 0.8]
plot(rules, method="graph",control=list(type="items"))