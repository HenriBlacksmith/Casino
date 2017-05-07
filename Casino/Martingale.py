'''
    Martingales.py
    @author: HenriBlacksmith
    @license: GNU GPL
'''
# --imports
from Roulette import Roulette
import matplotlib.pyplot as plt
# --class
class Martingale(object):
    def __init__(self, k, banque_initiale = 1):
        '''
            Builder
        '''
        self.nb_tirages = k
        self.tirage = Roulette(self.nb_tirages)
        self.banque_initiale = banque_initiale
        self.banque_vec = []
        self.gains_vec = []
        self.gagnant_vec = []
    # --getters
    def get_tirage(self):
        return self.tirage
    
    # --public methods
    def martingale_simple(self, mise_initiale):
        cl = self.tirage.get_results()[1,:]
        mise = []
        banque = self.banque_initiale
        self.banque_vec.append(self.banque_initiale)
        enchere_courante = 1
        mise.append(mise_initiale)
        for k in xrange(len(cl)):
            if mise[k] == cl[k]:
                gain = enchere_courante*2
                enchere_courante = 1
                self.gagnant_vec.append('Oui')
                if mise[k]=='Rouge':
                    mise.append('Noir')
                else :
                    mise.append('Rouge')
            else :
                gain = -enchere_courante
                enchere_courante = enchere_courante*2
                self.gagnant_vec.append('Non')
                mise.append(mise[k])
            self.gains_vec.append(gain)
            banque += gain
            if banque<0 :
                print 'Perdu'
                return None
            self.banque_vec.append(banque)
            
    def display_results(self, filename):
        plt.figure('mart_res')
        plt.plot(self.banque_vec)
        plt.ylabel('Banque')
        plt.xlabel('#tirage')
        plt.savefig(filename+'.png',format='png',dpi=300)
        print 'Maximum value of the bank = ',max(self.banque_vec),'units'