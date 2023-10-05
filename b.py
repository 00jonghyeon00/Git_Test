import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 데이터 생성
x = np.random.randn(100, 10)

# 데이터 전처리
x_norm = x / np.sqrt(np.sum(x ** 2, axis=1, keepdims=True))

# 주성분 추출
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_norm)

# 데이터 축소
x_red = x_pca[:, :2]

# 데이터 시각화
plt.scatter(x_red[:, 0], x_red[:, 1])
plt.show()


print("hi")
print("bye")
print("Hello")