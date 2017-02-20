#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

#######################################
# Plot 1: Dimension analysis
#######################################

D = [ 2,3,4,5 ]
time_D = [ 0.08,5.12,24.06,778.75 ]
time_D = [ 0.0448, 0.3493, 24.0235, 2105.5222 ]

fig = plt.figure()
ax = fig.gca()

ax.semilogy(D, time_D, 'k-o')

# plt.margins(x=0.1, y=0.1)
ax.set_xlim([1.5,5.5])
ax.set_ylim([1e-2,1e4])
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# ax.set_xlim([0,1])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.set_title("Compute Time vs. Dimension of Wave Packet")
ax.grid(True)
ax.set_xlabel(r"Dimension $D$")
ax.set_ylabel(r"Compute time $t$ [s]")
fig.savefig("dimension_analysis.png")
plt.show()
plt.close(fig)



#######################################
# Plot 2: Coefficient Analysis
#######################################

size_coef = np.array([ 1,2,4,7,8,10,15,18,34 ])
time_python = np.array([47.155, 52.934, 65.351, 84.075, 90.260, 102.531, 133.415, 151.438, 249.749])
time_cpp = np.array([1.3905, 1.3817, 1.4386, 1.5122, 1.4568, 1.6049, 1.7763, 1.8147, 2.2168])
speedup = time_python / time_cpp

print(speedup)

fig, ax = plt.subplots(2,1)

ax[0].loglog(size_coef, time_python, 'b-o', label=r"Python")
ax[0].loglog(size_coef, time_cpp, 'g-o', label=r"C++")
ax[1].loglog(size_coef, speedup, 'r-o')

# ax.set_xlim([0,1])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax[0].set_xlim([.8,40])
ax[1].set_xlim([.8,40])
ax[1].set_ylim([25,160])
ax[1].set_yscale('log', basey=2)
ax[0].set_title("Cost of IntSplit splitting coefficients")
ax[0].legend(loc='upper left')
ax[0].grid(True)
ax[1].grid(True)
ax[0].set_ylabel(r"Compute Time $t$ [s]")
ax[1].set_ylabel(r"Speedup")
ax[1].set_xlabel(r"Size of coefficient array")
fig.savefig("coefficient_analysis.png")
plt.show()
plt.close(fig)



#######################################
# Plot 3: Error analysis
#######################################

n_steps = [ 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.007812, 0.003906, 0.001953, 0.000977, 0.000488, 0.000244 ]
n_steps_morse = [ 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.007812, 0.003906, 0.001953 ]

# harmonic LT
error_harmonic_1D_lt_hagedorn = [ 9.545477e-07, 3.818193e-06, 1.527278e-05, 6.109122e-05, 2.443662e-04, 9.774862e-04, 3.910282e-03, 1.564622e-02, 6.264607e-02, 2.502071e-01, 9.070318e-01]
error_harmonic_1D_lt_mg4 = [ 3.968109e-12, 3.105810e-12, 2.779794e-12, 8.872414e-13, 3.629015e-12, 2.571130e-11, 3.863204e-10, 6.157092e-09, 9.848602e-08, 1.575815e-06, 2.521706e-05]
error_harmonic_1D_lt_mcl42 = [ 4.170521e-12, 2.910990e-12, 2.896429e-12, 7.860211e-13, 3.391014e-12, 2.569097e-11, 3.861969e-10, 6.156957e-09, 9.848581e-08, 1.575815e-06, 2.521706e-05]
error_harmonic_1D_lt_mcl84 = [ 4.424280e-12, 7.103594e-13, 4.890004e-12, 3.017013e-13, 4.049679e-12, 2.928067e-11, 4.425939e-10, 7.059074e-09, 1.129233e-07, 1.806804e-06, 2.891260e-05]
error_harmonic_1D_lt_pre764 = [ 3.154724e-12, 1.388741e-12, 2.953003e-12, 1.909897e-12, 4.346275e-12, 4.220303e-11, 6.432055e-10, 1.007762e-08, 1.554063e-07, 2.301564e-06, 3.102992e-05]
error_harmonic_1D_lt_semiclassical = [ 6.570944e-13, 2.810143e-12, 8.654158e-13, 2.010771e-12, 3.424029e-12, 2.499841e-11, 3.718457e-10, 5.920513e-09, 9.470839e-08, 1.515352e-06, 2.424855e-05]

# torsional LT
error_torsional_1D_lt_hagedorn = [ 4.413159e-08, 1.766168e-07, 7.065577e-07, 2.826307e-06, 1.130505e-05, 4.521597e-05, 1.807949e-04, 7.220749e-04, 2.870631e-03, 1.120047e-02, 4.033724e-02]
error_torsional_1D_lt_mg4 = [ 3.389891e-11, 3.717412e-11, 3.493770e-11, 3.225172e-11, 3.261378e-11, 3.397044e-11, 5.169600e-11, 3.423753e-10, 5.017209e-09, 7.981489e-08, 1.276773e-06]
error_torsional_1D_lt_mcl42 = [ 3.379270e-11, 3.702897e-11, 3.479613e-11, 3.327578e-11, 4.706530e-11, 1.434777e-10, 5.594621e-10, 2.195010e-09, 9.091761e-09, 7.849469e-08, 1.247707e-06]
error_torsional_1D_lt_mcl84 = [ 2.446365e-11, 3.216573e-11, 3.219421e-11, 3.325376e-11, 3.309425e-11, 3.384717e-11, 5.432106e-11, 3.926380e-10, 5.815999e-09, 9.259400e-08, 1.481307e-06]
error_torsional_1D_lt_pre764 = [ 3.414883e-11, 3.064713e-11, 3.417420e-11, 3.024380e-11, 3.211200e-11, 3.464738e-11, 6.443673e-11, 5.365296e-10, 7.648273e-09, 1.077038e-07, 1.305210e-06]
error_torsional_1D_lt_semiclassical = [ 3.279210e-11, 3.760648e-11, 3.617805e-11, 6.278279e-11, 1.945545e-10, 7.432790e-10, 2.947945e-09, 1.180447e-08, 4.801044e-08, 2.158989e-07, 1.608904e-06]

# morse LT
error_morse_1D_lt_hagedorn = [ 1.325977e-08, 5.307810e-08, 2.123536e-07, 8.494546e-07, 3.397868e-06, 1.359167e-05, 5.436919e-05, 2.175166e-04]
error_morse_1D_lt_mg4 = [ 9.032965e-06, 1.806527e-05, 3.612797e-05, 7.224567e-05, 1.444503e-04, 2.887368e-04, 5.768199e-04, 1.151037e-03]
error_morse_1D_lt_mcl42 = [ 9.032949e-06, 1.806521e-05, 3.612772e-05, 7.224467e-05, 1.444463e-04, 2.887210e-04, 5.767573e-04, 1.150793e-03]
error_morse_1D_lt_mcl84 = [ 1.208038e-05, 2.416038e-05, 4.831927e-05, 9.663264e-05, 1.932418e-04, 3.863905e-04, 7.724157e-04, 1.543424e-03]
error_morse_1D_lt_pre764 = [ 1.357298e-05, 2.716454e-05, 5.440344e-05, 1.091042e-04, 2.193969e-04, 4.435388e-04, 9.059879e-04, 1.887033e-03]
error_morse_1D_lt_semiclassical = [ 1.068625e-05, 2.137201e-05, 4.274209e-05, 8.547655e-05, 1.709227e-04, 3.417245e-04, 6.829718e-04, 1.364083e-03]

#########################################

# harmonic Y4
error_harmonic_1D_y4_hagedorn = [ 9.545477e-07, 3.818193e-06, 1.527278e-05, 6.109122e-05, 2.443662e-04, 9.774862e-04, 3.910282e-03, 1.564622e-02, 6.264607e-02, 2.502071e-01, 9.070318e-01]
error_harmonic_1D_y4_mg4 = [ 3.968109e-12, 3.105810e-12, 2.779794e-12, 8.872414e-13, 3.629015e-12, 2.571130e-11, 3.863204e-10, 6.157092e-09, 9.848602e-08, 1.575815e-06, 2.521706e-05]
error_harmonic_1D_y4_mcl42 = [ 4.170521e-12, 2.910990e-12, 2.896429e-12, 7.860211e-13, 3.391014e-12, 2.569097e-11, 3.861969e-10, 6.156957e-09, 9.848581e-08, 1.575815e-06, 2.521706e-05]
error_harmonic_1D_y4_mcl84 = [ 4.424280e-12, 7.103594e-13, 4.890004e-12, 3.017013e-13, 4.049679e-12, 2.928067e-11, 4.425939e-10, 7.059074e-09, 1.129233e-07, 1.806804e-06, 2.891260e-05]
error_harmonic_1D_y4_pre764 = [ 3.154724e-12, 1.388741e-12, 2.953003e-12, 1.909897e-12, 4.346275e-12, 4.220303e-11, 6.432055e-10, 1.007762e-08, 1.554063e-07, 2.301564e-06, 3.102992e-05]
error_harmonic_1D_y4_semiclassical = [ 6.570944e-13, 2.810143e-12, 8.654158e-13, 2.010771e-12, 3.424029e-12, 2.499841e-11, 3.718457e-10, 5.920513e-09, 9.470839e-08, 1.515352e-06, 2.424855e-05]

# torsional Y4
error_torsional_1D_y4_hagedorn = [ 4.413159e-08, 1.766168e-07, 7.065577e-07, 2.826307e-06, 1.130505e-05, 4.521597e-05, 1.807949e-04, 7.220749e-04, 2.870631e-03, 1.120047e-02, 4.033724e-02]
error_torsional_1D_y4_mg4 = [ 3.389891e-11, 3.717412e-11, 3.493770e-11, 3.225172e-11, 3.261378e-11, 3.397044e-11, 5.169600e-11, 3.423753e-10, 5.017209e-09, 7.981489e-08, 1.276773e-06]
error_torsional_1D_y4_mcl42 = [ 3.379270e-11, 3.702897e-11, 3.479613e-11, 3.327578e-11, 4.706530e-11, 1.434777e-10, 5.594621e-10, 2.195010e-09, 9.091761e-09, 7.849469e-08, 1.247707e-06]
error_torsional_1D_y4_mcl84 = [ 2.446365e-11, 3.216573e-11, 3.219421e-11, 3.325376e-11, 3.309425e-11, 3.384717e-11, 5.432106e-11, 3.926380e-10, 5.815999e-09, 9.259400e-08, 1.481307e-06]
error_torsional_1D_y4_pre764 = [ 3.414883e-11, 3.064713e-11, 3.417420e-11, 3.024380e-11, 3.211200e-11, 3.464738e-11, 6.443673e-11, 5.365296e-10, 7.648273e-09, 1.077038e-07, 1.305210e-06]
error_torsional_1D_y4_semiclassical = [ 3.279210e-11, 3.760648e-11, 3.617805e-11, 6.278279e-11, 1.945545e-10, 7.432790e-10, 2.947945e-09, 1.180447e-08, 4.801044e-08, 2.158989e-07, 1.608904e-06]

# morse Y4
error_morse_1D_y4_hagedorn = [ 1.325977e-08, 5.307810e-08, 2.123536e-07, 8.494546e-07, 3.397868e-06, 1.359167e-05, 5.436919e-05, 2.175166e-04]
error_morse_1D_y4_mg4 = [ 1.460253e-11, 1.472816e-11, 1.457033e-11, 1.520796e-11, 1.527166e-11, 3.794749e-11, 5.579321e-10, 8.913417e-09]
error_morse_1D_y4_mcl42 = [ 2.962581e-10, 1.182166e-09, 4.726521e-09, 1.890463e-08, 7.561734e-08, 3.024688e-07, 1.209888e-06, 4.839784e-06]
error_morse_1D_y4_mcl84 = [ 1.517644e-11, 1.480756e-11, 1.431413e-11, 1.569338e-11, 1.420991e-11, 2.342160e-11, 2.857094e-10, 4.524417e-09]
error_morse_1D_y4_pre764 = [ 1.579363e-11, 1.498456e-11, 1.553254e-11, 1.435766e-11, 1.516359e-11, 2.999104e-11, 4.127790e-10, 6.227530e-09]
error_morse_1D_y4_semiclassical = [ 1.125289e-09, 4.496678e-09, 1.798135e-08, 7.192046e-08, 2.876774e-07, 1.150712e-06, 4.602971e-06, 1.841389e-05]

#########################################

# torsional 2D


fig = plt.figure()
ax = fig.gca()

ax.loglog(n_steps, error_harmonic_1D_lt_hagedorn, 'r-o', label=r"Hagedorn")
ax.loglog(n_steps, error_harmonic_1D_lt_semiclassical, 'm-o', label=r"Semiclassical")
ax.loglog(n_steps, error_harmonic_1D_lt_mg4, 'b-o', label=r"Magnus (4)")
ax.loglog(n_steps, error_harmonic_1D_lt_mcl42, 'g-o', label=r"McLachlan (4,2)")
ax.loglog(n_steps, error_harmonic_1D_lt_mcl84, 'k-o', label=r"McLachlan (8,4)")
ax.loglog(n_steps, error_harmonic_1D_lt_pre764, 'c-o', label=r"Processing (7,6,4)")

# lgd = ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
ax.set_xlim([5e-1,1e-4])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.set_title(r"Convergence for Harmonic 1D potential (LT splitting)")
ax.grid(True)
ax.set_xlabel(r"Size of time step $\Delta t$")
ax.set_ylabel(r"$L_2$ error $\frac{\| u (x) - u_* (x) \|}{\| u_* (x) \|}$")
# fig.savefig("convergence_harmonic_1D_lt.png",bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig("convergence_harmonic_1D_lt.png")
plt.show()
plt.close(fig)


fig = plt.figure()
ax = fig.gca()

ax.loglog(n_steps, error_torsional_1D_lt_hagedorn, 'r-o', label=r"Hagedorn")
ax.loglog(n_steps, error_torsional_1D_lt_semiclassical, 'm-o', label=r"Semiclassical")
ax.loglog(n_steps, error_torsional_1D_lt_mg4, 'b-o', label=r"Magnus (4)")
ax.loglog(n_steps, error_torsional_1D_lt_mcl42, 'g-o', label=r"McLachlan (4,2)")
ax.loglog(n_steps, error_torsional_1D_lt_mcl84, 'k-o', label=r"McLachlan (8,4)")
ax.loglog(n_steps, error_torsional_1D_lt_pre764, 'c-o', label=r"Processing (7,6,4)")

# lgd = ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
ax.set_xlim([5e-1,1e-4])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.set_title(r"Convergence for Torsional 1D potential (LT splitting)")
ax.grid(True)
ax.set_xlabel(r"Size of time step $\Delta t$")
ax.set_ylabel(r"$L_2$ error $\frac{\| u (x) - u_* (x) \|}{\| u_* (x) \|}$")
# fig.savefig("convergence_torsional_1D_lt.png",bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig("convergence_torsional_1D_lt.png")
plt.show()
plt.close(fig)


fig = plt.figure()
ax = fig.gca()

ax.loglog(n_steps_morse, error_morse_1D_lt_hagedorn, 'r-o', label=r"Hagedorn")
ax.loglog(n_steps_morse, error_morse_1D_lt_semiclassical, 'm-o', label=r"Semiclassical")
ax.loglog(n_steps_morse, error_morse_1D_lt_mg4, 'b-o', label=r"Magnus (4)")
ax.loglog(n_steps_morse, error_morse_1D_lt_mcl42, 'g-o', label=r"McLachlan (4,2)")
ax.loglog(n_steps_morse, error_morse_1D_lt_mcl84, 'k-o', label=r"McLachlan (8,4)")
ax.loglog(n_steps_morse, error_morse_1D_lt_pre764, 'c-o', label=r"Processing (7,6,4)")

# lgd = ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
ax.set_xlim([5e-1,1e-3])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.set_title(r"Convergence for Morse 1D potential (LT splitting)")
ax.grid(True)
ax.set_xlabel(r"Size of time step $\Delta t$")
ax.set_ylabel(r"$L_2$ error $\frac{\| u (x) - u_* (x) \|}{\| u_* (x) \|}$")
# fig.savefig("convergence_morse_1D_lt.png",bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig("convergence_morse_1D_lt.png")
plt.show()
plt.close(fig)



fig = plt.figure()
ax = fig.gca()

ax.loglog(n_steps, error_harmonic_1D_y4_hagedorn, 'r-o', label=r"Hagedorn")
ax.loglog(n_steps, error_harmonic_1D_y4_semiclassical, 'm-o', label=r"Semiclassical")
ax.loglog(n_steps, error_harmonic_1D_y4_mg4, 'b-o', label=r"Magnus (4)")
ax.loglog(n_steps, error_harmonic_1D_y4_mcl42, 'g-o', label=r"McLachlan (4,2)")
ax.loglog(n_steps, error_harmonic_1D_y4_mcl84, 'k-o', label=r"McLachlan (8,4)")
ax.loglog(n_steps, error_harmonic_1D_y4_pre764, 'c-o', label=r"Processing (7,6,4)")

# lgd = ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
ax.set_xlim([5e-1,1e-4])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.set_title(r"Convergence for Harmonic 1D potential (Y4 splitting)")
ax.grid(True)
ax.set_xlabel(r"Size of time step $\Delta t$")
ax.set_ylabel(r"$L_2$ error $\frac{\| u (x) - u_* (x) \|}{\| u_* (x) \|}$")
# fig.savefig("convergence_harmonic_1D_y4.png",bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig("convergence_harmonic_1D_y4.png")
plt.show()
plt.close(fig)


fig = plt.figure()
ax = fig.gca()

ax.loglog(n_steps, error_torsional_1D_y4_hagedorn, 'r-o', label=r"Hagedorn")
ax.loglog(n_steps, error_torsional_1D_y4_semiclassical, 'm-o', label=r"Semiclassical")
ax.loglog(n_steps, error_torsional_1D_y4_mg4, 'b-o', label=r"Magnus (4)")
ax.loglog(n_steps, error_torsional_1D_y4_mcl42, 'g-o', label=r"McLachlan (4,2)")
ax.loglog(n_steps, error_torsional_1D_y4_mcl84, 'k-o', label=r"McLachlan (8,4)")
ax.loglog(n_steps, error_torsional_1D_y4_pre764, 'c-o', label=r"Processing (7,6,4)")

# lgd = ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
ax.set_xlim([5e-1,1e-4])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.set_title(r"Convergence for Torsional 1D potential (Y4 splitting)")
ax.grid(True)
ax.set_xlabel(r"Size of time step $\Delta t$")
ax.set_ylabel(r"$L_2$ error $\frac{\| u (x) - u_* (x) \|}{\| u_* (x) \|}$")
# fig.savefig("convergence_torsional_1D_y4.png",bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig("convergence_torsional_1D_y4.png")
plt.show()
plt.close(fig)


fig = plt.figure()
ax = fig.gca()

ax.loglog(n_steps_morse, error_morse_1D_y4_hagedorn, 'r-o', label=r"Hagedorn")
ax.loglog(n_steps_morse, error_morse_1D_y4_semiclassical, 'm-o', label=r"Semiclassical")
ax.loglog(n_steps_morse, error_morse_1D_y4_mg4, 'b-o', label=r"Magnus (4)")
ax.loglog(n_steps_morse, error_morse_1D_y4_mcl42, 'g-o', label=r"McLachlan (4,2)")
ax.loglog(n_steps_morse, error_morse_1D_y4_mcl84, 'k-o', label=r"McLachlan (8,4)")
ax.loglog(n_steps_morse, error_morse_1D_y4_pre764, 'c-o', label=r"Processing (7,6,4)")

# lgd = ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
ax.set_xlim([5e-1,1e-3])
# ax.set_ylim(view[2:])
# ax.ticklabel_format(style="sci", scilimits=(0, 0), axis="y")
ax.set_title(r"Convergence for Morse 1D potential (Y4 splitting)")
ax.grid(True)
ax.set_xlabel(r"Size of time step $\Delta t$")
ax.set_ylabel(r"$L_2$ error $\frac{\| u (x) - u_* (x) \|}{\| u_* (x) \|}$")
# fig.savefig("convergence_morse_1D_y4.png",bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig("convergence_morse_1D_y4.png")
plt.show()
plt.close(fig)
