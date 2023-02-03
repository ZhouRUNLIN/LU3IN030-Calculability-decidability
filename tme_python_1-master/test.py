from ensembles import *
from automates_finis import *

ex_A = ([0,1,2,3,4],\
        [(0,None,2),(0,None,3),(1,"b",1),(1,"a",2),(1,"b",3), \
         (1,"b",4),(3,"a",1),(3,"b",1),(3,None,2),(4,"a",0),(4,None,0)],\
        [0],[2],eq_atom)

(ex_S,ex_T,ex_I,ex_F,ex_eqS) = ex_A

print(eps_cl(ex_eqS,0,ex_T))
print(eps_cl(ex_eqS,1,ex_T))
print(eps_cl(ex_eqS,4,ex_T))
print(eps_cl_set(ex_eqS,[0,1],ex_T))

ex_RcoR = ([0,1,2,3,4,5],[(0,"a",1), (0,"a",2), (1,"a",1), (1,"b",5),\
                           (2,None,3), (3,"a",3), (3,"b",3), (4,"b",3),\
                           (4,"a",5)],\
            [0],[1,5],eq_atom)
            
print(reach_A(ex_RcoR))
print(co_reach_A(ex_RcoR))
