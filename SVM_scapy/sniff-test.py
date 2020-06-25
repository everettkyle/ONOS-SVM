from scapy.all import *
from scapy.utils import *
import matplotlib.pyplot as plt

countudp = 0
counttcp = 0
pkt = sniff(count = 100)

pkt.summary()
for packet in pkt:
	if(packet.haslayer(IP)):
		if(packet.proto == 6):
			counttcp = counttcp + 1
		if(packet.proto == 17):
			countudp = countudp + 1
	else:
		continue

activities = ['UDP', 'TCP']
slices = [countudp, counttcp]
colors = ['lightcoral','lightskyblue']

plt.pie(slices, labels = activities, colors=colors, shadow = True, radius = 1.2, autopct='%1.1f%%')

plt.legend()
plt.show()
