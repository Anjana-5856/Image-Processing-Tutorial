import matplotlib.pyplot as plt
import numpy as np
import cmath

# Generate a model signal
t0 = 1250.0
dt = 0.152
freq = (1./dt)/128

t = np.linspace( t0, t0+1024*dt, 1024, endpoint=False )
signal = np.sin( t*(2*np.pi)*freq )

## Fourier transform of real valued signal
signalFFT = np.fft.rfft(signal)

## Get Power Spectral Density
signalPSD = np.abs(signalFFT) ** 2
signalPSD /= len(signalFFT)**2

## Get Phase
signalPhase = np.angle(signalFFT)

## Phase Shift the signal +90 degrees
newSignalFFT = signalFFT * cmath.rect( 1., np.pi/2 )

## Reverse Fourier transform
newSignal = np.fft.irfft(newSignalFFT)

## Uncomment this line to restore the original baseline
# newSignal += signalFFT[0].real/len(signal)


# And now, the graphics -------------------

## Get frequencies corresponding to signal 
fftFreq = np.fft.rfftfreq(len(signal), dt)

plt.figure( figsize=(10, 4) )

ax1 = plt.subplot( 1, 2, 1 )
ax1.plot( t, signal, label='signal')
ax1.plot( t, newSignal, label='new signal')
ax1.set_ylabel( 'Signal' )
ax1.set_xlabel( 'time' )
ax1.legend()

ax2 = plt.subplot( 1, 2, 2 )
ax2.plot( fftFreq, signalPSD )
ax2.set_ylabel( 'Power' )
ax2.set_xlabel( 'frequency' )

ax2b = ax2.twinx()
ax2b.plot( fftFreq, signalPhase, alpha=0.25, color='r' )
ax2b.set_ylabel( 'Phase', color='r' )


plt.tight_layout()

plt.show()
