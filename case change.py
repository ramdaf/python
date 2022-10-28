# Find the weight of each strings in the input sentence according to the following condition.
#     a - z = 1 - 26
#     A - Z = 27 - 52
# Sort the strings according to its weight in the descending order and change the case of each character in the string as per the input strings.
# Note:#     String will have only alphabets, no special characters.
#     Length of each string in the sentence will be same.
#     Each string will be seperated with single white space.
# 1.Input  = aBC DeF
# Output = dEF AbC
# Explanation - Second string "DeF" has more weight than the string "aBC".
# so sorted string is "DeF aBC".
# Now change the case according to the input string,
#     Def -> dEF (casing order of first input string "aBC" is lower, upper, upper)
#     aBC -> AbC (casing order of second input string "DeF" is upper, lower, upper)