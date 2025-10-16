import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
result = df.loc[df.sum(axis=1)>100]
print(result)