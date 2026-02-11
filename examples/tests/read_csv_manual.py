# Test de lecture manuelle d'un fichier CSV sans pandas
# Objectif : comprendre comment ouvrir, lire, et découper un CSV

file = open("examples/sample_invoices.csv", "r", encoding="utf-8")
lines = file.readlines()

headers = lines[0].strip().split(",")

data = []

# On ignore la première ligne (les noms de colonnes)
for line in lines[1:]:
    values = line.strip().split(",")
    dico = dict(zip(headers, values))
    for k,v in dico.items():
        if k == "quantite" or k == "prix_unitaire" or k == "tva" :
            dico[v] = float(v)
    dico["montant_ht"] = dico["quantite"] * dico["prix_unitaire"]
    dico["montant_tva"] = dico["montant_ht"] * (dico["tva"] / 100)
    dico["montant_ttc"] = dico["montant_ht"] + dico["montant_tva"]

    data.append(dico)

    factures = {}

    for i in data:
        if i["invoice_id"] not in factures:
            factures[i["invoice_id"]] = [i]
        else :
            factures[i["invoice_id"]] += [i]
    
    for k,v in list(factures.items()) :
        total_ht = 0
        total_tva = 0
        total_ttc = 0

        for j in v :
            total_ht += j["montant_ht"]
            total_tva += j["montant_tva"]
            total_ttc += j["montant_ttc"]
            
        factures[i] = {
        "lignes": v,
        "total_ht": total_ht,
        "total_tva": total_tva,
        "total_ttc": total_ttc,
    }


file.close()