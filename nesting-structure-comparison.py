
def compare(original,other):
    def zeros(lst):
        # for i in range(len(lst)):
        #     if isinstance(lst[i], list):
        #         zeros(lst[i])
        #     else:
        #         lst[i] = 0
        # return lst
        return [zeros(lst[i]) if isinstance(lst[i], list) else 0 for i in range(len(lst))]
    return zeros(original) == zeros(other)
         
print(compare([1,[1,1]],[[2,2],2]))
print(compare([1,[1,1]],[2,[2,2]]))

"""
Final Solution:
---------------
def compare(original,other):
    def zeros(lst):
        return [zeros(lst[i]) if isinstance(lst[i], list) else 0 for i in range(len(lst))]
    try:
        return zeros(original) == zeros(other) and type(original) == type(other)
    except:
        return False
"""