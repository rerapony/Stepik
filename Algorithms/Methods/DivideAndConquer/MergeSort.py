def mergesort(array):
    if len(array)<=1:
        return array
    else:
        mid = len(array)//2
        left = array[0:mid]
        right = array[mid:len(array)]
        return merge(mergesort(left), mergesort(right))
        
def merge(left, right):
    print(left, right)
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    l = r = 0
    merged = []  # list to build and return
    while len(merged) < (len(left)+len(right)):
        if r == len(right):
            # Reached the end of right
            # Append the remainder of left and break
            merged += left[l:]
            break
        elif l == len(left):
            # Reached the end of left
            # Append the remainder of right and break
            merged += right[r:]
            break
        elif left[l] <= right[r]:
            #Left value is smaller (or equal so it should be selected)
            merged.append(left[l])
            l += 1
        else:
            # Right value is bigger
            merged.append(right[r])
            r += 1
    return merged
