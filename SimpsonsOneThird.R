## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Simpson's 1/3 rule

## We integrate e^(-x^2) in the interval [0, 3]
f <- function(x) exp(-x^2)
## f <- function(x) sin(x)
Simpson <- function(a, b, N) {
  ## No. of intervals N must always be positive
  sec <- N/2
  h <- (b - a)/N
  s <- 0.0
  for (n in 1:sec) {
    X <- a+2*(n-1)*h
    Y <- X+h
    Z <- Y+h
    s <- s+f(X)+4*f(Y)+f(Z)
  }
  return(s*h/3)
}
Simpson(0, 3, 20)
## Simpson(0, pi, 20)