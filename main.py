# --imports
# --class imports
from Martingale import Martingale
# --run
nb_tirages = 100
mise_initiale = 'Noir'
banque_initiale = 5

m = Martingale(nb_tirages, banque_initiale)
m.get_tirage().plot_stats('Test_tirage')
m.martingale_simple(mise_initiale)
m.display_results('Test_martingale')