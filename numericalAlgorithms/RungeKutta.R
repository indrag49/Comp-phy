## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Solving Ordinary Differential Equations using Runge-Kutta Methods

##f <- function(x, y) return(-2*x*y^2)
f <- function(x, y) return (-50*(y-cos(x)))

## Modified Euler's method
ME <- function(y_initial, x_initial, h, x_final){
  X <- seq(x_initial, x_final, h)
  Y <- c(y_initial)
  for(i in 2:length(X)) Y <- c(Y, Y[i-1] + h*f(X[i-1]+h/2, Y[i-1]+h/2*f(X[i-1], Y[i-1])))
  print(Y[length(Y)])
  plot(X, Y, type="l")
}

## Heun's method
H <- function(y_initial, x_initial, h, x_final){
  X <- seq(x_initial, x_final, h)
  Y <- c(y_initial)
  for(i in 2:length(X)) Y <- c(Y, Y[i-1]+h/2*(f(X[i-1], Y[i-1])+f(X[i], Y[i-1]+h*f(X[i-1], Y[i-1]))))
  print(Y[length(Y)])
  plot(X, Y, type="l")
}

## Classical Runge-Kutta method
RK <- function(y_initial, x_initial, h, x_final){
  X <- seq(x_initial, x_final, h)
  Y <- c(y_initial)
  for(i in 2:length(X)) {
    p=X[i-1]
    q=Y[i-1]
    k1=h*f(p, q)
    k2=h*f(p+h/2, q+k1/2)
    k3=h*f(p+h/2, q+k2/2)
    k4=h*f(p+h, q+k3)
    Y <- c(Y, q+(k1+2*k2+2*k3+k4)/6)
  }
  print(Y)
  plot(X, Y, type="l")
}
ME(1, 0, 25/1000, 25.0)
