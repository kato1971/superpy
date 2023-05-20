# Imports
from classes.Arguments import Arguments
from classes.Date import Date
from classes.Router import Router

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def main():
    pass

    Date().get_date()
    
    arguments = Arguments()
    router = Router(arguments.vars)
    router.route()

    return


if __name__ == "__main__":
    main()