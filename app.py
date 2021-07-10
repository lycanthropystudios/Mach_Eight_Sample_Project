#Importing neccesary libs
import json
import requests as req
import unittest

#cheking information from JSON file - start
data = {}
url = "https://mach-eight.uc.r.appspot.com/"
try:
    res = req.get(url)
    data = json.loads(res.text)
except req.exceptions.RequestException as e:  # This is the correct syntax
    print("Somehting is happening with the URL: https://mach-eight.uc.r.appspot.com/ please check it")
    raise SystemExit(e)
    
#cheking information from JSON file - end

#sorting data - start
single = data['values']
data_sorted = sorted(single, key = lambda z: z ['h_in'])
#sorting data - end

#returns the current h_in for index
def getItem(indx):
    try:
        z = int(data_sorted[indx]['h_in'])
    except ValueError:
        return "value error"
    except IndexError:
        return "list index out of range"
    return z
#print the info about the matches found
def debug(z, i):
    print(str(data_sorted[z]['first_name'])+ " " + str(data_sorted[z]['last_name']) +"  "+  str(data_sorted[i]['first_name'])+ " " + str(data_sorted[i]['last_name']))
    #print(str(data_sorted[z]['first_name'])+ " " + str(data_sorted[z]['last_name']) + " " + str(data_sorted[z]['h_in'])+ " " + str(data_sorted[i]['first_name'])+ " " + str(data_sorted[i]['last_name']) + " " + str(data_sorted[i]['h_in']))
def main():
    num = 0
    print("Welcome to Match finder - Type 'x' or 'exit' to close\n  --- Type 'test' for testing\n")
    
    while True:
        num = input("Please enter a number: ")
        try:
            if num == "x" or num == "exit":
                break
            elif num == "test":
                unittest.main()
                continue
            num_in = int(num)
            if finder(num_in) == False:
                print("No matches found")
            continue
        except ValueError:
            print("Please enter only numbers")
    return num

#last index
list_s = len(data_sorted)-1
#middle index
list_mid = (list_s-1)//2
#minimun value for h_in
min_h = getItem(0)
#h_in value in the middle of list
mid_h = getItem(list_mid)
#maximun value for h_in
max_h = getItem(list_s)

#search - start
#returns bool data, False for not matching pairs
def finder(num):
    
    input_h = int(num)
    found = False
    if max_h + getItem(list_s-1) < input_h:
        #this happens when we have a big number imposible to get, so return the function here, is not necessary across all the JSON data
        return found
    # search for the match starting at middle position of the list
    if mid_h + getItem(list_mid+1) < input_h:
        #counter used to avoid duplicates on the matching search
        iter = 0
        #used for get the current status for each finded match
        check = False
        for i in range(list_mid, list_s):
            current = getItem(i)
            #with this we can know what's the minimun number that works for the matching searh
            result = abs(input_h - current)
            #used to avoid duplicates
            if check == True:
                iter+=1
                check = False
            #for this case if we're looking for the match at the right side
            if result >= min_h:
                for z in range(iter, list_mid):
                    #current item to compare
                    item = getItem(z)
                    
                    #breking the loop for big values that cannot be used for the matching
                    if item + current > input_h:
                        break
                    #when the pair of matches are found
                    elif item + current == input_h and z != i:
                        #print("current mayor"+ str(input_h) + " vs sum "+ str(item + current))
                        check = True
                        found = True
                        debug(z,i)
    # search for the match starting at zero position of the list
    else:
        iter = 0
        check = False
        for i in range(0, list_mid):
            current = getItem(i)
            result = abs(input_h - current)
            #used to avoid duplicates
            if check == True:
                iter+=1
                check = False
            #for this case if we're looking for the match at the left side
            if result >= min_h:
                for z in range(iter, list_mid):
                    #current item to compare
                    item = getItem(z)
                    #breking the loop for big values that cannot be used for the matching
                    if item + current > input_h:
                        break
                    #when the pair of matches are found
                    elif item + current == input_h and z != i:
                        #print("current menor"+ str(input_h) + " vs sum "+ str(item + current))
                        check = True
                        found = True
                        debug(z,i)
    return found
#search - end

"""
 ----------------------- TESTING ---------------------
"""
class TestApp(unittest.TestCase):

    def test_match_true(self):
        print("Set the number to 139")
        self.assertEqual(finder(139), True, "Should be True")

    def test_match_false(self):
        print("Set the number to 5000")
        self.assertEqual(finder(5000), False, "Should be False")
    
    def test_get_item(self):
        print("Getting the item 50 refers to the h_in = 74")
        self.assertEqual(getItem(50), 74, "Should be 74")
    
    def test_get_item(self):
        print("Getting the item 800 to simulate a index out of range exception")
        self.assertEqual(getItem(800), "list index out of range", "Should be 'list index out of range'")

if __name__ == '__main__':
    main()