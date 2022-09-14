# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def is_predicate(x, y, z):
    print(f"Проверка истинности утверждения: ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not  y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
is_predicate(0, 0, 0)
is_predicate(0, 0, 1) 
is_predicate(0, 1, 1)
is_predicate(1, 1, 1)
is_predicate(1, 0, 1)
is_predicate(1, 1, 0)
is_predicate(0, 1, 0)
is_predicate(1, 0, 0)
