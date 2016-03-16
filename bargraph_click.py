################################################################################
# Click_Bargraph
#
# Created: 2016-03-14 20:27:46.627545
#
################################################################################

"""
.. module:: bargraph

*********
Bargraph Click
*********

This module contains the :class:`Bargraph` is a 10 segment shift register 
that can vary led intensity with PWM.

"""

import spi
import pwm
import streams


class Bargraph:
    """
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

    """
    spi_port = 0
    # initialize object
    def __init__(self, drvname, cs, rst, pwm):
        #Global variables for class needed
        self.spi_port = spi.Spi( cs, drvname )
        self.rst = rst
        self.pwm = pwm

        try:
            self.spi_port.start()
        except Exception as e:
            print(e)

        #Set modes of included pins
        pinMode(self.rst, OUTPUT)

        #Reset system to default values
        self._reset()
        self.set_number( 0 )
        self.set_intensity( 50.0 )

    #Latch the shift registers
    def _latch( self ):
        self.spi_port.select()
        sleep(3, MILLIS)
        self.spi_port.unselect()

    #Reset the display 
    def _reset( self ):
        digitalWrite(self.rst, LOW)
        sleep(3, MILLIS)
        digitalWrite(self.rst, HIGH)

    def set_number( self, number ):
        """
.. method:: set_number( number )

        Writes number from 0 to 10 on display.

        """
        if number > 10:
            return

        temp = 0x0000
        temp = ( 1 << number ) - 1
        value = bytearray(2)
        value[0] = ( temp & 0xff00 ) >> 8
        value[1] = ( temp & 0x00ff )

        self._reset()
        self.spi_port.lock()

        try:
            self.spi_port.write( value )
        except Exception as e:
            print(e)
        finally:
            self.spi_port.unlock()

        self._latch()
    
    def set_intensity( self, percent ):
        """ 
.. method:: set_inensity( percent) 

        Set the intensity of the led display from 0 to 100 percent. 
        """
        new_period = ( percent / 100.0 ) * 10
        try:
            pwm.write( self.pwm, 10, int(new_period) )
        except Exception as e:
            print(e)

