import numpy

arr1 = numpy.array([2, 60, 10, 23, 40])
arr2 = numpy.array(["Jay", "Aru", "Rishu","Sachin","Ashish"])

print("Sum of arr1:", numpy.sum(arr1))
print("Mean of arr1:", numpy.mean(arr1))
print("Median of arr1:", numpy.median(arr1))
print("Max of arr1:", numpy.max(arr1))
print("Min of arr1:", numpy.min(arr1))
print("Appended:", numpy.append(arr1, 55))
print("Inserted:", numpy.insert(arr1, 2, 25))
print("Sorted:", numpy.sort(arr1))
print("Split:", numpy.char.split(arr2))
print("Concatenated:", numpy.concatenate((arr2, ["Sonu"])))
