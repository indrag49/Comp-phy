## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Gauss-Legendre integration

#f <- function(x) return ((x^2+2*x+1)/(1+(1+x)^4))
f <- function(x) return (x*sin(x)/(1+ cos(x)^2))

GL <- function(a, b) {
  q <- (a+b)/2
  p <- (b-a)/2
  g <- function(t) return (f(p*t+q)*p)
  D <- data.frame(2*g(0), g(1/sqrt(3))+g(-1/sqrt(3)), (5*g(-sqrt(3/5)) + 8*g(0) + 5*g(sqrt(3/5)))/9)
  colnames(D) <- c("1-Point", "2-point", "3-Point")
  return(D)
} 

#GL(0, 2)
GL(0, pi)