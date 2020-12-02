# En variabel med anvnet "a" som initielt får tildelt værdi "0" nul
a = 0
# En while løkke der gentages indtil a bliver større end 5
while a<=5:
    print(a)
    # en betinget sætning der tester for a større eller mindre end 3
    if a<3:
        print("a mindre end 3")
    elif a>3:
        print("a større end 3")
    else:
        print("a er lig 3")
    # der lægges 1 til værdien i variablen a
    a = a + 1
print("while er nu overstået")
    