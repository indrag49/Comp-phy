## Author: Indranil Ghosh, Jadavpur University, Physics Department

## Shootng method to solve boundary value Ordinary Differential equations

f1 <- function(t, y1, y2) return(y2)
f2 <- function(t, y1, y2) return(3*y1^2/2)

#f1 <- function(t, y1, y2) return(y2)
#f2 <- function(t, y1, y2) return(2*y1+8*t*(9-t))


Runge <- function(y1_initial, y2_initial, t_initial, h, t_final){
  time <- seq(t_initial, t_final, h)
  Y1 <- c(y1_initial)
  Y2 <- c(y2_initial)
  
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
  D <- data.frame(time, Y1, Y2)
  return (D)
}

shooting <- function(y1_initial, y1_final, t_initial, h, t_final, guess0, guess1) {
  p0 <- guess0
  p1 <- guess1
  q0 <- Runge(y1_initial, p0, t_initial, h, t_final)$Y1
  q0 <- q0[length(q0)]
  q1 <- Runge(y1_initial, p1, t_initial, h, t_final)$Y1
  q1 <- q1[length(q1)]
  p <- p0+(p1-p0)*(y1_final-q0)/(q1-q0)
  R <- Runge(y1_initial, p, t_initial, h, t_final)
  y1 <- R$Y1
  y2 <- R$Y2
  x <- R$time
  
  plot(x, y1, type="l")
  return(y1)
}
#shooting(0, 0, 0, 3, 9, 4, -24)
shooting(4, 1, 0, 0.01, 1, -39, -30)