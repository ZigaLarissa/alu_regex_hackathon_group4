#!/usr/bin/env ruby
puts ARGV[0].scan(/\w+\s+\w*\s*S\d{2,2}E\d{2,2}:\s(\w+\s+)*/).join