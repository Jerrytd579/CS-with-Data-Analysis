import matplotlib.pyplot as plt, csv
from pylab import plot

first_line = True
with open('C:/Users/jerry/Desktop/crypto/bitcoin.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    bitcoin_dates = []
    bitcoin_close = []

    for row in readCSV:

        if first_line == True:
            first_line = False
            continue


        date = row[0]
        close = row[4]
        bitcoin_close.append(float(close))

with open('C:/Users/jerry/Desktop/crypto/bitcoin-cash.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    bitcoincash_dates = []
    bitcoincash_close = []

    for row in readCSV:

        if first_line == True:
            first_line = False
            continue

        date = row[0]
        close = row[4]
        bitcoincash_close.append(float(close))

with open('C:/Users/jerry/Desktop/crypto/ethereum.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ethereum_dates = []
    ethereum_close = []

    for row in readCSV:

        if first_line == True:
            first_line = False
            continue
        date = row[0]
        close = row[4]
        ethereum_close.append(float(close))

with open('C:/Users/jerry/Desktop/crypto/ardor.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ardor_dates = []
    ardor_close = []

    for row in readCSV:

        if first_line == True:
            first_line = False
            continue

        date = row[0]
        close = row[4]
        ardor_close.append(float(close))

with open('C:/Users/jerry/Desktop/crypto/ark.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ark_dates = []
    ark_close = []

    for row in readCSV:

        if first_line == True:
            first_line = False
            continue

        date = row[0]
        close = row[4]
        ark_close.append(float(close))

ardor_x_values = range(len(ardor_close))
ethereum_x_values = range(len(ethereum_close))
bitcoincash_x_values = range(len(bitcoincash_close))
bitcoin_x_values = range(len(bitcoin_close))
ark_x_values = range(len(ark_close))

plt.subplots_adjust(hspace=0.4)

plt.subplot(211)
plot(bitcoin_x_values, bitcoin_close, bitcoincash_x_values, bitcoincash_close, ethereum_x_values, ethereum_close,
     ardor_x_values, ardor_close, ark_x_values, ark_close)
plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000])
plt.legend(["Bitcoin Price", "Bitcoin-Cash Price", "Ethereum Price", "Ardor Price", "Ark Price"], fontsize=20)
plt.title('Crpyto-Currency Age vs Price', fontsize=40)
plt.xlabel('Lifespan (in Days)', fontsize=30)
plt.ylabel('Prices (USD)', fontsize=30)
plt.grid(True)

plt.subplot(212)
plot(ardor_x_values, ardor_close, ark_x_values, ark_close)
#plt.yticks([0, 0.3, 0.6, 0.9])
plt.legend(["Ardor Price", "Ark Price"], fontsize=20)
plt.title('Crpyto-Currencies Under $5', fontsize=40)
plt.xlabel('Lifespan (in Days)', fontsize=30)
plt.ylabel('Prices (USD', fontsize=30)
plt.grid(True)

plt.show()
