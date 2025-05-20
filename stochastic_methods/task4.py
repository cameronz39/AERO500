import random
import matplotlib.pyplot as plt
import numpy as np

unit_price = {
    "yearly": [50, 52, 55, 57, 65],
    "min": 50,
    "max": 70,
    "mode": 55
}

unit_sales = {
    "yearly": [2000, 2200, 2700, 2500, 2800],
    "min": 2000,
    "max": 3000,
    "mode": 2400
}

variable_costs = {
    "yearly": [50000, 55000, 56000, 57000, 58000],
    "min": 50000,
    "max": 65000,
    "mode": 55200
}

fixed_costs = {
    "yearly": [10000, 12000, 15000, 16000, 17000],    
    "min": 10000,
    "max": 20000,
    "mode": 14000
}

def draw_triangle_dis(data): # uniformly samples a grid until the result falls into the triangular PDF
    a = data["min"]
    b = data["max"]
    c = data["mode"]

    while True:
        x = random.uniform(a,b)
        y = random.uniform(0, 2/(b-a))

        if a <= x and x <= c:
            pdf_out = (2*(x-a)) / ((b-a)*(c-a))

        elif c <= x and x <= b:
            pdf_out = (2*(b-x))/((b-a)*(b-c))
        else:
            pdf_out = 0
        
        if y <= pdf_out:
            return x
        
n = 10000
earnings_samples = []
var_cost_samples = []
fixed_cost_samples  = []
sales_samples = []
for i in range(1,n):
    price  = draw_triangle_dis(unit_price)
    sales  = draw_triangle_dis(unit_sales)
    var_c  = draw_triangle_dis(variable_costs)
    fix_c  = draw_triangle_dis(fixed_costs)

    earnings = price * sales - (var_c + fix_c)
    earnings_samples.append(earnings)
    var_cost_samples.append(var_c)
    fixed_cost_samples.append(fix_c)
    sales_samples.append(price * sales)


plt.figure()
plt.hist(earnings_samples, bins=70)   
plt.xlabel("Earnings")
plt.ylabel("Frequency")
plt.title("Next‑Year Earnings Predictions using Monte Carlo Simulation")
plt.grid(True)
plt.show()

theta_hat_n = np.mean(earnings_samples) # samples mean
sigma_hat_n = 0
for sample in earnings_samples:
    sigma_hat_n += (sample - theta_hat_n)**2
sigma_hat_n = np.sqrt((sigma_hat_n)/(n-1))

z = 1.96 # from text, for alpha = 0.05 

L = theta_hat_n - z*(sigma_hat_n/np.sqrt(n))
U = theta_hat_n + z*(sigma_hat_n/np.sqrt(n))

print(f"95% confidence interval for next year's earnings: [{L:.0f}, {U:.0f}]")

slope_sales  = np.polyfit(sales_samples,  earnings_samples, 1)[0]
slope_var    = np.polyfit(var_cost_samples, earnings_samples, 1)[0]
slope_fixed  = np.polyfit(fixed_cost_samples, earnings_samples, 1)[0]

norm_slope_sales = slope_sales * (np.std(sales_samples, ddof=1) / np.std(earnings_samples, ddof=1))
norm_slope_var = slope_var * (np.std(var_cost_samples, ddof=1) / np.std(earnings_samples, ddof=1))
norm_slope_fixed = slope_fixed * (np.std(fixed_cost_samples, ddof=1) / np.std(earnings_samples, ddof=1))

print(f"Sigma-normalized derivative of variable costs: {norm_slope_var}")
print(f"Sigma-normalized derivative of fixed costs: {norm_slope_fixed}")
print(f"Sigma-normalized derivative of unit sales x unit price: {norm_slope_sales}")


plt.figure()
plt.scatter(var_cost_samples,earnings_samples)
plt.grid()
plt.ylim(0, 2e5)
plt.xlabel("Variable Costs")
plt.ylabel("Earnings")

plt.figure()
plt.scatter(fixed_cost_samples,earnings_samples)
plt.grid()
plt.ylim(0, 2e5)
plt.xlabel("Fixed Costs")
plt.ylabel("Earnings")

plt.figure()
plt.scatter(sales_samples,earnings_samples)
plt.grid()
plt.ylim(0, 2e5)
plt.xlabel("Unit Sales x Unit Price")
plt.ylabel("Earnings")
plt.show()

