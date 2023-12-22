from test_A import run
import numpy as np
from tqdm import tqdm


scores = []
for i in tqdm(range(50)):
    score = run(i)
    scores.append(score)
print('score', format(np.sum(scores), ','))