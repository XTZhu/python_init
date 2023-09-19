balls = ['football', 'basketball', 'baseball', 'baseball', 'big ball', 'cat']

useless_ball_types = ['football', 'basketball']

filtered_balls = []

for ball in balls:
    if ball not in useless_ball_types:
        filtered_balls.append(ball)


out = [ball for ball in balls if ball not in useless_ball_types]

out2 = [ball for ball in range(0, 2)]

out3 = list(filter(lambda ball: ball not in useless_ball_types, balls))

print(out3)