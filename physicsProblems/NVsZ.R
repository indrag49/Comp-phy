## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Plotting Neutron number vs Proton Number 

V <- read.table("C:/Users/mypc/Documents/NVsZ.txt", header=TRUE, sep=" ")
Z <- 1:length(V$MassNumber)
N <- V$MassNumber - Z
plot(Z, N, type="l", col="red", main="Neutron-Proton diagram for stable nuclides")
lines(Z, Z, type="l")