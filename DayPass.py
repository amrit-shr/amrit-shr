
#nothing just first program 
class after_clg:
    def __init__(self, prv_in_day, tom_day):
        self.prv_in_day=prv_in_day
        self.tom_day=tom_day
    def task(self):
        print(f"1st {self.prv_in_day} & 2nd {self.tom_day}")

def ev_task():
    doBoy=after_clg("Today's", "Tomorrow's")
    doBoy.task()

ev_task()
