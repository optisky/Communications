def dbpsk (datain):
    
    print('input:    ', str(datain))
    d0 = 0
    res = 50
    A = 0.3 # Amplitude
    ini_phase = 0
    t = np.linspace(0, 2*np.pi, res)
    out = A*np.cos(t+ini_phase)
    plt.plot(t, out, color='blue')
    plt.vlines(t[-1], -1, 1, linestyle='dashdot')
    print('output: ', d0, end=', ')
    for din in datain:
        d0 = (d0+din)%2
        print(d0, end=', ')
        t += 2*np.pi
        if din:
            out = -out
        plt.plot(t, out, color='blue')
        plt.vlines(t[-1], -1, 1, linestyle='dashdot')
    plt.xlim(0, (len(datain)+1)*2*np.pi)
    plt.ylim(-(A+0.1), A+0.1)
    plt.title('DPSK Modulation')
    plt.xlabel('time [s]')
    
import numpy as np
import matplotlib.pyplot as plt
data = [1,1,0,0,1,1]
dpsk(data)
plt.show()
