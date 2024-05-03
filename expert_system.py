def selectDieseases(symptoms):
    diseases = {
        "allergies": ['sneezing', 'blocked nose', 'watery eyes', 'red eyes', 'coughing', 'red rash'],
        "asthma": ['wheezing', 'shortness of breath', 'tight chest'],
        "head tumor": ['severe headaches', 'seizures', 'mental changes', 'vision problem'],
        "chronic pain": ['diabetes', 'arthritis', 'back pain'],
        "dehydration": ['feeling thirsty', 'dry mouth', 'tiredness', 'strong smelling urine'],
        "food poisoning": ['nausea', 'vomiting', 'weakness', 'loss of appetite', 'aching muscles', 'chills','sneezing']
    }
    op = []
    for disease, dsymptoms in diseases.items():
        for symptom in symptoms:
            symptom = symptom.lower()
            if symptom in dsymptoms:
                if disease not in op: 
                    op.append(disease)
    return op

symptoms = []
for i in range(int(input("Enter number of symptoms : "))):
    symptom = input("")
    symptoms.append(symptom)
op = selectDieseases(symptoms)
if op:
    print("You may have diseases : ")
    count = 0
    for i in op:
        count+=1
        print(f"{count} : {i}")
    print("\n")