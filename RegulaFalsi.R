## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Regula Falsi Method

#f <- function(x) return(x^3 + 3*x - 5)
#f <- function(x) return(x*log10(x)-1.2)
f <- function(x) return(5*(sin(x))^2-8*(cos(x))^5)
Falsi <- function(a, b, epsilon, Max) {
  n <- 0
  B <- b
  while(n<=Max) {
    fa <- f(a)
    fb <- f(b)
    x <- a-(fa*(b-a))/(fb-fa)
    n <- n+1
    if (abs(x-B)<epsilon*abs(x)) return(x)
    else {
      print(c(n, a, b, x))
      B <- x
      fx <- f(x)
      if (sign(fa)==sign(fx)) a <- x else b <- x
    }
  }
}
#Falsi(1, 2, 0.0001, 25)
#Falsi(2, 3, 0.0001, 25)
Falsi(0.5, 1.5, 0.0001, 25) 