## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Runge-Kutta method for solving a system of equations

par(mfrow=c(2, 1))
#f1 <- function(x, y1, y2) return(-3*y1+2*y2)
#f2 <- function(x, y1, y2) return(3*y1-4*y2)

f1 <- function(x, y1, y2) return(1-4*y1+y1^2*y2)
f2 <- function(x, y1, y2) return(3*y1-y1^2*y2)
R <- function(y1_initial, y2_initial, x_initial, h, x_final){
  X <- seq(x_initial, x_final, h)
  Y1 <- c(y1_initial)
  Y2 <- c(y2_initial)
  for(i in 2:length(X)) {
    p <- X[i-1]
    q <- Y1[i-1]
    r <- Y2[i-1]
    k11 <- h*f1(p, q, r)
    k21 <- h*f2(p, q, r)
    k12 <- h*f1(p+h/2, q+k11/2, r+k21/2) 
    k22 <- h*f2(p+h/2, q+k11/2, r+k21/2) 
    k13 <- h*f1(p+h/2, q+k12/2, r+k22/2)
    k23 <- h*f2(p+h/2, q+k12/2, r+k22/2)
    k14 <- h*f1(p+h, q+k13, r+k23)
    k24 <- h*f2(p+h, q+k13, r+k23)
    Y1 <- c(Y1, Y1[i-1]+(k11+2*k12+2*k13+k14)/6)
    Y2 <- c(Y2, Y2[i-1]+(k21+2*k22+2*k23+k24)/6)
  }
  #print(Y1)
  #print(Y2)
  plot(X, Y1, type="l")
  plot(X, Y2, type="l")
}
R(1.5, 3, 0, 20/10^4, 20)
