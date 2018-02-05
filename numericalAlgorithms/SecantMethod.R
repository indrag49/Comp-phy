## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Secant method

f <- function(x) x*exp(x)-cos(x)
Secant <- function(x0, x1, Max, epsilon) {
  k <- 1
  while(k<=Max) {
    f0 <- f(x0)
    f1 <- f(x1)
    x2 <- x1-f1*(x1-x0)/(f1-f0)
    if(abs(x2 - x1)<epsilon) return (x2)
    x0 <- x1
    x1 <- x2
    k <- k + 1
  }
  return ("error: maximum limit reached")
}
Secant(0.5, 1, 20, 0.0001)
