## Bead on a rotating hoop (without any damping force and air friction) solved by Runge Kutta algorithm

require(plot3D)

g <- 9.8
r <- 0.5
phi0 <- pi/3
omega0 <- 0.3
y1_initial <- 0.1
y2_initial <- 0
t_initial <- 0
t_final <- 100
h <- 0.01


f1 <- function(t, y1, y2) return (y2)
f2 <- function(t, y1, y2) return (omega0^2*sin(y1)*cos(y1)-g*sin(y1)/r)
Runge <- function(y1_initial, y2_initial, t_initial, h, t_final){
  time <- seq(t_initial, t_final, h)
  Y1 <- c(y1_initial)
  Y2 <- c(y2_initial)
  x <- numeric()
  y <- numeric()
  z <- numeric()
  
  for(i in 2:length(time)) {
    p <- time[i-1]
    q <- Y1[i-1]
    r <- Y2[i-1]
    k11 <- h*f1(p, q, r)
    k21 <- h*f2(p, q, r)
    k12 <- h*f1(p+h/2, q+k11/2, r+k21/2) 
    k22 <- h*f2(p+h/2, q+k11/2, r+k21/2) 
    k13 <- h*f1(p+h/2, q+k12/2, r+k22/2)
    k23 <- h*f2(p+h/2, q+k12/2, r+k22/2)
    k14 <- h*f1(p+h, q+k13, r+k23)
    k24 <- h*f2(p+h, q+k13, r+k23)
    Y1 <- c(Y1, Y1[i-1]+(k11+2*k12+2*k13+k14)/6)
    Y2 <- c(Y2, Y2[i-1]+(k21+2*k22+2*k23+k24)/6)
  }
  #D <- data.frame(time, Y1, Y2)
  for (i in 1:length(Y1)) {
    x <- c(x, r*sin(Y1[i])*cos(phi0+omega0*time[i]))
    y <- c(y, r*sin(Y1[i])*sin(phi0+omega0*time[i]))
    z <- c(z, -r*cos(Y1[i]))
  }
  
  #plot(time, Y1, type="l")
  lines3D(x, y, z, type="l", col="red")
}

Runge(y1_initial, y2_initial, t_initial, h, t_final)