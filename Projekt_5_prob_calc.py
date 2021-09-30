import random


class Hat:

    def __init__(self, **kwargs):
        self.balls = dict()
        for key, value in kwargs.items():
            self.balls[key] = value
        self.ball_list = list()
        self.contents = list()
        for key, value in self.balls.items():
            self.ball_count = value * (key,)
            self.ball_list.append(self.ball_count)
        for x in self.ball_list:
            for y in x:
                self.contents.append(y)

    def draw(self, draw_number):
        self.draw_number = draw_number
        self.drawn_balls = list()
        count = len(self.contents)
        if count < draw_number:
            self.drawn_balls.extend(self.contents)
            self.contents.clear()
            for x in self.ball_list:
                for y in x:
                    self.contents.append(y)
                    continue
        else:
            for i in range(self.draw_number):
                self.ball = random.randint(0, len(self.contents)-1)
                self.drawn_balls.append(self.contents[self.ball])
                del self.contents[self.ball]
                count -= 1
                if count < draw_number:
                    self.contents.clear()
                    for x in self.ball_list:
                        for y in x:
                            self.contents.append(y)
                            count = len(self.contents)
                            continue
        print(self.drawn_balls)  # print drawn balls per session
        return self.drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_matching_balls = 0
    balls_drawn = dict()
    count = num_experiments
    while count > 0:
        Hat.draw(hat, num_balls_drawn)
        for x in hat.drawn_balls:
            if x in balls_drawn.keys():
                balls_drawn[x] += 1
            else:
                balls_drawn[x] = 1
        if check_balls(expected_balls, balls_drawn) is None:
            count_matching_balls += 1

        balls_drawn.clear()
        count -= 1
    if count_matching_balls == 0:
        percentage = 0
    else:
        percentage = count_matching_balls/num_experiments
    print(percentage)  # print percentage of picked balls to be drawn
    return percentage


def check_balls(a, b):
    results = list()
    final_result = list()
    for x in a.keys():
        if x in b.keys():
            match = a[x] - b[x]
            if match > 0:
                results.append("False")
            else:
                results.append("True")
        else:
            return False
    for x in results:
        if x == "False":
            final_result.append("False")
    for x in final_result:
        if x == "False":
            return False


hat = Hat(yellow=5, red=8, green=5, blue=9)
probability = experiment(hat=hat, expected_balls={"yellow": 4, "blue": 2}, num_balls_drawn=13,
                         num_experiments=100)
