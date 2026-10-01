"""bcweb: a client for the UNSW Battlecode competition website (game.battlecode.au)."""

from .core import (BcError, availability, fetch, login, main, our_team_id, page_data,
                   resolve_team, tfetch)

__all__ = ["BcError", "availability", "fetch", "login", "main", "our_team_id", "page_data",
           "resolve_team", "tfetch"]
