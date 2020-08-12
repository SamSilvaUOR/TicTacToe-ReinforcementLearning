import sys
import TicTacToe
import matplotlib.pyplot as plt


####################################################################


def train(cold=True, name='data.csv', n=10000):
    """Train the computer and store memory into training data file. If cold,
    computer starts with no prior training data. If warm, computer starts
    with whatever memory is in training data"""
    
    ttt = TicTacToe.TicTacToe()
    
    if cold:
        
        print('Stochastic\n')
        wins1 = ttt.CvC(iterations=int(0.2*n), rand=True)
        print('Learning\n')
        wins2 = ttt.CvC(iterations=int(0.8*n), rand=False)
        ttt.comp.store_dta(name)
        
        wins = wins1.append(wins2, ignore_index=True)
        x = wins.groupby(wins.index//100).sum()
        plt.plot(x['win'])
        plt.show()
    
    else:
        
        print('Loading...')
        ttt.comp.load_dta(name)
        
        wins = ttt.CvC(iterations=n, rand=False)
        ttt.comp.store_dta(name)
        
        x = wins.groupby(wins.index//100).sum()
        plt.plot(x['win'][:-1])
        plt.show()


####################################################################

    
def play(name=None):
    """Play against the computer. For random, don't pass a training data file
    name. For learned, pass the training data file name"""
    
    ttt = TicTacToe.TicTacToe()
    
    try:
        print('Loading...')
        ttt.comp.load_dta(name)
    except Exception as e:
        print(e)
    
    ttt.PvC(rand=False)
    
    if name != None:
        ttt.comp.store_dta(name)
    
    
####################################################################
    

def test(name='data.csv', n=10000):
    """Examin performace of computer without adjusting training data"""
    
    ttt = TicTacToe.TicTacToe()
    
    print('Loading...')
    ttt.comp.load_dta(name)
    wins = ttt.CvC(iterations=n, rand=False)
    
    x = wins.groupby(wins.index//100).sum()
    plt.plot(x['win'][:-1])
    plt.show()
    
    
####################################################################
    
    
if __name__ == '__main__':
    
    # play()
    
    train(cold=True, name='data.csv', n=1_000_000)
    play(name='data.csv')
    
    # train(cold=False, name='data.csv', n=100_000)
    # test(name='data.csv', n=100_000)