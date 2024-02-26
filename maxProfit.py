import statistics
import matplotlib.pyplot as plt

class Solution(object):
    def maxProfit(self, l):
        stock = str(input('What is the name of your stock?'))
        #If you want to add your own values uncomment
        '''
        l = []
        x = int(input('What is your first price of the stock?\n'))
        l.append(x)
        while True:
            try:
                x = int(int(input('add next days price (-1 to stop)\n')))
                if x == -1:
                    break
                elif x < 0:
                    print('Your value seems to be negative! try again.')
                else:
                    l.append(x)
            except:
                print("Looks like you didnt input a number, please try again.")
        '''
        if len(l) < 1:
            return "Please provide 2 or more prices"
        #calculate variance and standard deviation for samples not population
        
        print(f'Max profit in this time range: {self.profit_calculation(l)}\nRiskiness of stock in this time range: {self.risk_calculation(l)}')
        self.plot(stock, l)
            
        return None
    def plot(self, stock, l):
        plt.plot(l)
        plt.xlabel('Month')
        plt.ylabel('Stock Price')
        plt.title(f'{stock} Prices Over Time')
        plt.show()
        plt.xticks(rotation = 30)


    def profit_calculation(self, l):
        profit = 0
        smallest = l[0]
        for price in l:
            if price < smallest:
                smallest = price
            else:
                profit += max(0, price - smallest)
                smallest = price
        return profit
    def risk_calculation(self, l):
        mean = sum(l)/len(l)
        variance = []
        for v in l:
            diff = v - mean
            variance.append(diff**2)
        standard_deviation = (sum(variance)/(len(l)-1))**0.5
        standard_deviation_percent = (standard_deviation/mean)*100
        if standard_deviation_percent > 30:
            risk_of_stock = 'Risky'
        elif standard_deviation_percent > 15:
            risk_of_stock = 'Moderate'
        else:
            risk_of_stock = 'Safe'
        print(f'standard deviation: {standard_deviation}\n')
        print(f'standard deviation percent:  {standard_deviation_percent}\n')
        return risk_of_stock

instance = Solution()   
apple_pastyear_monthly = [149, 158, 165, 174, 187, 192, 177, 175, 173, 191, 194, 194, 182]
l = apple_pastyear_monthly
#calculate max profit and standard deviation percentage
instance.maxProfit(l)

