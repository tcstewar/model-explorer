model-explorer
==============

Model Explorer

This toolkit should let you explore models by running them, varying parameters,
and graphing the results.

Installation
-------------

Use the standard Python easy_install approach::

    python setup.py develop
    
By specifying 'develop', it installs things so that when you do a git pull to
update to the latest version, python will automatically use that latest version.

Instructions
-------------

Build your model as a python script.  There are some examples in the
examples directory.

Specify your parameters at the top of the file like this (it can be after
comments, but should be before any other code)::
      
     alpha = 1
     beta = 'hello'
     gamma = -0.34
     
Indicate data to be save by creating a log object::

    import modex
    log = modex.log()
    ...
    log.zeta = 0.3
    log.kappa = sum(data)/len(data)
    
You can even do::

    log.whatever.something.otherstuff.value = 8
    
If you want to give values over time, this works::

    dt = 0.01
    for i in range(100):
        log.time = i*dt    
        log.mu = sin(i*dt)
        
By default, data will be printed to the screen.  You can adjust this with
parameters on the log object::

    log = modex.log(screen=True, data=False, html=False)        
        
If you set data to True, it will be saved to a data file.  If you set html
to be True, you get a nice html file showing the values changing over time.
(Note: the html output is meant for situations where there are discrete
changes in log values over time)

Running parameter sweeps
-------------------------

To do a parameter sweep, make a new file with this as the contents::

    import modex
    modex.run('mymodel', 10, alpha=[1,2,3], beta='world', gamma=[0.1, 0.2])

This will run the model in mymodel.py 10 times for each parameter setting.
The parameters provided in [square brackets] are treated as different
options, so in the above case there are 3 values for alpha and 2 values for
gamma, so 6 different parameter settings.

Viewing data
-------------

To see the results, there is an html interface::

    python modex/view.py

This does require matplotlib to be installed.    
        
    