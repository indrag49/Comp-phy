f <- function(x) {
  return (x^3 + 5*x)
}

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
Trap(0, 8, 1000)

V <- c()
N <- c()
for (i in 1:1000) {
  V <- c(V, Trap(0, 8, i))
  N <- c(N, i)
}
plot (N, V, col="blue", type="l", main="convergence of the value of the integration")