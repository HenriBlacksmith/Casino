'''
    Roulette.py
    @author: HenriBlacksmith
    @license: GNU GPL
'''
# --imports
import matplotlib.pyplot as plt
import numpy as np
import csv # For use of CSV (Comma Separated Values) files
import re # For RegExp
from numpy.random import randint

# --class
class Roulette(object):
    def __init__(self, k):
        '''
            Builder
        '''
        # --constants
        self.RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.COLORS = ['g','r','k','r','k','r','k','r','k','r','k','k','r','k','r','k','r','k','r','r','k','r','k','r','k','r','k','r','k','k','r','k','r','k','r','k','r']
        self.NUMBERS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        self.ORDERED_NUMBERS = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,17,28,12,35,3,26]
        self.ORDERED_COLORS = ['g', 'r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k','r','k']
        
        self.nb_tirages = k
        self.tirages = self.__generer_tirages(self.nb_tirages)
        
        line = k*['        ']
        self.results = np.array([line,line,line,line])
        
        self.__pair_impair()
        self.__couleur()
        self.__passe_manque()
        self.__colonne()
        self.stats = {}
        self.__compute_stats()
    
    # --getters
    def get_results(self):
        return self.results
    
    def get_RED(self):
        return self.RED
    # --private methods
    def __text_to_stat(self, l):
        d = {}
        for i in xrange(len(l)):
            if not l[i] in d.keys():
                d[l[i]] = 1
            else :
                d[l[i]] += 1
        return d
    
    def __to_stat(self, l, l_keys):
        d = {}
        for k in l_keys:
            d[k]=0
        for i in xrange(len(l)):
            if not l[i] in l_keys:
                print 'Error', l[i], 'is not in the pre-defined keys'
            else :
                d[l[i]] += 1
        return d
    
    def __lnum_to_lstr(self, l):
        for i,x in enumerate(l):
            l[i] = str(x)
        return l
    
    def __generer_tirages(self, i):
        return randint(0,37,i)
    
    def __compute_stats(self):
        self.stats['Parite'] = self.__to_stat(self.results[0,:], ['Pair', 'Impair', 'Zero'])
        self.stats['Couleur'] = self.__to_stat(self.results[1,:], ['Rouge', 'Noir', 'Zero'])
        self.stats['PM'] = self.__to_stat(self.results[2,:], ['Passe', 'Manque', 'Zero'])
        self.stats['Colonne'] = self.__to_stat(self.results[3,:], ['Premiere', 'Milieu', 'Derniere', 'Zero'])
    
    def __pair_impair(self):
        for i in xrange(len(self.tirages)):
            if self.tirages[i]%2 == 0 and self.tirages[i] != 0 :
                self.results[0,i] = 'Pair'
            elif self.tirages[i] == 0 :
                self.results[0,i] = 'Zero'
            else :
                self.results[0,i] = 'Impair'

    def __couleur(self):
        for i in xrange(len(self.tirages)):
            if self.tirages[i] in self.get_RED() :
                self.results[1,i] = 'Rouge'
            elif self.tirages[i] == 0 :
                self.results[1,i] = 'Zero'
            else :
                self.results[1,i] = 'Noir'

    def __passe_manque(self):
        for i in xrange(len(self.tirages)):
            if self.tirages[i]<19 and self.tirages[i]>0:
                self.results[2,i] = 'Passe'
            elif self.tirages[i] == 0 :
                self.results[2,i] = 'Zero'
            else :
                self.results[2,i] = 'Manque'
    
    def __colonne(self):
        for i in xrange(len(self.tirages)):
            if self.tirages[i]%3 == 1 and self.tirages[i] != 0:
                self.results[3,i] = 'Premiere'
            elif self.tirages[i] == 0 :
                self.results[3,i] = 'Zero'
            elif self.tirages[i]%3 == 2 :
                self.results[3,i] = 'Milieu'
            else :
                self.results[3,i] = 'Derniere'
    
    def __display_roulette(self, sizes, labels):
        roulette_ordered_sizes = []
        new_labels = np.zeros(37)
        new_sizes = np.zeros(37)
        j=0
        for i,x in enumerate(self.ORDERED_NUMBERS):
            new_labels[i] = self.ORDERED_NUMBERS[i]
            if x in labels :
                new_sizes[i] = sizes[j]
                j=+1
            else :
                new_sizes[i]=0 
        for i in xrange(len(self.ORDERED_NUMBERS)):
                roulette_ordered_sizes.append(new_sizes[i])
        return roulette_ordered_sizes

    # --public methods
    def plot_stats(self, filename):
        plt.rcParams.update({'font.size': 4})
        plt.figure('Statistics')
        plt.subplot(241)
        barlist = plt.bar(range(len(self.stats['Parite'])), self.stats['Parite'].values(), align='center')
        barlist[2].set_color('g')
        plt.xticks(range(len(self.stats['Parite'])), self.stats['Parite'].keys())
        plt.subplot(242)
        barlist = plt.bar(range(len(self.stats['Couleur'])), self.stats['Couleur'].values(), align='center')
        barlist[0].set_color('g')
        barlist[1].set_color('k')
        barlist[2].set_color('r')
        plt.xticks(range(len(self.stats['Couleur'])), self.stats['Couleur'].keys())
        plt.subplot(245)
        barlist = plt.bar(range(len(self.stats['PM'])), self.stats['PM'].values(), align='center')
        barlist[1].set_color('g')
        plt.xticks(range(len(self.stats['PM'])), self.stats['PM'].keys())
        plt.subplot(246)
        barlist = plt.bar(range(len(self.stats['Colonne'])), self.stats['Colonne'].values(), align='center')
        barlist[2].set_color('g')
        plt.xticks(range(len(self.stats['Colonne'])), self.stats['Colonne'].keys()) 
        plt.subplot(122)
        # Plots the roulette as a pie chart
        old_labels = self.__text_to_stat(self.__lnum_to_lstr(self.tirages)).keys()
        old_sizes = self.__text_to_stat(self.tirages).values()
        sizes = self.__display_roulette(old_sizes, old_labels)
        colors = self.ORDERED_COLORS
        plt.pie(sizes, labels=self.ORDERED_NUMBERS, shadow=True, colors=colors)  
        plt.savefig(filename + '.png', format='png', dpi=300)  
    
    def save_to_file(self, filename, format='csv'):
        '''
            Sauvegarde les tirages dans un fichier au format texte ou CSV
            @param filename: nom du fichier sans extension
            @param format: format de fichier choisi (defaut: CSV)
        '''
        if format == 'text':
            f = open(filename+'.dat', 'w')
            f.write('Numero\tCouleur\tParite\tColonne\tPasse-Manque\n')
            for i in xrange(self.nb_tirages):
                    f.write(str(self.tirages[i])+'\t'+self.results[0,i]+'\t'+self.results[1,i]+'\t'+self.results[2,i]+'\t'+self.results[3,i]+'\n')
            f.close()
        else:
            with open(filename+'.csv', 'w') as csvfile:
                fieldnames = ['Numero', 'Couleur', 'Parite', 'Colonne', 'Passe-Manque']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in xrange(self.nb_tirages):
                    writer.writerow({'Numero': str(self.tirages[i]), 'Couleur': self.results[0,i], 'Parite': self.results[1,i], 'Passe-Manque': self.results[2,i], 'Colonne': self.results[3,i]})
    
    def load_from_file(self, path_to_file):
        '''
            Charge des tirages depuis un fichier texte ou CSV. 
            Les numeros seuls sont charges et les resultats sont recalcules.
            @param path_to_file : chemin vers le fichier a charger
        '''
        # Clearing attributes
        self.tirages = []
        # Regular expressions to test file extensions
        test = re.search('.*.dat$|.*.txt$', path_to_file)
        test2 = re.search('.*.csv$', path_to_file)
        if test.group(0) == path_to_file:
            # In case of a .txt or .dat file
            f = open(path_to_file, 'r')
            for k,line in enumerate(f):
                if k != 0:
                    values = line.split('\t')
                    self.tirages.append(int(values[0]))
            self.nb_tirages = k-1
            self.__pair_impair()
            self.__couleur()
            self.__passe_manque()
            self.__colonne()
        elif test2.group(0) == path_to_file:
            pass
        else:
            print 'Extension de fichier invalide'