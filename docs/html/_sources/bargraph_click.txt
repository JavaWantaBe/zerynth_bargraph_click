.. module:: bargraph

*********
Bargraph Click
*********

This module contains the :class:`Bargraph` is a 10 segment shift register 
that can vary led intensity with PWM.
.. class:: Bargraph
    
    Creates an intance of a new Bargraph.
    
    :param drvname: SPI Bus used `( SPI0, SPI1 )`
    :param cs: Chip select used for latching
    :param rst: Reset pin used to reset display
    :param pwm: PWM Pin for display intensity
    
    :Example:

.. code-block:: python

    bargraph = bargraph_click.Bargraph( SPI0, D22, D21, D6.PWM )
    bargraph.set_number( 5 )
    bargraph.set_inensity( 95 )

    
.. method:: set_number( number )

        Writes number from 0 to 10 on display.

        
.. method:: set_inensity( percent) 

        Set the intensity of the led display from 0 to 100 percent. 
        
