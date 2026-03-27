import matplotlib.pyplot as plt
def selectionsort(array):
    n=len(array)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                min_index=j
        array [i],array[min_index]=array[min_index],array[i]
    return array
array=[]
n=int(input("how many elements you want in your array"))
for i in range(n):
    array.append(int(input("enter %d element"%i)))
print(f"before swapping:{array}")
array=selectionsort(array)
print(f"after swapping:{array}")
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("time complexity of selectionsort is O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
        
