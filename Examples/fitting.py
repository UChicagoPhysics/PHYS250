# DO NOT CHANGE THIS FILE!
#
# This file contains the functions linear_fit for fitting a straight
# line to data and general_fit for fitting any user-defined funciton
# to data.  To use either of them,  the first line of your program
# should be "from fitting import *".

from __future__ import print_function  # in case Python 2 is used

from math import sqrt
from scipy import odr



def linear_fit(xdata, ydata, sigmay=None, sigmax=None):
    """
    Performs a linear fit to data.

    Parameters
    ----------
    xdata : An array of length N.
    ydata : An array of length N.

    sigmay : None or an array of length N.
    sigmax : None or an array of length N.
        If one is provided, it is the standard deviation of ydata.  Analytical linear regression used.
        If both are provided, they are the standard deviations of ydata and xdata, respectively. ODR is used.

    Returns
    -------
    a, b   : Optimal parameter of linear fit (y = a*x + b)
    sa, sb : Uncertainties of the parameters
    """

    def lin_func(p, x):
        a, b = p
        return a*x + b
    
    dof = len(ydata) - 2

    if sigmax is None:
        if sigmay is None:
            w = ones(len(ydata)) # Each point is equally weighted.
        else:
            w=1.0/(sigmay**2)

        sw = sum(w)
        wx = w*xdata # this product gets used to calculate swxy and swx2
        swx = sum(wx)
        swy = sum(w*ydata)
        swxy = sum(wx*ydata)
        swx2 = sum(wx*xdata)

        a = (sw*swxy - swx*swy)/(sw*swx2 - swx*swx)
        b = (swy*swx2 - swx*swxy)/(sw*swx2 - swx*swx)
        sa = sqrt(sw/(sw*swx2 - swx*swx))
        sb = sqrt(swx2/(sw*swx2 - swx*swx))

        if sigmay is None:
            chi2 = sum(((a*xdata + b)-ydata)**2)
        else:
            chi2 = sum((((a*xdata + b)-ydata)/sigmay)**2)
        rchi2 = chi2/dof

    else:
        # make the initial guess a line passing through first and last points
        a0 = (ydata[-1]-ydata[0])/(xdata[-1]-xdata[0])
        b0 = ydata[0]-xdata[0]*a0
        model = odr.Model(lin_func)
        data = odr.RealData(x=xdata, y=ydata, sx=sigmax, sy=sigmay)
        od = odr.ODR(data, model, [a0,b0])
        out = od.run()
        a,b = out.beta
        sa,sb = out.sd_beta
        rchi2 = out.res_var

#    From: https://www.physics.utoronto.ca/~phy326/python/odr_fit_to_data.py
#    scipy.odr scales the parameter uncertainties by the reduced chi 
#    square (out.res_var).  If the fit is poor, i.e. reduced chisq is 
#    large, the uncertainties are scaled up, which makes sense. If the 
#    fit is "too good", i.e. reduced chisq << 1, it suggests that the 
#    uncertainties may have been overestimated, but it seems risky to 
#    scale down the uncertainties. 
        if rchi2 < 1.0 :
            sa = sa/sqrt(rchi2)
            sb = sb/sqrt(rchi2)

    if sigmay is None:
        print('results of linear_fit: no uncertainties provided, so use with caution')
    else:
        print('results of linear_fit:')

#    print('   chi squared = ', chi2)
    print('   reduced chi squared = ', rchi2)
    print('   degrees of freedom = ', dof)


    return a, b, sa, sb, rchi2, dof


from scipy.optimize import curve_fit
from pylab import *  # for array, zeros, arange


#def general_fit(f, xdata, ydata, p0=None, sigma=None, **kw):
def general_fit(f, xdata, ydata, p0=None, sigmay=None, sigmax=None):

    """
    Pass all arguments to curve_fit, which uses non-linear least squares
    to fit a function, f, to data.  Calculate the uncertaities in the
    fit parameters from the covariance matrix.
    """

    dof = len(ydata) - len(p0)

    if sigmax is None:
        popt, pcov = curve_fit(f, xdata, ydata, p0, sigmay)

        if sigmay is None:
            chi2 = sum(((f(xdata,*popt)-ydata))**2)
        else:
            chi2 = sum(((f(xdata,*popt)-ydata)/sigmay)**2)
#        dof = len(ydata) - len(popt)
        rchi2 = chi2/dof
        # The uncertainties are the square roots of the diagonal elements
        punc = zeros(len(popt))
        for i in arange(0,len(popt)):
            punc[i] = sqrt(pcov[i,i])
    else:
        # ODR expects a funciton with parameters, then x
        def f_fixed(p,x):
            return f(x,*p)
        
        model = odr.Model(f_fixed)
        data = odr.RealData(x=xdata, y=ydata, sx=sigmax, sy=sigmay)
        od = odr.ODR(data, model, p0)
        out = od.run()
        popt = out.beta
        punc = out.sd_beta
        rchi2 = out.res_var

#    From: https://www.physics.utoronto.ca/~phy326/python/odr_fit_to_data.py
#    scipy.odr scales the parameter uncertainties by the reduced chi 
#    square (out.res_var).  If the fit is poor, i.e. reduced chisq is 
#    large, the uncertainties are scaled up, which makes sense. If the 
#    fit is "too good", i.e. reduced chisq << 1, it suggests that the 
#    uncertainties may have been overestimated, but it seems risky to 
#    scale down the uncertainties. 
        if rchi2 < 1.0 :
            sa = sa/sqrt(rchi2)
            sb = sb/sqrt(rchi2)
    if sigmay is None:
        print('results of general_fit: no uncertainties provided, so use with caution')
    else:
        print('results of general_fit:')
#    print('   chi squared = ', chi2)
    print('   degrees of freedom = ', dof)
    print('   reduced chi squared = ', rchi2)

    return popt, punc, rchi2, dof


def fit_errors2d(func, xdata, ydata, xerr, yerr, p0):
    model = odr.Model(func)
    data = odr.RealData(x=xdata, y=ydata, sx=xerr, sy=yerr)
    od = odr.ODR(data, model, p0)
    out = od.run()
    popt = out.beta
    punc = out.sd_beta
    rchi2 = out.res_var
    dof = len(ydata) - len(popt)
    return popt, punc, rchi2, dof