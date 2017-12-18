## Author: Indranil Ghosh, Physics Department, Jadavpur University

x <- c(0.1)
r <- c(2.4)
dr <- 0.00001
for (i in 2:160001) {
  x <- c(x, r[i - 1]*x[i - 1]*(1 - x[i - 1]))
  r <- c(r, r[i - 1]+dr)
}
plot(r, x, type="p", cex=0.2, pch=15, main="Bifurcation diagram")

