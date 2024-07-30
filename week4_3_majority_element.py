def majority_element(elements):
    elements.sort()
    left, right = 0, len(elements) -1
    mid = (left+right)//2
    
    if elements[mid] == elements [mid-1] or elements[mid] == elements[mid+1]:
        if elements.count(elements[mid]) > len(elements)/2:
            return 1
        else:
            return 0
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
