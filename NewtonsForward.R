## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Newton's Forward interpolation

NewtonForward <- function(X, x, y) {
  N <- length(x)
  z <- numeric()
  f <- numeric()
  Y <- y[1]
  M <- numeric()
  fac <- factorial
  while(length(y) >= 2) {
    for(i in 2:length(y)) z <- c(z, y[i] - y[i-1])
    f <- c(f, z[1])
    y <- z
    z <- numeric()
  }
  h <- abs(x[1]-x[2])
  g <- numeric()
  for(i in 1:N) {
    for (j in 1:i-1) g <- c(g, X-x[j])
    M <- c(M, prod(g)/(fac(i-1)*h^(i-1)))
    g <- numeric()
  }
  M <- M[2:length(M)]
  return (sum(M*f)+Y)
}

#NewtonForward(0.5, c(-2, -1, 0, 1, 2, 3), c(15, 5, 1, 3, 11, 25))
#NewtonForward(0.35, c(0.1, 0.2, 0.3, 0.4, 0.5), c(1.40, 1.56, 1.76, 2.00, 2.28))
NewtonForward(1.0, c(0.1, 0.3, 0.5, 0.7, 0.9, 1.1), c(-1.699, -1.073, -0.375, 0.443, 1.429, 2.631))
