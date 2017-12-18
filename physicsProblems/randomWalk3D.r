## Author: Indranil Ghosh, Physics Department, Jadavpur University

###############################################################################
## A simulation of Random walk in 3-D. Step length is +-1 and probability of ##
## moving in all the four directions is equal i.e, 1/6.                      ##
###############################################################################

require(plot3D)

x <- c(0)
y <- c(0)
z <- c(0)

for (i in 2:10000) {
  r <- runif(1)
  if (r<=1/6) {
    x <- c(x, x[i-1]+1)
    y <- c(y, y[i-1])
    z <- c(z, z[i-1])
  }
  else if(r<=2/6) {
    x <- c(x, x[i-1])
    y <- c(y, y[i-1]+1)
    z <- c(z, z[i-1])
  }
  else if(r<=3/6) {
    x <- c(x, x[i-1])
    y <- c(y, y[i-1])
    z <- c(z, z[i-1]+1)  
  }
  else if(r<=4/6) {
    x <- c(x, x[i-1]-1)
    y <- c(y, y[i-1])
    z <- c(z, z[i-1])
  }
  else if(r<=5/6) {
    x <- c(x, x[i-1])
    y <- c(y, y[i-1]-1)
    z <- c(z, z[i-1])
  }
  else {
    x <- c(x, x[i-1])
    y <- c(y, y[i-1])
    z <- c(z, z[i-1]-1)  
  }
}

lines3D(x, y, z, type="l", col="red", main="Random walk in 3D")

