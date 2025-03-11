import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('TkAgg')

myfile= pd.read_csv('data.csv')
year=myfile['year']
sales=myfile['sales']

# plt.plot(year,sales,color='red', marker='o',linestyle="--", linewidth=1)
# plt.xlabel('year')
# plt.ylabel('sales')
# plt.title('Sales vs Year')
# plt.show()

# plt.bar(year,sales, color='red')
# plt.title("Title")
# plt.xlabel("year")
# plt.ylabel("sales")
# plt.show()

x=[1,2,3,4]
y=[1,4,9,16]
plt.subplot(2,2,1) #2x2 grid, first subplot
plt.plot(x,y, color='blue', marker='o')
plt.title('First')
plt.subplot(2,2,2)#2X2 grid, second subplot
plt.plot(x,[2*i for i in y], color='red', marker='o')
plt.title('Second')
plt.suptitle("Common title")
plt.show()
