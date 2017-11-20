simple_Pendulum_Euler <- function(theta, omega, length, dt) {
  Th <- c(theta) ## initial angle
  Om <- c(omega) ## initial angular frequency
  g <- 9.8
  t <- c(0) ## initial time
  T <- 2*pi*sqrt(length/g)
  
  for (i in 2:10000) {
    t <- c(t, t[i - 1] + dt)
    Om <- c(Om, Om[i - 1] - g*Th[i - 1]*dt/length)
    Th <- c(Th, Th[i - 1] + Om[i - 1]*dt)
  }
  plot(t, Th, type="l", col="red", main="Simple Pendulum with Euler's method")
}

simple_Pendulum_Euler(5, 10, 5, 0.01)