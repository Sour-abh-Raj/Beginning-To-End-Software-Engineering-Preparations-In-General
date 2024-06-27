def insertAnywhere1(list_, element, position):
    list_.insert(position, element)
    return list_

def insertAnywhere2(list_, element, position):
    return list_[:position] + [element] + list_[position:]

def insertFirst1(list_, element):
    return [element] + list_

def insertFirst2(list_, element):
    list_.insert(0, element)
    return list_

def insertLast1(list_, element):
    return list_ + [element]

def insertLast2(list_, element):
    list_.append(element)
    return list_

array = [1, 2, 3, 4, 5]
element = 6
position = 2
print(insertAnywhere1(array, element, position))
print(insertAnywhere2(array, element, position))
print(insertFirst1(array, element))
print(insertFirst2(array, element))
print(insertLast1(array, element))
print(insertLast2(array, element))

