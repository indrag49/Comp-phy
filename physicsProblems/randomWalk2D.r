## Author: Indranil Ghosh, Physics Department, Jadavpur University

###############################################################################
## A simulation of Random walk in 2-D. Step length is +-1 and probability of ##
## moving in all the four directions is equal i.e, 1/4.                      ##
###############################################################################


x <- c(0.0)
y <- c(0.0)

for (i in 2:10000) {
  r <- runif(1)
  if (r<=1/4) {
    x <- c(x, x[i-1]+1)
    y <- c(y, y[i-1])
  }
  else if(r<=2/4) {
    x <- c(x, x[i-1])
    y <- c(y, y[i-1]+1)
  }
  else if(r<=3/4) {
    x <- c(x, x[i-1]-1)
    y <- c(y, y[i-1])
  }
  else {
    x <- c(x, x[i-1])
    y <- c(y, y[i-1]-1)
  }
}

plot(x, y, type="l", col="red", main="Random walk in 2D")
  
  
