import nseScrapy
symbolCode = input("enter the symbol code: ")
# symbolCode = 'infy'
nseScrapy.getData(symbolCode)



def print_hi(name):
    print(f' {name} MainFunc')

if __name__ == '__main__':
    print_hi('using')
