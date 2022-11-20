import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = []

    def __init__(self, **args) :
        self.contents = []
        for k,v in args.items() :
            for i in range(v) :
                self.contents.append(k)

    def draw(self, draw) :
        if draw > len(self.contents) :
            draw = len(self.contents)
        sample = []
        for i in range(draw) :
            rand = random.randint(0, len(self.contents) - 1)
            sample.append(self.contents[rand])
            self.contents.pop(rand)
        return sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
    expected = []
    ocurrances = 0

    for k,v in expected_balls.items() :
        for i in range(v) :
            expected.append(k)

    for i in range(num_experiments) :
        back_up = copy.deepcopy(hat)
        sample = back_up.draw(num_balls_drawn) 
        sample_obj = dict()
        for item in sample :
            sample_obj[item] = sample_obj.get(item, 0) + 1
        ocurred = True
        for k,v in expected_balls.items() :
            try :
                if sample_obj[k] < expected_balls[k] :
                    ocurred = False
            except :
                ocurred = False
        if ocurred :
            ocurrances = ocurrances + 1
    
    probability = ocurrances / num_experiments
    return probability