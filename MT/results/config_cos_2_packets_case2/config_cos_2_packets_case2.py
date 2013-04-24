algorithm = "hagedorn"

T = 20
dt = 0.01

dimension = 2
ncomponents = 1

eps = 0.1

potential = {}
potential["potential"] = "(1-cos(x)) + (1-cos(y))"
potential["variables"] = ["x", "y"]


P = [[1.0j,0.0],[0.0, 1.0j]]
Q = [[1.0,0.0],[0.0,1.0]]
p = [[ 0.0],[0.0]]
q = [[ 1.0],[0.0]]
S = [[0.0]]

# What it takes to specify a wavepacket!
wp0 = {
    "type" : "HagedornWavepacket",
    "dimension" : 2,
    "ncomponents": 1,
    "eps" : 0.1,
    "Pi" : [q,p,Q,P,S],
    "basis_shapes" : [{
        "type" : "HyperbolicCutShape",
        "K" : 8,
        "dimension" : 2
    }],
    "coefficients" : [[ ((0,0), 1.0) ]],
    "quadrature" : {
        "type" : "HomogeneousQuadrature",
	'qr': {
            'type': 'TensorProductQR',
            'dimension': 2,
            'qr_rules': [{'dimension': 1, 'order': 12, 'type': 'GaussHermiteQR'},
                         {'dimension': 1, 'order': 12, 'type': 'GaussHermiteQR'}],
        }
    }
}

# Issue: where to put the chis?
initvals = [ wp0 ]

leading_component = 0

basis_size = 20

matrix_exponential = "arnoldi"
