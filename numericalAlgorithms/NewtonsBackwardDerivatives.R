## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Derivatives using Newton's backward method

options(warn=-1)
NFD <- function(X, x, y) {
  ## This calculated f'(X) and f''x from a table of datas for x and y
  N <- length(x)
  z <- numeric()
  f_dashed <- numeric()
  while(length(y) >= 2) {
    for (i in 2:length(y)) z <- c(z, y[i]-y[i-1])
    f_dashed <- c(f_dashed, z[length(z)])
    y <- z
    z <- numeric()
  }
  h <- abs(x[1] - x[2])
  s <- (X - x[N])/h
  f_double_dashed <- f_dashed[2:length(f_dashed)]
  f1 <- c(1, (2*s+1)/2, (3*s^2+6*s+2)/6, (4*s^3+18*s^2+22*s+6)/24, (5*s^4+40*s^3+105*s^2+100*s+24)/120)
  f2 <- c(1, (s+1), (6*s^2+18*s+11)/12, (2*s^3+12*s^2+21*s+10)/12)
  D <- data.frame(h, s, sum(f1[1:length(f_dashed)]*f_dashed)/h, sum(f2[1:length(f_double_dashed)]*f_double_dashed)/(h^2))
  colnames(D) <- c('h', 's', "f'(X)","f''(X)")
  return(D)
}
#NFD(3, c(1, 1.5, 2, 2.5, 3), c(-1.5, -2.875, -3.5, -2.625, 0.5))
#NFD(2.5, c(1,1.5, 2, 2.5), c(3.7183, 5.4817, 8.3891, 13.1825))
NFD(1.2, c(0, 0.3, 0.6, 0.9, 1.2), c(1, 1.8221, 3.3201, 6.0496, 11.0232))
