## Import libraries
import time
from typing import Optional, Callable # use Optional later
import os

## global function
delay: Callable[ [ float ], None ] = time.sleep
sys_call: Callable[ [ str ], int ] = os.system


## flush utilities
def clear_flush(  ) -> None:
    """
    clear_flush
    - clears console( Terminal ) from text
    """
    sys_call( "cls || clear" )


def line_flush( text: str, seconds: float= 1.0 ) -> None:
    """
    line_flush
    - prints text line by line from up to down
    """
    for line in text.splitlines(  ):
        print( line )
        delay( seconds )

def print_flush( text: str, seconds: float= 1.0 ) -> None:
    """
    print_flush
    - prints the text char by char to console( Terminal )
    """
    for char in text:
        print( char, end= "", flush= True )
        delay( seconds )

    print( "\n" )

# maybe not bytes who knows
def music_flush( record: bytes ) -> None:
    # TODO: figure out how to play music in terminal games XD
    """
    music_flush
    - plays sounds
    """
    ...


