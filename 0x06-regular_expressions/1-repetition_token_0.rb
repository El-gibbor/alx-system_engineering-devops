#!/usr/bin/env ruby
# used range quantifier -> {min,max)char

puts ARGV[0].scan(/hbt{2,5}n/).join
