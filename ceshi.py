class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

chars = 'hhJJHKNjk'
x=sorted(chars,key=lambda c: c.isupper())
print(x)

# s='asdf234GDSdsf23'
# x=sorted(s, key=lambda x: (x.isdigit(),x.isdigit() and int(x) % 2 == 0,x.isupper(),x.islower(),x))
# print(x)