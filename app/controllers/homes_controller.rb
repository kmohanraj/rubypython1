class HomesController < ApplicationController
  require "rubypython"

  def index
  	puts "I am in"
    RubyPython.start
    sys = RubyPython.import("sys")
    sys.path.append('.')
    puts sys
    my = RubyPython.import("find_face")
    #here pass params
    temp = my.find("/home/iteron/Pictures/sridivya.jpg").rubify
	RubyPython.stop
	puts temp
  end
end
