#!/usr/bin/env ruby
# a Ruby script that accepts one argument and pass it
# exactly matching a string that starts with h ends with n and can have any single character in between

puts ARGV[0].scan(/\bh.?n$/).join
