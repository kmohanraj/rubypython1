class HomesController < ApplicationController
  require "rubypython"
  def index
#if using rubypython gem 
    RubyPython.start
    sys = RubyPython.import("sys")
    sys.path.append('.')
   my = RubyPython.import("find_face")
   one = "Hello World"
   # sys.stdout.write(json.dumps(my))
   # find_face.to_enum.each do |i|
   # 	p i
   # end
    p ">>>>>>>>>>>>>>>>>>>"
    p my
    p ">>>>>>>>>>>>>>>>>>>"
  	# RubyPython.stop

#if using gem escape these method
 #if using string is default code
  python_cmd = Escape.shell_command(['python', "find_face.py"]).to_s
   # python_cmd = Escape.shell_command(['python', "find_face.py"])
  p ">>>>>>>>>>>>>"
  p python_cmd
  p ">>>>>>>>>>>>>"

   system python_cmd

  p "22222222222222222>>>>>>>>>>>>>"

  end
end
