#install BiocManager if you don't have it already
install.packages("BiocManager", repos='http://cran.rstudio.com/')

#install IRanges from bioconductor
BiocManager::install("IRanges")

#install devtools if you don't have it already
install.packages("devtools", repos='http://cran.rstudio.com/')
library(devtools)

# Install the NORMT3 package manually as it has been removed from CRAN
install.packages("/path/to/NORMT3_1.0.4.tar.gz", repos = NULL, type = "source")

# install the 'bmm' package
install_github("genome/bmm")

# install the 'sciClone' package
install_github("genome/sciClone")

