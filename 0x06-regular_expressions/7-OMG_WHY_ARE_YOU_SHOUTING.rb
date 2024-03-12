#!/usr/bin/env ruby
#Regexp that only matches capital letters
input=ARGV[0]
puts input.scan(/[A-Z]*/).join
