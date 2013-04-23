"""Multistate Simulation

This is the configuration file for the multistate simulation code.
All available configuration parameters can be set here. This file
is imported from the simulation code. For configuring the code, just
modifiy the values here.

@author: R. Bourquin
@copyright: Copyright (C) 2010 R. Bourquin
@license: Public Domain
"""

# Algorithm 
# =========

#: The algorithm used for time propagation, can be
#: one of "fourier" | "hagedorn" | "multihagedorn".
algorithm = "hagedorn"


# Potential
# =========

#: The potential $V\ofs{x}$ used in the simulation. See the I{PotentialLibrary} for
#: available potentials.
potential = "delta_gap"


# Time stepping
# =============

#: Perform a simulation in the time interval $[0, T]$.
T = 10

#: Duration of a single time step $\tau$.
dt = 0.01


# Semi-classical parameters
# =========================

#: The parameter $\varepsilon$ in the semiclassical scaling.
eps = 0.1

#: A variable that is used in the definition of some potentials.
delta = 0.1*eps


# Initial values
# ==============

# Some hagedorn parameters that can be used for defining the initial values.
P = 1.0j
Q = 1.0 - 5.0j
S = 0.0

#: A list of $N$ lists of $(k,c_k)$ tuples that set the coefficient $c_k$
#: of the basis function $\phi_k$. The $i$-th list sets the coefficients
#: $c^i$ of the component $\Phi_i$ of the initial wavepacket $\Psi$.
coefficients = [ [(0,1.0)] , [(0,0.0)] ]

#: A list of the Hagedorn parameter sets $\Pi_i$ of component $\Phi_i$ of the
#: initial wavepacket $\Psi$.
parameters = [ (P, Q, S, 1.0, -5.0) , (P, Q, S, 1.0, -5.0) ]


# Specific for Fourier
# ====================

#: The number of grid nodes $\gamma_i$ in position space.
ngn = 2**12

#: Scaling factor $f$ for the computational domain $\Omega$ in position
#: space. The interval in the position space is given by $[-f\pi, f\pi]$.
f = 5.0


# Specific for Hagedorn
# =====================

#: The number $K$ of basis functions $\phi_k$ used for Hagedorn wavepackets $\Phi$.
basis_size = 64

#: The leading component index $\chi$ of the eigenvalue $\lambda_\chi$ that
#: governs the propagation of the Hagedorn parameters $\Pi$ for homogeneous
#: wavepackets.
leading_component = 0


# Specific for Multi Hagedorn
# ===========================

# None, but basis_size applies here too.


# Output parameters
# =================

#: Filename of the output file that contains the grid nodes $\gamma_i$.
outfile_nodes = "nodes.dat"
#: Filename of the output file that contains the wavefunction $\psi_i$.
outfile_wavefunction = "wavefunction.dat"
#: Filename of the output file that contains the energies $E$.
outfile_energies = "energies.dat"
#: Filename of the output file that contains the operators $T$ and $V$.
outfile_operators = "operators.dat"
#: Filename of the output file that contains the hagedorn parameters $\Pi_i$.
outfile_parameters = "parameters.dat"
#: Filename of the output file that contains the hagedorn coefficients $c^i$.
outfile_coefficients = "coefficients.dat"

#: Write data to disk only each $n$-th timestep.
write_nth = 1
