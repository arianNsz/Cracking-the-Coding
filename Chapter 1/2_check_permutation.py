def check_permutation(s1, s2):
  s1 = sorted(s1)
  s2 = sorted(s2)
  return s1 == s2



# for better performance we can use hashtables, iterating through the strings
# and counting the numbere of repeatations for each char and finally comparing
# the two hashtables
