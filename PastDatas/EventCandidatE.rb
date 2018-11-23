class EventCandidatC < ApplicationRecord
  self.table_name = 'events'
  KIND = %w(opening appointment).freeze

  validates :kind, inclusion: { in: KIND, message: 'is not a valid kind of event' }
  validates :starts_at, presence: true
  validates :ends_at, presence: true
  validate :starts_at_cannot_be_greater_than_ends_at,
           :ends_at_cannot_be_a_different_day_than_starts_at,
           :hours_must_be_a_multiple_of_thirty_minutes,
           :same_kind_of_event_cannot_be_in_a_same_time_slot

  with_options if: :appointment? do |appointment|
    appointment.validates :weekly_recurring, absence: true
    appointment.validate :appointment_cannot_be_outside_of_opening_hours
  end


# Function to evaluate a polynomial at x.  The polynomial is given
# as a list of coefficients, from the greatest to the least.
def polyval(x, coef)
    sum = 0
    coef = coef.clone           # Don't want to destroy the original
    while true
        sum += coef.shift       # Add and remove the next coef
        break if coef.empty?    # If no more, done entirely.
        sum *= x                # This happens the right number of times.
    end
    return sum
end

#
# Function to read a line containing a list of integers and return
# them as an array of integers.  If the string conversion fails, it
# throws TypeError.  If the input line is the word 'quit', then it
# converts it to an end-of-file exception
def readints(prompt)
    # Read a line
    print prompt
    line = readline.chomp
    raise EOFError.new if line == 'quit' # You can also use a real EOF.

    # Go through each item on the line, converting each one and adding it
    # to retval.
    retval = [ ]
    for str in line.split(/\s+/)
# Objects may have methods all to themselves.
        if str =~ /^\-?\d+$/
            retval.push(str.to_i)
        else
            raise TypeError.new
        end
    end

    return retval
end

#
# Take a coeff and an exponent and return the string representation, ignoring
# the sign of the coefficient.
def term_to_str(coef, exp)
    ret = ""

    # Show coeff, unless it's 1 or at the right
    coef = coef.abs
    ret = coef.to_s     unless coef == 1 && exp > 0
    ret += "x" if exp > 0                               # x if exponent not 0
    ret += "^" + exp.to_s if exp > 1                    # ^exponent, if > 1.

    return ret
end



    return result
end

#
# Run until some kind of endfile.
begin
    # Repeat until an exception or quit gets us out.
    while true
        # Read a poly until it works.  An EOF will except out of the
        # program.
        print "\n"
        begin
            poly = readints("Enter a polynomial coefficients: ")
        rescue TypeError
            print "Try again.\n"
            retry
        end
        break if poly.empty?

        # Read and evaluate x values until the user types a blank line.
        # Again, an EOF will except out of the pgm.
        while true
            # Request an integer.
            print "Enter x value or blank line: "
            x = readline.chomp
            break if x == ''
            raise EOFError.new if x == 'quit'

            # If it looks bad, let's try again.
            if x !~ /^\-?\d+$/
                print "That doesn't look like an integer.  Please try again.\n"
                next
            end

            # Convert to an integer and print the result.
            x = x.to_i
            print "p(x) = ", polystr(poly), "\n"
            print "p(", x, ") = ", polyval(x, poly), "\n"
        end
    end
rescue EOFError
    print "\n=== EOF ===\n"
rescue Interrupt, SignalException
    print "\n=== Interrupted ===\n"
else
    print "--- Bye ---\n"
end

  def opening?
    kind.eql? 'opening'
  end

  def appointment?
    kind.eql? 'appointment'
  end



  private

  def starts_at_cannot_be_greater_than_ends_at
    if starts_at.present? and ends_at.present? and starts_at >= ends_at
      errors.add(:starts_at, 'cannot be greater than ends_at')
    end
  end

  def ends_at_cannot_be_a_different_day_than_starts_at
    if starts_at.present? and ends_at.present? and starts_at.to_date != ends_at.to_date
      errors.add(:ends_at, 'cannot be a different day than starts_at')
    end
  end



  def same_kind_of_event_cannot_be_in_a_same_time_slot
    if kind.present? and starts_at.present? and ends_at.present? and
        EventCandidatA.where(kind: kind).overlapping(starts_at, ends_at).any?
      errors.add(:base, 'cannot be in a same time slot than an other')
    end
  end

  def appointment_cannot_be_outside_of_opening_hours
    if starts_at.present? and ends_at.present? and
        EventCandidatA.openings_on(starts_at).cover(starts_at, ends_at).empty?
      errors.add(:base, 'cannot be outside of opening hours')
    end
  end
end
