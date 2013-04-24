algorithm = "hagedorn"

potential = "delta_gap"

T = 7
dt = 0.01

eps = 0.1

delta = 0.75*eps

f = 4.0
ngn = 4096

leading_component = 0
basis_size = 80

P = 1.0j
Q = 1.0-5.0j
S = 0.0

parameters = [ (P, Q, S, 1.0, -5.0), (P, Q, S, 1.0, -5.0) ]
coefficients = [[(0,0.6),(1,0.8)], [(0,0.0)]]

write_nth = 1
