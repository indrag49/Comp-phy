## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Power Method to calculate the largest eigen value from a set of linear equations 

powerMethod <- function(A, eps, Max) {
  n <- nrow(A)
  v <- array(rep(1, times=n), dim=c(n, 1))
  i=1
  while(i <= Max) {
    y <- A %*% v
    print("y=")
    print(y)
    lambda <- y/v
    print("lambda=")
    print(lambda)
    if (n<3) {
      if (abs(lambda[1]-lambda[2]) < eps) return(lambda[1])
    }
    else {
      if (abs(lambda[1]-lambda[2]) < eps && abs(lambda[2]- lambda[3]) < eps) return (lambda[1])
    }
    m <- max(y)
    print("m=")
    print(m)
    v <- y/m
    print("v")
    print (v)
    i <- i+1
  }
  return ("Maximum iteration reached, no convergence")
}
#A <- array(c(25, 1, 2, 1, 3, 0, 2, 0, -4), dim=c(3, 3))
#A <- array(c(1, 3, 2, 4), dim=c(2, 2))
A <- array(c(1, 3, -1, 3, 2, 4, -1, 4, 10), dim=c(3, 3))
A <- array(c(3, 1, 5, 1, 0, 2, 5, 2, -1), dim=c(3, 3))
powerMethod(A, 0.0005, 200)
