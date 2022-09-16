import matplotlib.pyplot as plt

x=["2022-09-16T02:58:26Z","2022-09-16T03:58:26Z","2022-09-16T4:58:26Z","2022-09-16T05:58:26Z","2022-09-16T06:58:26Z"]
y=[28,28,28,29,31]
plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel('Humidity')
plt.title("Humidity Level Over Time")
plt.show()
