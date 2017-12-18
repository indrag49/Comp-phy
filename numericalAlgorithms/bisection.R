## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Bisection Method
f <- function(x) return(x^3 - x - 2)
bisection <- function(a, b, epsilon, Max) {
  n <- 1
  while (n<=Max) {
    c <- (a+b)/2
    if (f(c)==0 || (b-a)/2<epsilon) return(c)
    n <- n+1
    if (sign(f(c))==sign(f(a))) a <- c else b <- c
  }
  return ("Max steps reached: no convergence")
}
bisection(1, 2, 0.0001, 20)