library(ggplot2)

args <- commandArgs(trailingOnly = TRUE)

f=read.table(args[1])

pdf(args[2], 12,10)
qplot(V1, V2, data=f, fill=V3, geom='tile') + theme(axis.text.x = element_text(angle = 45, hjust = 1))
dev.off()
