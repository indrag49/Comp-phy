(* Author: Indranil Ghosh, Physics Department, Jadavpur University *)

l=3; m=2; LegendreP[l, m, x]

Clear[l]; Table[Plot[Re[SphericalHarmonicY[l, l, t, 0]],{t, 0,Pi}], {l, 0, 10}]