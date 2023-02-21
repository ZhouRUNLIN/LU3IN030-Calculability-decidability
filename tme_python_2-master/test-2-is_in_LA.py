from automates_a_pile import *

a1_st = ["q0","q1","q2"]
a1_alph = ["a","b","c"]
a1_stack_alph = ["z0"]
a1_t_rel = [(("q0","z0","a"),("q0",["z0","z0"])),\
            (("q0","z0",None),("q1",["z0"])),\
            (("q1","z0","b"),("q1",["z0"])),\
            (("q1","z0",None),("q2",[])),\
            (("q2","z0","c"),("q2",[]))]
a1_init_st = "q0"
a1_init_stack = "z0"
a1_accept_mode = 0
a1_final_st = []
a1_eq_st = eq_atom

a1_a = (a1_st,a1_alph,a1_stack_alph,a1_t_rel,a1_init_st,\
        a1_init_stack,a1_accept_mode,a1_final_st,a1_eq_st)

a2_st = ["q0","q1"]
a2_alph = ["a","b"]
a2_stack_alph = ["Z","A","B"]
a2_t_rel = [(("q0","Z","a"),("q0",["A","Z"])),\
            (("q0","Z","b"),("q0",["B","Z"])),\
            (("q0","A","a"),("q0",["A", "A"])),\
            (("q0","A","b"),("q0",[])),\
            (("q0","B","a"),("q0",[])),\
            (("q0", "B", "b"),("q0", ["B","B"])),\
            (("q0", "Z", None), ("q1", []))]
a2_init_st = "q0"
a2_init_stack = "Z"
a2_accept_mode = 0
a2_final_st = []
a2_eq_st = eq_atom

a1_a = (a1_st,a1_alph,a1_stack_alph,a1_t_rel,a1_init_st,\
        a1_init_stack,a1_accept_mode,a1_final_st,a1_eq_st)
a2_a = (a2_st,a2_alph,a2_stack_alph,a2_t_rel,a2_init_st,\
        a2_init_stack,a2_accept_mode,a2_final_st,a2_eq_st)
#TD, ex 8

a2_a_f = (a2_st,a2_alph,a2_stack_alph,a2_t_rel,a2_init_st,\
        a2_init_stack,1,["q1"],a2_eq_st)

a3_st = ["q","p"]
a3_alph = ["0","1"]
a3_stack_alph = ["Z0","X"]
a3_t_rel = [(("q","Z0","0"),("q",["X","Z0"])),\
            (("q","X","0"),("q",["X","X"])),\
            (("q","X","1"),("q",["X"])),\
            (("q","X",None),("p",[])),\
            (("p","X",None),("p",[])),\
            (("p", "X", "1"),("p", ["X","X"])),\
            (("p", "Z0", "1"), ("p", []))]
a3_init_st = "q"
a3_init_stack = "Z0"
a3_accept_mode = 1
a3_final_st = ["p"]
a3_eq_st = eq_atom

a3_a=(a3_st, a3_alph, a3_stack_alph, a3_t_rel, a3_init_st,\
a3_init_stack, a3_accept_mode, a3_final_st, a3_eq_st)#TD3 ex 9

a3_a_p=(a3_st, a3_alph, a3_stack_alph, a3_t_rel, a3_init_st,\
a3_init_stack, 0, [], a3_eq_st)

a3_a_vide=(a3_st, a3_alph, a3_stack_alph, a3_t_rel, a3_init_st,\
a3_init_stack, a3_accept_mode, [], a3_eq_st)

print("\n\n----------------------------------------------\n\n")
print("Test 1 : Fonction is_in_LA")
print("------------------------------------------------")

assert(is_in_LA(a1_a,[])==True), "Erreur dans is_in_LA: test de l'enonce!"
assert(is_in_LA(a1_a,["a", "b", "c"])==True), "Erreur dans is_in_LA: test de l'enonce!"
assert(is_in_LA(a1_a,["a", "a", "b", "c", "c", "c"])==False), "Erreur dans is_in_LA: test de l'enonce!"
assert(is_in_LA(a1_a,["a", "a", "a", "c", "c", "c", "c"])==False), "Erreur dans is_in_LA: test de l'enonce!"
assert(is_in_LA(a1_a,["a", "a", "a", "c", "c", "c"])==True), "Erreur dans is_in_LA: test de l'enonce!"
assert(is_in_LA(a1_a,["a", "a", "b", "b", "b", "b", "b", "b", "b", "c", "c"])==True), "Erreur dans is_in_LA: test de l'enonce!"
assert(is_in_LA(a1_a,["b", "b", "a", "a", "a", "c", "c", "c"])==False), "Erreur dans is_in_LA: test de l'enonce!"
assert(is_in_LA(a1_a,["a", "c"])==True), "Erreur dans is_in_LA: test de l'enonce!"

print("\n\n----------------------------------------------\n\n")
print("Test 2 : Fonction is_in_LA acceptation par pile vide")
print("------------------------------------------------")
assert(is_in_LA(a2_a, [])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a, ["a", "b", "c"])==False), "Erreur dans is_in_LA:mauvais alphabet"
assert(is_in_LA(a2_a, ["a", "b", "a", "b"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a, ["a", "a", "a"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a, ["b", "b", "a", "a", "a", "a", "b", "b"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a, ["a", "a", "a", "b", "b", "b", "b", "b", "a", "b", "b", "b", "b", "a", "a", "a", "b", "a", "a"])==False), "Erreur dans is_in_LA"

print("\n\n----------------------------------------------\n\n")
print("Test 3 : Fonction is_in_LA acceptation par etat final")
print("------------------------------------------------")
assert(is_in_LA(a2_a_f, [])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a_f, ["a", "b", "c"])==False), "Erreur dans is_in_LA:mauvais alphabet"
assert(is_in_LA(a2_a_f, ["a", "b", "a", "b"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a_f, ["a", "a", "a"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a_f, ["b", "b", "a", "a", "a", "a", "b", "b"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a2_a_f, ["a", "a", "a", "b", "b", "b", "b", "b", "a", "b", "b", "b", "b", "a", "a", "a", "b", "a", "a"])==False), "Erreur dans is_in_LA"

print("\n\n----------------------------------------------\n\n")
print("Test 4 : Fonction is_in_LA acceptation par etat final")
print("------------------------------------------------")
assert(is_in_LA(a3_a, [])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a, ["0", "1"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a, ["0", "1", "0", "1"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a, ["0", "1", "0"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a, ["b", "b", "a", "a", "a", "a", "b", "b"])==False), "Erreur dans is_in_LA:mauvais alphabet"
assert(is_in_LA(a3_a, ["1", "1", "0", "0"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a, ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"])==True), "Erreur dans is_in_LA"

print("\n\n----------------------------------------------\n\n")
print("Test 5 : Fonction is_in_LA acceptation par pile vide")
print("------------------------------------------------")
assert(is_in_LA(a3_a_p, [])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_p, ["0", "1"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_p, ["0", "1", "0", "1"])==True), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_p, ["0", "1", "0"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_p, ["b", "b", "a", "a", "a", "a", "b", "b"])==False), "Erreur dans is_in_LA:mauvais alphabet"
assert(is_in_LA(a3_a_p, ["1", "1", "0", "0"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_p, ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"])==False), "Erreur dans is_in_LA"

print("\n\n----------------------------------------------\n\n")
print("Test 6 : Fonction is_in_LA acceptation par etat final")
print("------------------------------------------------")
assert(is_in_LA(a3_a_vide, [])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_vide, ["0", "1"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_vide, ["0", "1", "0", "1"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_vide, ["0", "1", "0"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_vide, ["b", "b", "a", "a", "a", "a", "b", "b"])==False), "Erreur dans is_in_LA:mauvais alphabet"
assert(is_in_LA(a3_a_vide, ["1", "1", "0", "0"])==False), "Erreur dans is_in_LA"
assert(is_in_LA(a3_a_vide, ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"])==False), "Erreur dans is_in_LA"
