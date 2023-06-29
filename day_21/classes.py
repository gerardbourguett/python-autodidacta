# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.  # noqa: E501

class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def estad_datos(self):
        for datos in self.datos:
            print(datos)


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]  # noqa: E501

my_estadistica = Estadistica(ages)

my_estadistica.estad_datos()



