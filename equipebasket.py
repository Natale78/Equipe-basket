def calculer_score(joueur):
    stats=joueur[2]
    score=stats[0] + stats[1] + stats[2]
    return score
equipe = [[("Lebron James"),23,[25,8,7]],[("Stephen Curry"),30,[30,5,9]]]
for joueur in equipe:
    nom=joueur[0]
    score=calculer_score(joueur)
print(f"{nom} a un score de {score}")