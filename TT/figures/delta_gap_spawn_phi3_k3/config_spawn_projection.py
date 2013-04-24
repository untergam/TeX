# The spawn algorithm
algorithm = "spawning_apost_na"

# Threshold for spawning (details see theory)
spawn_threshold = 1e-6

# Spawn a packet $\phi_order$ by copying over the norm
spawn_method = "projection"

# The order used in the parameter estimation
spawn_order = 3

# Basis size of the spawned packet
spawn_max_order = 16

# Components for which spawning is tried
spawn_components = [1]
