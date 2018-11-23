



class Fred
  def initialize(v)
    @val = v
  end

  # Set it and get it.
  def set(v)
    @val = v
  end

  def get
    return @val
  end
end

a = Fred.new(10)
b = Fred.new(22)

print "A: ", a.get, " ", b.get,"\n";
b.set(34)
print "B: ", a.get, " ", b.get,"\n";

class Fred
  def inc
    @val += 1
  end
end

a.inc
b.inc
print "C: ", a.get, " ", b.get,"\n";

def b.dec
  @val -= 1
end

begin
  b.dec
  a.dec
rescue StandardError => msg
  print "Error: ", msg, "\n"
end

print "D: ", a.get, " ", b.get,"\n";

