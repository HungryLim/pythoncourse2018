## Fill in the following methods for the class 'Clock'

class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        if self.minutes < 10:
            return "%d:0%d" % (self.hour, self.minutes)
        else:
            return "%d:%d" % (self.hour, self.minutes)


    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        self.minutes += minutes
        if self.minutes >=60:
            self.hour += self.minutes/60
            if self.hour > 24:
                self.hour = self.hour%24
                self.minutes = self.minutes%60
            else:
               self.hour =  self.hour
        else:
            self.minutes = self.minutes

    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
            if minutes >= 60:
                h= minutes/60
                m= minutes%60
                self.hour -= h
                self.minutes -= m
                if abs(self.hour) > 24:
                    self.hour = self.hour%24
            elif (self.minutes < minutes) and (minutes < 60):
                 self.hour = self.hour-1
                    if self.hour<0:
                        12-abs(self.hour)
                 self.minutes = self.minutes+60
                 self.minutes-= minutes
            else:
                self.hour = self.hour
                self.minutes -= minutes


    ## Are two times equal?
    def __eq__(self, other):
        if (self.hour == other.hour) and (self.minutes == other.minutes):
            return "Yes, they are equal."

    ## Are two times not equal?
    def __ne__(self, other):
        if self.hour and self.minutes != other:
            return "No, they are not eqaul."

clock1=Clock(1,30)
clock2=Clock(12,5)

print clock1
print clock2
clock1-60
print clock1

print clock1

clock2==clock1
