## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Double Integration using Simpson's 1/3rd Rule

# f <- function(x, y) return(1/(x+y))
f <- function(x, y) return (log(x+2*y))
#f <- function(x, y) return(exp(x+y))
Sm <- function(A, B, C, D, h, k) {
  M <- (B-A)/h
  N <- (D-C)/k
  m <- M+1
  n <- N+1
  L <- array(numeric(m*n), dim=c(m, n))
  W <- array(numeric(m*n), dim=c(m, n))
  
  row <- seq(A, B, h)
  col <- seq(C, D, k)
  for (x in 1:length(row)){
    for (y in 1:length(col)) {
      L[x,y] <- f(row[x], col[y])
      if(x%%2==1 && y%%2==1) W[x, y] <- 4
      else if((x%%2==0 && y%%2==1) || (x%%2==1 && y%%2==0)) W[x, y] <- 8
      else W[x, y] <- 16
    }
  }
  W[1, ] <- W[m, ] <- W[1,]/2
  W[ ,1] <- W[ ,n] <- W[ ,1]/2
  return(h*k*sum(W*L)/9)
}
#Tr(1, 2, 1, 2, 0.1, 0.25)
Sm(1.4, 2.0, 1.0, 1.5, 0.15, 0.25)
#Sm(0, 1, 0, 1, 0.25, 0.25)