"""Multistate Simulation

This is the configuration file for the multistate simulation code.
All available configuration parameters can be set here. This file
is imported from the simulation code. For configuring the code, just
modifiy the values here.

@author: R. Bourquin
@copyright: Copyright (C) 2010 R. Bourquin
@license: ?
"""

# Algorithm 
# =========

#: The algorithm used for time propagation, can be
#: one of "fourier" | "hagedorn" | "multihagedorn"
algorithm = "fourier"


# Potential
# =========

#: The potential used in the simulation
potential = "two_crossings"


# Time stepping
# =============

#: Perform a simulation in the time interval [0, T].
T = 16

#: Duration of a single time step.
dt = 0.02


# Semi-classical parameters
# =========================

#: The epsilon parameter in the semiclassical scaling
eps = 0.2

#: A free variable that is used for definition of some potentials
delta = 1.0*eps


# Initial values
# ==============

#: Some hagedorn parameters that can be used for defining the initial values.
P = 1.0j
Q = 1.0-6.0j
S = 0.0

#: A list with the lists of (index,value) tuples that set the coefficients
#: of the basis functions for the initial wave packets.
#: Format: [packet][index,value]
coefficients = [ [(0,1.0)], [(0,0.0)] ]

#: The hagedorn parameters of the initial wave packets
#: Format is [ (P0,Q0,S0,p0,q0), (P1,Q1,S1,p1,q1), ... ]
parameters = [ (P, Q, S, 1.0, -6.0), (P, Q, S, 1.0, -6.0) ]


# Specific for Fourier
# ====================

#: Number of grid nodes
ngn = 2**12

#: Scaling factor for the computational domain
#: The interval in the position space is [-f*pi, f*pi]
f = 5.0


# Specific for Hagedorn
# =====================

#: Number of basis functions used for hagedorn packages.
basis_size = 64

#: The leading component is the eigenvalue that governs the propagation of
#: the hagedorn parameters.
leading_component = 0


# Specific for Multi Hagedorn
# ===========================

# None, but basis_size applies here too.


# Output parameters
# =================

#: Filename for the output file that contains the grid nodes
outfile_nodes = "nodes.dat"
#: Filename for the output file that contains the potential
outfile_potential = "potential.dat"
#: Filename for the output file that contains the wavefunctions
outfile_wavefunction = "wavefunction.dat"
#: Filename for the output file that contains the energies
outfile_energies = "energies.dat"
#: Filename for the output file that contains the operators T and V
outfile_operators = "operators.dat"
#: Filename for the output file that contains the hagedorn parameters
outfile_parameters = "parameters.dat"
#: Filename for the output file that contains the hagedorn coefficients
outfile_coefficients = "coefficients.dat"

#: Write data to disk only each n-th timestep
write_nth = 1
