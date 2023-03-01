#!/usr/bin/env ruby

# {min,max} is a range quantifier used to match b/w the min & max
# occurrence of the precedding character. t{2,5} -> matches 2 - 5 
# occurence of t in the sequence.
 
puts ARG[0].scan(/hbt{2,5}n/).join
