l1 = [1, 2, 4, 'hello', 8]
def division (list):
    result = []
    for i in list:
        try:
            result.append(i/2)
        except Exception as e:
            print(e)
        finally:
            print(i)
    return result
print(division(l1))