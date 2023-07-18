# Installing required R packages
requiredPackages <- c(
  "R6",
  "cowplot",
  "digest",
  "ggplot2",
  "igraph",
  "limSolve",
  "RColorBrewer",
  "Rcpp",
  "RcppArmadillo",
  "reshape2",
  "scales",
  "devtools"  # Include devtools in the list
)

for (p in requiredPackages) {
  if (!require(p, character.only=TRUE)) {
    install.packages(p, repos = "https://cloud.r-project.org")  # Set the repos argument here
  }
}

# The devtools library is required for installing packages from BitBucket
library(devtools)

# Install Cloe from the BitBucket repository
install_bitbucket("fm361/cloe", dependencies=TRUE)

# Building the vignette (if pandoc is installed)
install_bitbucket("fm361/cloe", dependencies=TRUE, build_vignettes=TRUE)

