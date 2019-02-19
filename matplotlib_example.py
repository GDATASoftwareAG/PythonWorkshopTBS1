import matplotlib.pyplot as pyplot
import numpy


def main():
    # We need some data for plotting.
    # This will create a range of date points from 0 to 2 in 0.01 increments
    # We will use this as the Y axis of our graph
    voltage = numpy.arange(0.0, 2.0, 0.01)

    # Now we need the X axis of our graph, which will be a sinus graph of the voltage per millisecond
    time = 1 + numpy.sin(2 * numpy.pi * voltage)

    # Now we need two sub-plots, one is the figure itself and one is a tuple with the X and Y axis
    fig, ax = pyplot.subplots()
    ax.plot(voltage, time)

    # We can also set some vanity
    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='Basic implementation of PyPlot with two axis')
    ax.grid()

    pyplot.show()


if __name__ == "__main__":
    main()
