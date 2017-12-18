## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Newton Raphson

## f <- function(x) x^3 - 5*x + 1
## f_dashed <- function(x) 3*x^2 - 5
f <- function(x) x*log10(x)-12.34
f_dashed <- function(x) log10(x) + 1/log10(x)
Newton <- function(x_ini, Max, epsilon) {
  k <- 1
  while(k<=Max) {
    x_final <- x_ini - f(x_ini)/f_dashed(x_ini)
    print(x_final)
    if(abs(x_final - x_ini)<epsilon) return (x_final)
    x_ini <- x_final
    k <- k + 1
  }
  return ("error: maximum limit reached")
}
## Newton(0.5, 5, 0.0001)
Newton(10, 10, 0.0001)