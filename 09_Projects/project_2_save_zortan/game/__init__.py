"""
API:
----
This is were we expose public interface, i.e the functionality or objects that the client
can consume. This is also called as API (Application Programming Interface).

We don't want to expose internal details, those are for us as developers of the game.
Internal implementations can change over time and we don't want to introduce breaking
changes to client as much as possible, thus exposing a public API makes things easier.

When we do want to introduce breaking changes, we launch a new version `Game v2`, so it
gives client some time to transition to new code while still utilizing the existing API's.
"""

from .impl import Game, Player
