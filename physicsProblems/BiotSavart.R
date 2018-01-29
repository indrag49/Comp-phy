## Author: Indranil Ghosh, Jadavpur University, Physics Department

# Generalised complete Elliptic Integration solution
cel <- function(kc, p, l, s){
  if (kc==0) return (NaN)
  epsilon <- 1e-06
  k <- abs(kc)
  P <- p
  cc <- l
  S <- s
  em <- 1.0
  if (p>0) {
    P <- sqrt(p)
    S <- s/P
  }
  else{
    f <- kc^2
    q <- 1-f
    g <- 1-P
    f <- f-P
    q <- q*(S-l*P)
    P <- sqrt(f/g)
    cc <- (l-S)/g
    S <- -q/(g^2*P) + cc*P
  }
  f <- cc
  cc <- cc + S/P
  g <- k/P
  S <- 2*(S+f*g)
  P <- g+P
  g <- em
  em <- k+em
  K <- k
  while (abs(g-k)>g*epsilon) {
    k <- 2*sqrt(K)
    K <- k*em
    f <- cc
    cc <- cc+S/P
    g <- K/P
    S <- 2*(S+f*g)
    P <- g+P
    g <- em
    em <- k+em
  }
  return(pi/2*(S+cc*em)/(em*(em+P)))
}

# We can calculate the magnetic field at any point (X, Y. Z) on/off the axis
B <- function(X, Y, Z, a, length, I, n) {
  # length is the length of the cylinder
  # a is the radius of the solenoid
  # n is the number of turns of the solenoid
  # I is the current through the solenoid
  rho <- sqrt(X^2+Y^2)
  mu0 <- 4*pi*10^(-7)
  b <- length/2
  B0 <- mu0*n*I/pi
  z_plus <- Z+b
  z_minus <- Z-b
  alpha_plus <- a/sqrt(z_plus^2+(rho+a)^2)
  alpha_minus <- a/sqrt(z_minus^2+(rho+a)^2)
  beta_plus <- z_plus/sqrt(z_plus^2+(rho+a)^2)
  beta_minus <- z_minus/sqrt(z_minus^2+(rho+a)^2)
  gamma <- (a-rho)/(a+rho)
  k_plus <- sqrt((z_plus^2+(a-rho)^2)/(z_plus^2+(a+rho)^2))
  k_minus <- sqrt((z_minus^2+(a-rho)^2)/(z_minus^2+(a+rho)^2))
  # radial Magnetic field
  B1 <- B0*(alpha_plus*cel(k_plus, 1, 1, -1)-alpha_minus*cel(k_minus, 1, 1, -1))
  # longitudinal magnetic field
  B2 <- B0*a*(beta_plus*cel(k_plus, gamma^2, 1, gamma)-beta_minus*cel(k_minus, gamma^2, 1, gamma))/(a+rho)
  # Self Inductance of the solenoid
  k0 <- b/sqrt(a^2+b^2)
  L <- 8*mu0*(n*a)^2*(sqrt(a^2+b^2)*cel(k0, 1, 1, 2*k0^2)-a)
  #return(c(B1, B2, L))
  return(B2)
}

Z <- seq(0.001, 1, 0.001)
b <- numeric()
for(z in Z) {
  b <- c(b, B(0, 0, z, 0.5, 1, 10^7/(4*pi), 1))
}
plot(Z, b, type="l")