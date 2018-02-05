## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Inverse Quadratic interpolation method

#f <- function(x) -2
f <- function(x) x*exp(x)-cos(x)
IQI <- function(x0, x1, x2, Max, epsilon) {
  k <- 1
  while(k<=Max) {
    f0 <- f(x0)
    f1 <- f(x1)
    f2 <- f(x2)
    x3 <-f1*f2*x0/((f0-f1)*(f0-f2))+f0*f2*x1/((f1-f0)*(f1-f2))+f0*f1*x2/((f2-f0)*(f2-f1)) 
    if(abs(x3 - x2)<epsilon) return (x3)
    x0 <- x1
    x1 <- x2
    x2 <- x3
    k <- k + 1
  }
  return ("error: maximum limit reached")
}
#IQI(0, 1, 2, 20, 0.0001)
IQI(0, 0.5, 1, 20, 0.0001)