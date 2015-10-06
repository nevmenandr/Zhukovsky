library(irr)
# if err:
# install.packages("irr")
p <- read.table('forms_no_stopwords', h=FALSE, sep=' ')
pd <- data.frame(p)
kappa2(pd)
