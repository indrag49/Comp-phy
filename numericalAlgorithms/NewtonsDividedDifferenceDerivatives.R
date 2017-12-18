## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Derivatives using Newton's divided differene method

options(warn=-1)
NDD <- function(X, x, y) {
  N <- length(y)
  f_dashed <- numeric()
  i <- 2
  it <- 1
  z <- numeric()
  a <- numeric()
  while (length(y) >= 2) {
    for (j in 2:length(y)) z <- c(z, (y[j] - y[j-1]))
    for (t in i:N) a <- c(a, x[t] - x[t - it])
    z <- z/a
    f_dashed <- c(f_dashed, z[1])
    y <- z
    z <- numeric()
    a <- numeric()
    it <- it + 1
    i <- i + 1
  }
  f_double_dashed <- f_dashed[2:length(f_dashed)]
  f1 <- c(1, (X-x[1])+(X-x[2]), (X-x[2])*(X-x[3]) + (X-x[1])*(X-x[3]) + (X-x[1])*(X-x[2]))
  f2 <- c(2, 2*(3*X-x[1]-x[2]-x[3]))
  D <- data.frame(sum(f1[1:length(f_dashed)]*f_dashed), sum(f2[1:length(f_double_dashed)]*f_double_dashed))
  colnames(D) <- c("f'(X)","f''(X)")
  return(D)
}
NDD(1.6, c(1, 1.5, 2, 3), c(0, 0.40547, 0.69315, 1.09861))