def locate_duplicates(arr):
    dictionary = {}

    for element in arr:
        try:
            #get dictionary element and add one to it
            dictionary[element] += 1
        except:
            #dictionary if it already has an element of 1
            dictionary[element] = 1
    
    for element in dictionary:
        #if element is seen more than once
        if(dictionary[element] > 1):
            print(element, end=" ")
    print("\n")

if __name__ == "__main__":
    random_list = [40, 93, 82, 34, 50, 83, 48, 14, 
        20, 99, 11, 29, 65, 6, 37, 62, 97, 85, 81, 63, 15, 86,
        53, 71, 55, 96, 49, 45, 94, 77, 16, 10, 3, 31, 75, 78, 
        26, 71, 55]
    locate_duplicates(random_list)