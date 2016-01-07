library(ggplot2)

args <- commandArgs(trailingOnly = TRUE)

f=read.table(args[1])

pdf(args[2], 12,10)
names(f)[3]="concordance"
qplot(V1, V2, data=f, fill=concordance, geom='tile', xlab = "samples", ylab="normals") + theme(axis.text.x = element_text(angle = 45, hjust = 1), legend.position="top")
dev.off()
