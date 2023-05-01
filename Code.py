library(treeheatr)

p <- read.csv("penguins.csv")

heat_tree(p, target_lab = 'species')

