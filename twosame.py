# lowest energy if the two qbits have the same value
#import
import dimod
# assign to variable exactsolver
exactsolver = dimod.ExactSolver()
# QUBO
Q = {(0,0):1,(1,1):1,(0,1):-2}
# assign results
results = exactsolver.sample_qubo(Q)
# print results
for sample, energy in (results.data(['sample', 'energy'])):
  print(sample, energy)


