#########################################
# This file was automatically generated #
#########################################

bsize = 16
Q = [[1.0, 0.0], [0.0, 1.0]]
S = [[0.0]]
delta = 0.1
write_nth = 5
algorithm = "hagedorn"
eps = 0.05
p = [[0.5], [0.0]]
dimension = 2
P = [[1j, 0.0], [0.0, 1j]]
dt = 0.01
ncomponents = 2
potential = "delta_gap_rotsym"
T = 10
q = [[-3.0], [0.0]]
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
            'qr_rules': [{'dimension': 1, 'order': 20, 'type': 'GaussHermiteQR'},
                         {'dimension': 1, 'order': 20, 'type': 'GaussHermiteQR'}],
        }
    }
}
leading_component = 0
initvals = [ wp0 ]
matrix_exponential = "arnoldi"
