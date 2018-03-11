## Model of an Epidemic; Strogatz: 3.7.6

require(plot3D)

f1 <- function(t, x, y, z) return(-k*x*y)
f2 <- function(t, x, y, z) return(k*x*y - l*y)
f3 <- function(t, x, y, z) return(l*y)

x_initial <- 10
y_initial <- 5
z_initial <- 3
t_initial <- 0
k <- 0.1
l <- 0.1
t_final <- 1000
h <- 0.1

Runge <- function(x_initial, y_initial, z_initial, t_initial, h, t_final){
  time <- seq(t_initial, t_final, h)
  X <- c(x_initial)
  Y <- c(y_initial)
  Z <- c(z_initial)
  
  for(i in 2:length(time)) {
    p <- time[i-1]
    q <- X[i-1]
    r <- Y[i-1]
    s <- Z[i-1]
    k11 <- h*f1(p, q, r, s)
    k21 <- h*f2(p, q, r, s)
    k31 <- h*f3(p, q, r, s)
    
    k12 <- h*f1(p+h/2, q+k11/2, r+k21/2, s+k31/2) 
    k22 <- h*f2(p+h/2, q+k11/2, r+k21/2, s+k31/2) 
    k32 <- h*f3(p+h/2, q+k11/2, r+k21/2, s+k31/2) 
    
    k13 <- h*f1(p+h/2, q+k12/2, r+k22/2, s+k32/2)
    k23 <- h*f2(p+h/2, q+k12/2, r+k22/2, s+k32/2)
    k33 <- h*f3(p+h/2, q+k12/2, r+k22/2, s+k32/2)
    
    k14 <- h*f1(p+h, q+k13, r+k23, s+k33)
    k24 <- h*f2(p+h, q+k13, r+k23, s+k33)
    k34 <- h*f3(p+h, q+k13, r+k23, s+k33)
    
    X <- c(X, X[i-1]+(k11+2*k12+2*k13+k14)/6)
    Y <- c(Y, Y[i-1]+(k21+2*k22+2*k23+k24)/6)
    Z <- c(Z, Z[i-1]+(k31+2*k32+2*k33+k34)/6)
  }
  N=X+Y+Z
  print(N)

  X_dashed <- k*X*Y
  Y_dashed <- k*X*Y-l*Y
  Z_dashed <- l*y
  
  #plot(Z, Z_dashed, type="l")
  lines3D(X, Y, Z, type="l", col="red")
}

Runge(x_initial, y_initial, z_initial, t_initial, h, t_final)