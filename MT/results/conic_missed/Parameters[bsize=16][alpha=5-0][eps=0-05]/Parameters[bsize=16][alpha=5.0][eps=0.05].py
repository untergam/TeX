#########################################
# This file was automatically generated #
#########################################

bsize = 16
Q = [[1.0, 0.0], [0.0, 1.0]]
S = [[0.0]]
alpha = 5.0
matrix_exponential = "arnoldi"
ncomponents = 2
p = [[1.0], [0.0]]
dimension = 2
P = [[1j, 0.0], [0.0, 1j]]
dt = 0.001
eps = 0.05
potential = "conic"
T = 0.2
q = [[-0.1      ],
              [ alpha*eps]]
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
leading_component = 0
initvals = [ wp0 ]
algorithm = "hagedorn"
