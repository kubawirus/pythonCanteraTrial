import cantera as ct
import numpy as np

g = ct.Solution('gri30.yaml')
II = [i for i,r in enumerate(g.reactions())
      if 'CO' in r.reactants and 'CO2' in r.products]

for i in II:
    print(g.reaction(i).equation)

g.TPX = 300, 101325, {'CH4':0.6, 'O2':1.0, 'N2':3.76}
g.equilibrate('HP')

print(g.net_rates_of_progress[II])

g.TP = g.T-100, None
print(g.net_rates_of_progress[II])

# g.TPX = 300, ct.one_atm, 'CH4:0.95, O2:2, N2:7.52'
# g.equilibrate('TP')
#
# rf = g.forward_rates_of_progress
# rr = g.reverse_rates_of_progress
#
# for i in range(g.n_reactions):
#     if g.is_reversible(i) and rf[i] != 0.0:
#         print(' %4i  %10.4g  ' % (i, (rf[i] - rr[i]) / rf[i]))
#
# g()

