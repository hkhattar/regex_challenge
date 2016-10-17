import re

def get_matching_words(regex):
    results = []
    words = [
        "baby",
        "baseball",
        "denver",
        "facetious",
        "issue",
        "mattress",
        "obsessive",
        "paranoia",
        "rabble",
        "union",
        "volleyball",
    ]
    for word in words:
        if re.search(regex, word):
            results.append(word)

    return results

my_expression = r"a"
print get_matching_words(my_expression)



my_expression = r"v"
print get_matching_words(my_expression)

my_expression = r"^[aeiou]"
print get_matching_words(my_expression)

my_expression = r"(\w)\1"
print get_matching_words(my_expression)

print "1 "
my_expression = r"ss"
print get_matching_words(my_expression)

print "2 "
my_expression = r"b\wb"
print get_matching_words(my_expression)

print'3'
my_expression = r"b\w+b"
print get_matching_words(my_expression)

print '4'
my_expression = r"b\w*b"
print get_matching_words(my_expression)

print '5'
my_expression = r"b\w?b"
print get_matching_words(my_expression)

print'6'
my_expression = r"^\w*a\w*e\w*i\w*o\w*u\w*$"
print get_matching_words(my_expression)

print '7'
my_expression = r"[aieou]{2}$"
print get_matching_words(my_expression)

print'8'
my_expression = r"^[regular expression]+$"
print get_matching_words(my_expression)

print '9'
my_expression = r"^[^regex]+$"
print get_matching_words(my_expression)

print '10'
my_expression = r"(.)\1\w*(.)\1"
print get_matching_words(my_expression)
