#!/usr/bin/env python
# coding: utf-8

# # Calculo De Emisions

# Vai calcular a emision de co2 na atmosfera

# In[15]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 0
DIAS_LABORAIS_SEMANAIS = 0
SEMANAS = 0

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM_MOTOELEC = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_MOTOELEC
print('O teu consumo en:', cantidade_de_emisions, 'gC02')


# In[ ]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 100
DIAS_LABORAIS_SEMANAIS = 5
SEMANAS = 48

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM_MOTOELEC = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_MOTOELEC
print('O teu consumo en:', cantidade_de_emisions, 'gC02')


# In[ ]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 20
DIAS_LABORAIS_SEMANAIS = 3
SEMANAS = 40

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM_MOTOELEC = 53

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_MOTOELEC
print('O teu consumo en:', cantidade_de_emisions, 'gC02')


# In[ ]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 6
DIAS_LABORAIS_SEMANAIS = 5
SEMANAS = 24

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM_MOTOELEC = 49

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_MOTOELEC
print('O teu consumo en:', cantidade_de_emisions, 'gC02')


# In[24]:


#!/usr/bin/env python

def emision(emision):
    KMS_DIARIOS = 100
    DIAS_LABORAIS_SEMANAIS = 5
    SEMANAS = 48
    cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * emision
    print('O teu consumo en:', cantidade_de_emisions, 'gC02')
    return cantidade_de_emisions
def resta(emision1,emision2):
    if(emision1>emision2):
        print('A resta e',emision1-emision2,'gC02 de diferencia')
    else: 
        print('A resta e',emision2-emision1,'gC02 de diferencia')
# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM_MOTOELEC = 17
totalmoto=emision(EMISION_X_KM_MOTOELEC)
EMISION_X_KM_BICIELEC = 3
totalbici=emision(EMISION_X_KM_BICIELEC)
resta(totalbici,totalmoto)






# In[ ]:




