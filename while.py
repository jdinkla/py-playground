def f(i):
    print(f"Start {i}")
    while i < 3:
        print(f"Inc {i}")
        i += 1
        #if i == 2: break
    else:
        print(f"Else {i}")
    print(f"End {i}")

f(0)    
f(4)