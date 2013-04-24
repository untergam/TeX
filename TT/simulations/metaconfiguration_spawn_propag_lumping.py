# Global parameters that stay the same for all simulations:
GP = {}

GP["algorithm"] = "\"spawning_adiabatic\""
GP["potential"] = "\"eckart\""
GP["eps"] = "0.0234218**0.5"
GP["T"] = 70
GP["dt"] = 0.005
GP["parameters"] = "[ (0.1935842258501978j, 5.1657101481699996, 0.0, 0.24788547371, -7.55890450883) ]"
GP["coefficients"] = [ [(0,1.0)] ]
GP["basis_size"] = 300
GP["leading_component"] = 0
GP["matrix_exponential"] = "\"pade\""
GP["ngn"] = 4096
GP["f"] = 9.0
GP["write_nth"] = 20

# Local parameters that change with each simulation
LP = {}

LP["K0"] = [80, 100, 120]
LP["spawn_threshold"] = [0.2, 0.225, 0.25, 0.275, 0.29, 0.3, 0.31, 0.315, 0.32, 0.325]



