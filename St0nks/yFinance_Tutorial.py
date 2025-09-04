import yfinance
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    snp_ticker = "VOO"
    snp = yfinance.Ticker(snp_ticker)
    
    # Fetch historical data for the last year
    data = snp.history(period="1y")
    plt.scatter(np.linspace(0, len(data), len(data)), data['Open'])
    plt.show()


if __name__ == "__main__":

    main()