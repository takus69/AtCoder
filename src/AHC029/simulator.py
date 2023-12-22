from test_A import run
import numpy as np
from tqdm import tqdm


scores = []
for i in tqdm(range(100)):
    score = run(i)
    scores.append(score)
print('average', np.mean(scores))