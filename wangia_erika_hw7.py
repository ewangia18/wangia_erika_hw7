import numpy as np

import matplotlib.pyplot as plt
import numpy as np

X, Y = np.loadtxt('sed.txt', delimiter=',', unpack=True)

integ = np.trapz(np.where(X>10))
print(integ)

plt.plot(X,Y)
plt.title('Spectral Energy Distribution Graph')
plt.xlabel('Microns')
plt.ylabel('Specific Luminosity')
plt.savefig('wangia_erika_hw7.png')
plt.show()
