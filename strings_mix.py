"""
QUESTION:

Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

"""

#Solution:-

def mix(s1, s2):
    # I wrote a algorithm to count the number of lowercase letters and add it to the dictionary.
    # s1_dict = {}
    # s2_dict = {}
    # for i in s1:
    #     if i.islower():
    #         count = s1.count(i)
    #         if count > 1:
    #             s1_dict[i] = count
    # for i in s2:
    #     if i.islower():
    #         count = s2.count(i)
    #         if count > 1:
    #             s2_dict[i] = count

    #Then I made a comprehension for the algorithm.

    s1_dict = {k:v for (k, v) in zip([i for i in s1 if i.islower() and s1.count(i) > 1], [s1.count(i) for i in s1 if i.islower() and s1.count(i) > 1])}
    s2_dict = {k:v for (k, v) in zip([i for i in s2 if i.islower() and s2.count(i) > 1], [s2.count(i) for i in s2 if i.islower() and s2.count(i) > 1])}
    
    #print(s1_dict, '\n', s2_dict) For checking the algorithm and the comprehension actually works

    #Then I'm gonna check which dictionary has more keys and copy it to 'main_dict' for comparison to make sure none of the keys get omitted
    if len(s1_dict.keys()) >= len(s2_dict.keys()):
        main_dict = s1_dict
    else:
        main_dict = s2_dict

    #Then I'm gonna do the main comparison and append it to a list called 'result_list'    
    result_list = []
    for key in main_dict.keys():
        if key in s1_dict.keys() and key in s2_dict.keys():
            if s1_dict[key] > s2_dict[key]:
                result_list.append(f"1:{key * s1_dict[key]}")
            elif s1_dict[key] < s2_dict[key]:
                result_list.append(f"2:{key * s2_dict[key]}")
            elif s1_dict[key] == s2_dict[key]:
                result_list.append(f"=:{key * s2_dict[key]}")
        else:
            if main_dict == s1_dict:
                result_list.append(f"1:{key * s1_dict[key]}")
            else:
                result_list.append(f"2:{key * s2_dict[key]}")

    #print(result_list)  Again for checking that the algorithm I wrote is working

    #Then I'm gonna join the result_list with '/' as delimiter and return it
    return  ('/').join(result_list)
print(mix("Are they here", "yes, they are here"))



message="""
        _
       | |
     ( | | )
    ^^^^^^^^^^^^^^^^^^^
   /       FUCK        \\
  -----------------------
 / It's giving errors!   \\
{_________________________}
|__________________________|
| +++++  |>)    _          |
|   | O  |>)E  |_ ontd.... |
|__________________________|
It is giving error when i test it... I'll do it tomorrow.
"""
print(message)