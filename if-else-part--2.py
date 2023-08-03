mark = int(input("enter the mark: "))
if mark >80 and mark<=100:
  print("O grade")
elif mark>=60 and mark<100:
  print("A grade")
elif mark>=40 and mark<60:
  print("B grade")
elif mark>=35 and mark<40:
  print("C grade")
else:
  print("Fail")
