# class Solution:
#     """
#     @param: chars: The letter array you should sort by Case
#     @return: nothing
#     """
#
# def sortLetters(self, chars):
#     # write your code here
#     chars.sort(key=lambda c: c.isupper())
# sortLetters(chars)
# chars = {'hhJJHKNjk'}
# print(chars)
s='asdf234GDSdsf23'
x=sorted(s, key=lambda x: (x.isdigit(),x.isdigit() and int(x) % 2 == 0,x.isupper(),x.islower(),x))
print(x)