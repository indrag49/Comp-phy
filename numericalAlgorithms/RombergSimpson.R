## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Romberg Method for the Simpson's 1/3rd  Rule

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
#f <- function(x) return (x*sin(x)/(1+cos(x)^2))
#f <- function(x) return (x^2/(x^2+log(2*cos(x))^2))
f <- function(x) return (log(x))
Rom_sim <- function (a, b, n) {
  N <- 2^(1:n)
  Y <- numeric()
  z <- numeric()
  for (i in N) Y <- c(Y, Simpson(a, b, i))
  m <- 2
  while (length(Y) >= 2) {
    for(i in 2:length(Y)) z <- c(z, (4^m*Y[i]-Y[i-1])/(4^m-1))
    Y <- z
    z <- numeric()
    m <- m+1
    print(Y)
  }
  return(Y[1])
}