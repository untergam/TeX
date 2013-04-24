#########################################
# This file was automatically generated #
#########################################

bsize = 32
Q = [[1.0, 0.0], [0.0, 1.0]]
S = [[0.0]]
delta = 0.05
matrix_exponential = "arnoldi"
ncomponents = 2
q = [[1.0], [0.0]]
potential = "conic_avoided"
leading_component = 0
P = [[1j, 0.0], [0.0, 1j]]
dt = 0.01
eps = 0.01
dimension = 2
T = 4
p = [[0.0], [0.0]]
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
            'dimension' : 2
        },
        {
            'type' : 'HyperbolicCutShape',
            'K' : bsize,
            'dimension' : 2
        }
    ],
    'coefficients' : [[ ((0,0), 1.0) ],
                      [ ((0,0), 0.0) ]],

    'quadrature' : {
        'type' : 'HomogeneousQuadrature',
	'qr': {
            'type': 'TensorProductQR',
            'dimension': 2,
            'qr_rules': [{'dimension': 1, 'order': 40, 'type': 'GaussHermiteQR'},
                         {'dimension': 1, 'order': 40, 'type': 'GaussHermiteQR'}],
        }
    }
}
initvals = [ wp0 ]
algorithm = "hagedorn"
