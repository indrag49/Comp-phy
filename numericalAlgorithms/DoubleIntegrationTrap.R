## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Double Integration using Trapezoidal Rule

# f <- function(x, y) return(1/(x+y))
f <- function(x, y) return (log(x+2*y))
#f <- function(x, y) return(exp(x+y))
Tr <- function(A, B, C, D, h, k) {
  M <- (B-A)/h
  N <- (D-C)/k
  m <- M+1
  n <- N+1
  L <- array(numeric(m*n), dim=c(m, n))
  
  ## Write the weight matrix
  W <- (L+1)*4
  W[1, ] <- W[m, ] <- W[ ,n] <- W[ ,1] <- 2
  W[1, 1] <- W[m, 1] <- W[1, n] <- W[m, n] <- 1
  
  row <- seq(A, B, h)
  col <- seq(C, D, k)
  for (x in 1:length(row)){
    for (y in 1:length(col)) {
      L[x,y] <- f(row[x], col[y])
    }
  }
  return(h*k*sum(W*L)/4)
}
#Tr(1, 2, 1, 2, 0.1, 0.25)
Tr(1.4, 2.0, 1.0, 1.5, 0.15, 0.25)
#Tr(0, 1, 0, 1, 0.5, 0.5)