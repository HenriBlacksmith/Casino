# --imports
import matplotlib.pyplot as plt
# --class imports
from roulette import Roulette
# --run

r = Roulette(10000)
r.plot_stats()
plt.figure('Banque')
plt.plot(r.martingale_simple('Noir', 10))
plt.show()