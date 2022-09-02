departamento_aux=["Amazonas",
"Antioquia",
"Arauca",
"Atlántico",
"Bogotá",
"Bolívar",
"Boyacá",
"Caldas",
"Caquetá",  
"Casanare",
"Cauca",
"Cesar",
"Chocó",
"Córdoba",
"Cundinamarca",
"Guainía",  
"Guaviare",
"Huila",
"La Guajira",
"Magdalena",
"Meta",
"Nariño",
"Norte de Santander",
"Putumayo",
"Quindío",
"Risaralda",
"San Andrés y Providencia",
"Santander",
"Sucre",
"Tolima",
"Valle del Cauca",
"Vaupés",
"Vichada"]

def promedioA(lista):
    count = 0
    prom = {}
    for dep in departamento_aux:
        for p in lista:
            if p.departamento == dep:
                if prom.get(dep) != None:
                    prom.update({dep:p.prob_aprob+(prom.get(dep))})
                else:
                    prom.update({dep:p.prob_aprob})
                count+=1

        if prom.get(dep) != None:
            prom.update({dep:prom.get(dep)/count})
        count=0

    return prom

def promedioP(lista):
    count = 0
    prom = {}
    for dep in departamento_aux:
        for p in lista:
            if p.departamento == dep:
                if prom.get(dep) != None:
                    prom.update({dep:p.prob_perd+(prom.get(dep))})
                else:
                    prom.update({dep:p.prob_perd})
                count+=1

        if prom.get(dep) != None:
            prom.update({dep:prom.get(dep)/count})
        count=0

    return prom

def promedioD(lista):
    count = 0
    prom = {}
    for dep in departamento_aux:
        for p in lista:
            if p.departamento == dep:
                if prom.get(dep) != None:
                    prom.update({dep:p.prob_dese+(prom.get(dep))})
                else:
                    prom.update({dep:p.prob_dese})
                count+=1

        if prom.get(dep) != None:
            prom.update({dep:prom.get(dep)/count})
        count=0

    return prom