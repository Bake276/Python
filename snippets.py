import random
# from random import choice

############# GENERAL ###############

# Tenary Operator

def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)



# max/min with key lambda and default value

def longest_name(names):
    return max(names, key=len)
	# return max(names, key=lambda name: len(name), default=0)

# print(longest_name(["Mel", "Bake", "Sammy", "Manfred"]))



# map

def square(arr):
    squared = map(lambda x: x**2, arr)
    return list(squared)

# print(square([1, 2, 3, 4]))



# filter (True of False)

def even(arr):
    evens = filter(lambda x: x % 2 == 0, arr)
    return list(evens)

# print(even([1, 2, 3, 4]))



#filter by type

def filter_list(l):
    # return [val for val in l if type(val) is str]
    return [val for val in l if isinstance(val, int)]

# print(filter_list([1, 2, "hello", 3, "welcome"]))



# ZIP

# put together 1 string from 2 strings with zip

def interleave(string1, string2):
	# return "".join([char[0] + char[1] for char in  zip(string1, string2)])
	return "".join("".join(chars) for chars in zip(string1, string2))

# print(interleave("lzr", "iad"))



# calculate grade, return dict with student and highest grade

def calculate_grade(students, midterms, finals):
	return {grade[0]: max(grade[1], grade[2]) for grade in zip(students, midterms, finals)}

# print(calculate_grade(["Dan", "Angie", "kate"], [80, 91, 78], [98, 89, 53]))



# Recursion

def factorial(num):

	if num == 1:
		return num

	return num * factorial(num - 1)


# print(factorial(5))



def get_count(sentence):
    # 	#gernerator, ergibt true(1) false(0); klappt auch mit array
    return sum((c.lower() in "aeiou" for c in sentence))

    # 	#alternative lösung mit array und len
    return len([char for char in sentence if char.lower() in "aeiou"])

# print(get_count("xxaeiouxAEIOUx"))



# alternative in int

def sum_str(a, b):
    # if not a.isdigit(): a = 0
    # if not b.isdigit(): b = 0

    # return str(int(a) + int(b))

    return str(int(a or 0) + int(b or 0))

# print(sum_str("2", "5"))
# print(sum_str("2", ""))



# unpacking tuple in for loop

def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data]

# print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))








############ NUMBERS ##############

# print divisors or prime

def divisors(integer):
	return [num for num in range(2, integer) if integer % num == 0] or f"{integer} is prime"



# sum a numbers digits

def sum_digits(number):
    return sum(int(num) for num in list(str(abs(number))))





############ STRINGS #############

# Format

mad_libs = "{} laughed at the {} {}."
# print(mad_libs.format("Bake", "dirty", "joke"))

mad_libs = "{2} laughed at the {1} {0}."
# print(mad_libs.format("Bake", "dirty", "joke"))

mad_libs = "{name} laughed at the {adjective} {noun}."
# print(mad_libs.format(name="Bake", adjective="dirty", noun="joke"))

# 4 decimals
print(f"Division: {(2 / 3):.4f}")



def correct(string):
    def change(char):
        if char == "5":
            return "S"
        if char == "0":
            return "O"
        if char == "1":
            return "I"
        return char

    return "".join(map(change, string))

    # return string.translate(str.maketrans("501", "SOI"))

# print(correct("51NGAP0RE"))



def DNA_strand(dna):

	changes = {
		"A": "T",
		"T": "A",
		"C": "G",
		"G": "C"
	}

	return "".join(changes[char] for char in dna)

# print(DNA_strand("ATTGC"))



def disemvowel(string):
    return "".join(char for char in string if char.lower() not in "aeiou")

# print(disemvowel("This website is for losers LOL!"))



def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
   
# print(to_camel_case("the-stealth-warrior"))
# print(to_camel_case("The_stealth_warrior"))
# print(to_camel_case(""))





def order(sentence):
    solution = []
    sentence_arr = sentence.split(" ")

    for i in range(1, len(sentence_arr) + 1):
        for word in sentence_arr:  
            if str(i) in word:
                solution.append(word)    

    return " ".join(solution)
  

# print(order("is2 Thi1s T4est 3a"))






######### LISTS ###############


# List Comprehension with if else

def fizz(n):
	return ["Fizz" if num % 3 == 0 else str(num) for num in range(1, n + 1)]

# print(fizz(6))



# sort array of strings by length in reverse order

def sort_by_length(arr):
	return sorted(arr, key=len, reverse=reversed)

# print(sort_by_length(["I", "am", "groot", "h", "the", "hellohello", "to", "be"]))



# flatten and sort array -> 2 ways

def flatten_and_sort(list_of_arrays):
    return sorted([number for arr in list_of_arrays for number in arr])

    # flat_list = []

    # for arr in list_of_arrays:
    #     for number in arr:
    #         flat_list.append(number)

    # return sorted(flat_list)


# print(flatten_and_sort([[3, 5, 1], [2, 9, 4], [8, 6, 7]]))





############ DICTIONARIES ##############


# make dict with all same values

def fromkeys_example():
     test_dict = dict.fromkeys("abcd", 0)
     test_dict = dict.fromkeys(["a", "b", "c"], 10)


# sum of dict values

def plenty_of_arguments(a, b, **kwargs):
    return a + b + sum(kwargs.values())

# print(plenty_of_arguments(30, 20, c = 30, d = 30))



def sort_by_dict_values(dictionary):
	#returns list of sorted values
	# return sorted(dictionary.values(), reverse=True)
	
	# returns list of keys sorted by value
	# return sorted(dictionary, key=dictionary.get, reverse=True)

	# returns list with (key, value) tuple
	# return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

	# returns dict
	return {key: value for key, value in sorted(dictionary.items(), key=lambda x: x[1], reverse=True)}


# print(sort_by_dict_values({"Angie": 12, "Tom": 4, "Larry": 6, "Lisa": 24}))



# dict comprehension

test_dict = {"first": 1, "second": 2, "third": 3}
squared = {key: value**2 for key, value in test_dict.items()}

# print(squared)



# dict comprehension with logic (logic can also be as key)

{num: ("even" if num % 2 == 0 else "odd") for num in range(1, 11)}



# iter makes iterator and next gives value and sets state of iterator

def get_single_dict_value(dict_obj):
	key = next(iter(dict_obj.keys()))
	value = next(iter(dict_obj.values()))

	return (key, value)

print(get_single_dict_value({"name": "Thorsten"}))




def pairs(l):
    count_map = {}

    for num in l:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    counter = 0

    for val in count_map.values():
        counter += val * (val - 1) // 2

    return counter

# print(pairs([1, 2, 3, 1, 1, 3]))



def playlist():
	song1 = {
		"artist": "Gigi D'agosino",
		"title": "L'amour toujour",
		"album": "Best of Gigi",
		"date": "2017-10-31",
		"time": "03:37",
	}

	song2 = {
		"artist": "Cindy Lauper",
		"title": "Girls wanna have fun",
		"album": "Cindy's Best",
		"date": "2010-05-24",
		"time": "04:02",
	}

	song3 = {
		"artist": "Metallica",
		"title": "Hells Bells",
		"album": "Best of Metallica",
		"date": "2005-02-16",
		"time": "05:37",
	}


	playlist = {
		"title": "Bake's songs",
		"author": "Bake",
		"items": [song1, song2, song3],
	}

	# print(playlist["items"][2]["artist"][1])


	durations = [value["time"] for value in playlist["items"]]
	# print(durations)

	minutes = sum(int(minute.split(":")[0]) for minute in durations)
	seconds_total = sum(int(second.split(":")[1]) for second in durations)
	minutes_from_seconds = seconds_total // 60
	seconds = seconds_total % 60

	playlist_length = f"{minutes + minutes_from_seconds}:{seconds}"

	return playlist_length

# playlist()




#update grades from exam dict, insert new grade in first position of list, if not present insert None
# exam.get puts None as a default if grade isn't there

def update_grades():
	grades = {
		'John': [90, 95, 98],
		'Eric': [86, 84, 92],
		'Michael': [90, 89, 85]
	}

	exam = {
		'Eric': 99,
		'John': 100
	}

	for key, value in grades.items():
		value.insert(0, exam.get(key, None))

	return grades

# print(update_grades())



def count_the_letters():

	sentence = "'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation of negation) they are a complete set of basic logical operations — all other logical operations, no matter how complex, can be obtained by suitable combinations of these."

	letter_count = {}

	for char in sentence:
		if char.isalpha():
			#another example of the get method  where it chechs if the value is already there and puts 0 if not
			#no if char in letter_count nesseccary
			letter_count[char] = letter_count.get(char, 0) + 1

	return letter_count

# print(count_the_letters())



