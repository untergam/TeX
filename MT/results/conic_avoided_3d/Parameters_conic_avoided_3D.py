#########################################
# This file was automatically generated #
#########################################

algorithm = "hagedorn"

eps = 0.01

bsize = 16

T = 4
dt = 0.01

potential = {}
potential["variables"] = ["x", "y", "z"]
potential["potential"] = [["x", "sqrt(y**2+z**2+delta**2)"],
                          ["sqrt(y**2+z**2+delta**2)", "-x"]]

delta = 0.5

dimension = 3
ncomponents = 2

q = [[1.0],
     [0.0],
     [0.0]]

p = [[0.0],
     [0.0],
     [0.0]]

P = [[1.0j, 0.0,  0.0],
     [0.0,  1.0j, 0.0],
     [0.0,  0.0,  1.0j]]

Q = [[1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 1.0]]

S = [[0.0]]

wp0 = {
    'type' : 'HagedornWavepacket',
    'dimension' : dimension,
    'ncomponents': ncomponents,
    'eps' : eps,
    'Pi' : [q,p,Q,P,S],
    'basis_shapes' : [
        {
            'type' : 'HyperbolicCutShape',
            'K' : bsize,
            'dimension' : dimension
        },
        { 
            'type' : 'HyperbolicCutShape',
            'K' : bsize,
            'dimension' : dimension
        }
    ],
    'coefficients' : [[ ((0,0,0), 1.0) ],
                      [ ((0,0,0), 0.0) ]],
    'quadrature' : {
        'type' : 'HomogeneousQuadrature',
        'qr': {
            'type': 'TensorProductQR',
            'dimension': dimension,
            'qr_rules': [{'dimension': 1, 'order': 20, 'type': 'GaussHermiteQR'},
                         {'dimension': 1, 'order': 20, 'type': 'GaussHermiteQR'},
                         {'dimension': 1, 'order': 20, 'type': 'GaussHermiteQR'}],
        }
    }
}

initvals = [ wp0 ]
leading_component = 0

matrix_exponential = "arnoldi"

