## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Romberg Method for the Trapezium Rule

Trap <- function(a, b, N) {
  interval <- (b - a)/(N - 1) ## There are N points evenly placed at an interval
  S <- 0.0
  x <- 0.0
  for (n in 1:N) {
    x <- a + (n-1)*interval
    if (n==1 || n==N) weight <- interval/2 else weight <- interval
    S <- S + weight*f(x)
  }
  return(S)
}
#f <- function(x) return (x*sin(x)/(1+cos(x)^2))
f <- function(x) return (x^2/(x^2+log(2*cos(x))^2))
Rom_Trap <- function (a, b, n) {
  N <- 2^(1:n)
  Y <- numeric()
  z <- numeric()
  for (i in N) Y <- c(Y, Trap(a, b, i))
  m <- 1
  while (length(Y) >= 2) {
    for(i in 2:length(Y)) z <- c(z, (4^m*Y[i]-Y[i-1])/(4^m-1))
    Y <- z
    z <- numeric()
    m <- m+1
    print(Y)
  }
}

#Rom_Trap(0, pi, 10)
Rom_Trap(0, pi/2, 20)