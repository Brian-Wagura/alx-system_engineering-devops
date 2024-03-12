#!/usr/bin/env ruby
#script to output sender, receiver and flags

x = ARGV[0]
puts x.scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
