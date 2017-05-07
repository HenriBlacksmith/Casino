# --imports
# --class imports
from Martingale import Martingale
# --run

m = Martingale(10)
m.get_tirage().plot_stats('Test_tirage')
m.martingale_simple(1)
m.display_results('Test_martingale')