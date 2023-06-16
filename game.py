##########################################
### Name: soup game repository         ###
### Version: 0.0.2                     ###
### By: WumboWatcher & SolathPrime     ###
### repo: Solath Prime                 ###
##########################################


## Import librarys
import json
from flushUtils import ( print_flush, clear_flush, line_flush, music_flush, delay )
from arts import logo, main_menu_screen, credits






class GamePlay():
    """
    GamePlay
    - I had to make it this way sorry.
    """
    def __init__( self, settings: dict[ str, dict[ str, int | bool ] ], words: list[ dict[ str, str ] ]  ) -> None:
        """
        initialize
        - fetches settings and other stuff!
        """

        # when a class variable is prefixed with "__" (double underscore)
        # it becomes privet to that class, that includes class methods
        self.__settings: dict[ str, dict[ str, int | bool ] ] = settings
        self.__play: bool = True
        self.__has_played: bool = False
        self.__words: list[ dict[ str, str ] ] = words
        clear_flush(  )


    def __main_menu( self ) -> None:
        """
        privet: main_menu
        - main menu for player!.
        """
        # internal parameters
        settings: dict = self.__settings
        choices: list[ str ] = [ "p", "play", "a", "achivements", "s", "settings", "c", "credits", "e", "exit" ]

        # print main menu
        clear_flush(  )
        line_flush( text= logo, seconds= settings[ "game_settings" ][ "text_speed" ] / 1000 )
        print_flush(text= main_menu_screen, seconds= settings[ "game_settings" ][ "text_speed" ] / 1000 )
        
        ## handel choices
        # get user input
        choice: str = input( "choose an option: " ).lower(  )

        # evaluate user input
        if not( choice in choices ):
            input( f"please give a valid choice from { choices }." )
            self.__main_menu(  )

        if choice in [ "e", "exit" ]:
            if not (self.__has_played):
                self.__play = False
                input( "Then WHY did you come HERE?.")

            else :
                self.__play = False

        if choice in [ "c", "credits" ]:
            self.__credits(  )

        if choice in [ "s", "settings" ]:
            print( "accessing settings is not implemented yet!." )
            self.__main_menu(  )

        if choice in ["a", "achivements"]:
            print( "accessing achivements is not implemented yet!." )
            self.__main_menu(  )

        if choice in ["p", "play"]:
            self.__has_played = True
            self.__game_loop(  )


    def __credits( self ) -> None:
        """
        privet credits
        - shows the game credits.
        """
        
        # internal parameters
        settings = self.__settings

        clear_flush(  )
        line_flush( logo, settings[ "game_settings" ][ "text_speed" ] / 1000 )
        line_flush( credits, settings[ "game_settings" ][ "text_speed" ] / 1000 )
        code: str = input( "\n Press Enter To Continue!." ).lower(  )

        if code == "amegardo":
            clear_flush(  )
            print( "What?." )
            print( "Never minde." )
        
        self.__main_menu(  )


    def __game_loop( self ) -> None:pass


    def run( self ):
        while self.__play:
            self.__main_menu(  )

        clear_flush(  )






## loading section
# loading settings
with open( "settings.json", "r" ) as settings:
    clear_flush(  )
    print( "loading settings." )
    settings_object:dict[ str, dict[ str, int | bool ] ] = json.load( settings )
    delay( 2 ) # for suspense
    print( "settings loaded!." )
    settings.close(  )


with open( "words.json", "r" ) as words:
    print( "loading words!." )
    words_object: dict[ str, list[ dict[ str, str ] ] ] = json.load( words )
    delay( 2 ) # for susy effects
    print( "words loaded!." )
    delay( 0.7 )
    words.close(  )


print( "initializing game." )
game = GamePlay( settings= settings_object, words= words_object["words"] )
delay( 2 ) # same lol
print( "game initialized!" )
delay( 0.7 )



def main() -> None:
    """
    main
    - call main duah!.
    """
    game.run()


if __name__ == "__main__":
    main()



