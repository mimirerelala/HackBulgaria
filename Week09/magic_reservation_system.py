from reservation_System import Reservation_System


class CLI:
    def __init__(self):
        self.input_spell = input("Type your spell, love:")
        self.rs = Reservation_System()
        self.dialog_on = True
        while(self.dialog_on):
            print("Hi")
            if self.input_spell == "show_movies":
                self._show_movies()
            if self.input_spell.startswith("show_movie_projections"):
                self._show_movie_proj()
            if self.input_spell == "make_reservation":
                self._make_reserv()
            if self.input_spell.startswith("cancel_reservation"):
                self._cancel_reserv()
            if self.input_spell == "exit":
                self.rs.close()
                self.dialog_on = False
            if self.input_spell == "help":
                self._print_help()
            self.input_spell = input("Type your spell, love")


    def _show_movies(self):
        self.rs.show_movies()

    def _show_movie_proj(self):
        self.input_spell = self.input_spell.split(" ")
        if len(input_spell) == 2:
            self.rs.show_movie_projections(int(input_spell[1]))
        if len(input_spell) == 3:
            self.rs.show_movie_projections(int(input_spell[1]), input_spell[2])
        # list all results by date
        # for each projection - show the total number of spots

    def _make_reserv(self):
        input_username = input("Please provide a username:")
        if input_username == "exit":
            self.input_spell = "exit"
            return
        user_movie_id = input("Please provide the number of tickets:")
        # show movies to choose movie id
        #
        # show pplaces and ask for (rol.col)

    def _cancel_reserv(self):
        pass

    def _print_help(self):
        pass
