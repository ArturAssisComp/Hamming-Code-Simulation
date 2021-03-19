import sys
sys.path.append(".")
from tools import tools as tl
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

pb = []
p_vector = []
vp = np.logspace(math.log(0.5, 2), math.log(0.001, 2), 30, base=2)
for p in vp:
    print('p = ', p)
    p_vector.append(p)
    number_information_words = int(2*pow(10, 5)/4)
    information_words = tl.generate_words(number_information_words)
    code_words = tl.encoder(information_words)
    received_words = tl.binary_symmetric_channel(code_words, p)
    decoder_words = tl.decoder(received_words)
    pb.append(tl.comparator(information_words, decoder_words))

x = np.linspace(0.5, 0, 100)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(p_vector, pb, label='Hamming')
plt.plot(x, x, label='Sem codificação')
ax.set_xlim(0.5, pow(10, -3))
ax.set_ylim(pow(10, -3), 0.5)
ax.set_yscale('log', base=2)
ax.set_xscale('log', base=2)
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: '{0:.2g}'.format(float(x), ',')))
ax.get_xaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: '{0:.2g}'.format(float(x), ',')))

plt.xlabel('p')
plt.ylabel('Pb')
ax.legend()
plt.savefig('./plots/fig.png')
plt.show()

