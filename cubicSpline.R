## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Cubic spline of a tridiagonal array
## Algorithm adapted from David Kincaid's book on numerical methods

Spline3_coef <- function(n, t, y) {
  h <- numeric()
  b <- numeric()
  u <- numeric()
  v <- numeric()
  for (i in 2:n) {
    h <- c(h, t[i] - t[i - 1])
    b <- c(b, (y[i] - y[i - 1])/h[i-1])
  }
  u <- c(u, 2*(h[1]+h[2]))
  v <- c(v, 6*(b[1]-b[0]))
  for (i in 2:n-1) {
    u[i] <- 2*(h[i] + h[i-1])-h[i-1]^2/u[i-1]
    v[i] <- 6*(b[i]-b[i-1])-h[i-1]*v[i-1]/u[i-1]
  }
  z[n] <- 0
  for (i in n-1:2) z[i] <- (v[i]-h[i]*z[i+1])/u[i]
  z[0] <- 0
  i <- n
  while(i>=1){
    if (x-t[i]>=0) break
    i <- i-1
  }
  h <- t[i] - t[i-1]
  tmp <- (z[i-1]/2) + (x - t[i-1])*(z[i]-z[i-1])/(6*h)
  tmp <- (-h/6)*(z[i] + 2*z[i-1]) + (y[i]-y[i-1])/h + (x-t[i-1])*tmp
  return(y[i-1]+(x-t[i-1])*tmp)
}
