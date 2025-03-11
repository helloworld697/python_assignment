import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

x = [2020, 2021, 2022,2023,2024 ]
y = [10000, 20000, 25000, 30000, 40000]
plt.plot(x, y, color="#672622", marker="o",linestyle=":",linewidth=1)
plt.xlabel('Year')
plt.ylabel('sales')
plt.title('Graph of sales in last five years')
plt.show()



