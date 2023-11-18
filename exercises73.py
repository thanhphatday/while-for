string = input("Nhập chuỗi: ")
is_palindrome =True 
string = string.lower()
string = string.replace(" ", "")
for i in range(0, len(string) // 2):
  if string[i] != string[len(string) - i - 1]:
    is_palindrome =False
if is_palindrome:
  print(f"{string} is a palindrome ")
else:
  print(f"{string} is not palindrome")
  