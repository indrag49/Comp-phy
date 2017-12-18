## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Newton’s Divided Difference Interpolation

NewtonDifference <- function(X, x, y) {
  N <- length(y)
  Y <- y[1]
  f <- numeric()
  M <- numeric()
  i <- 2
  it <- 1
  z <- numeric()
  a <- numeric()
  while (length(y) >= 2) {
    for (j in length(y):2) z <- c(z, (y[j] - y[j-1]))
    z <- rev(z)
    #print(z)
    for (t in N:i) a <- c(a, x[t] - x[t - it])
    a <- rev(a)
    #print(a)
    z <- z/a
    #print(z)
    f <- c(f, z[1])
    y <- z
    z <- numeric()
    a <- numeric()
    it <- it + 1
    i <- i + 1
  }
  g <- numeric()
  for (i in 1:N){
    for (j in 1:i-1) g <- c(g, X- x[j])
    M <- c(M, prod(g))
    g <- numeric()
  }
  M <- M[2:length(M)]
  return(sum(M*f)+Y)
}
#NewtonDifference(3, c(-4, -1, 0, 2, 5), c(1245, 33, 5, 9, 1335))
#NewtonDifference(0.5, c(-2, -1, 0, 1, 3, 4), c(9, 16, 17, 18, 44, 81))
#NewtonDifference(8, c(1, 3, 4, 5, 7, 10), c(3, 31, 69, 131, 351, 1011))
#NewtonDifference(10, c(5, 6, 9, 11), c(12, 13, 14, 16))
#NewtonDifference(8, c(4, 5, 7, 10, 11, 13), c(48, 100, 294, 900, 1210, 2028))
NewtonDifference(1.5, c(1, 1.3, 1.6, 1.9, 2.2), c(0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623))
