## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Lagrange's Interpolation

lagrangeInt <- function(X, x, y) {
  n <- length(x)
  l <- numeric(n)
  for (i in 1:n) {
    p <- 1
    for (j in 1:n) {
      if (j != i) p <- p*(X - x[j])/(x[i] - x[j])
      else p <- p
    }
    l[i] <- p
  }
  return (sum(l*y))
}
#x <- c(-1, 1, 4, 7)
#y <- c(-2, 0, 63, 342)
#lagrangeInt(5, x, y)

#x <- c(0.1, 0.2)
#y <- c(0.09983, 0.19867)
#lagrangeInt(0.15, x, y)

x <- c(1997, 1999, 2001, 2002)
y <- c(43, 65, 159, 248)
lagrangeInt(2000, x, y)
