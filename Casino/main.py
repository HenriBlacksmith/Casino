# --imports
import matplotlib.pyplot as plt
# --class imports
from Roulette import Roulette
# --run

r = Roulette(100)
r.plot_stats()
r.save_to_file('Test_1', format = 'csv')
#plt.figure('Banque')
#plt.plot(r.martingale_simple('Noir', 10))
#plt.show()