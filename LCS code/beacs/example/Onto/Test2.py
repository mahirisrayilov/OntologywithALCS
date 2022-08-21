# from owlready2 import *

# onto = get_ontology("ALCS-Ontology.owl")
# onto.load()

# with onto:
#     class Drug(Thing): pass
#     class number_of_tablets(Drug >> int, FunctionalProperty): pass
#     class price(Drug >> float, FunctionalProperty): pass
#     class price_per_tablet(Drug >> float, FunctionalProperty): pass

#     rule = Imp()
#     rule.set_as_rule("""Drug(?d), price(?d, ?p), number_of_tablets(?d, ?n), divide(?r, ?p, ?n) -> price_per_tablet(?d, ?r)""")

# drug = Drug(number_of_tablets = 10, price = 25.0)
# sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)
# print(drug.price_per_tablet)


# from owlready2 import *
# onto_path.append("ALCS-Ontology.owl")
# onto = get_ontology("ALCS-Ontology.owl")
# onto.load()

# with onto:
#     class Drug(Thing): pass
#     class number_of_tablets(Drug >> int, FunctionalProperty): pass
#     class price(Drug >> float, FunctionalProperty): pass
#     class price_per_tablet(Drug >> float, FunctionalProperty): pass

#     rule = Imp()
#     rule.set_as_rule("""Drug(?d), price(?d, ?p), number_of_tablets(?d, ?n), divide(?r, ?p, ?n) -> price_per_tablet(?d, ?r)""")

# drug = Drug(number_of_tablets = 10, price = 25.0)
# sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)
# print(drug.price_per_tablet)


from owlready2 import *
onto_path.append("ALCS-Ontology.owl")
onto = get_ontology("ALCS-Ontology.owl")
onto.load()
with onto:
  class Math(Thing): pass
  class hasa(Math >> int, FunctionalProperty): pass
  class hasb(Math >> float, FunctionalProperty): pass
  class hasc(Math >> float, FunctionalProperty): pass

  rule = Imp()
  rule.set_as_rule("""Math(?m), hasa(?m,?a), hasb(?m,?b), divide(?x,?a,?b) -> hasc(?m,?x)""")
value = Math(hasa = 6, hasb = 2.0)
sync_reasoner_pellet(infer_property_values= True, infer_data_property_values= True)
print(value.hasc)