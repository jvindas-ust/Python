#Modifying inner array’s data with the index: 
#Idx 0,  1   , 2  , [   3   ], 4,  5
l = [2,"tres",True,["uno", 10],5,'Hi'] 
print ('Imprimir Lista: ' + str(l))
l[1] = 4
l2 = l[1]
print ('Imprimir cambio de dato en Indice 1: ' + str(l2))
#Slicing: Copy some information from an Array towards another one [begginingIndex:QuantityOfCopyingElements]: 
l3 = l[0:3] 
l7 = l[1:2]
print ('Imprimir Slicing de Indice 0, 3 Elementos: ' + str(l3))
#Copy some information from an Array towards another one by skipping some information [begginingIndex:QuantityOfCopyingElements:AmountOfSkipsPerIndex] 
l4 = l[0:3:2]
print ('Imprimir desde indice 0, 3 elementos, saltando cada 2 elementos: ' + str(l4))
#Copy some information from an Array towards another one by skipping each we want [begginingIndex::AmountOfSkipsPerIndex] 
l5 = [2,"tres",True,["uno", 10],6]
l6 = l5[0::2]
print ('Imprimir Lista 5: ' + str(l5))
print ('Imprimir la informacion saltando los datos consecutivos: ' + str(l6))