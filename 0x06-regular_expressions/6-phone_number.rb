#!/usr/bin/env ruby
# a Ruby script that accepts one argument and pass it

puts ARGV[0].scan(/^\d{10,10}$/).join
