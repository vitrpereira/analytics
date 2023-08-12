    
class Metrics:
    def cagr(self, start_value, end_value, period):
        result = f'{round(((end_value/start_value)**(1/period)-1)*100, 2)}%'
        return result
    
    def roi(self, net_gain, cost_of_investment):
        result = f'{((net_gain/cost_of_investment)*100)}%'

metrics = Metrics()

initial = 1
final = 20
period = 1    

cagr = metrics.cagr(initial, final, period)

roi = metrics.roi(100000, 50)

print(f'{cagr}\n{roi}')