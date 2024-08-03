import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import TennisPlayer, Tournament, Match
from django.db.models import Count, Q


def get_tennis_players(search_name=None, search_country=None):
    if search_name is not None and search_country is not None:
        players = TennisPlayer.objects.filter(
            Q(full_name__icontains=search_name),
            Q(country__icontains=search_country)
        )
    elif search_name is not None:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name)
    elif search_country is not None:
        players = TennisPlayer.objects.filter(country__icontains=search_country)
    else:
        return ""

    players = players.order_by('ranking')

    if players.exists():
        return "\n".join(
            [f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}" for player in
             players]
        )
    else:
        return ""


def get_top_tennis_player():
    # top_player = TennisPlayer.objects.annotate(wins_count=Count('matches_won')).order_by('-wins_count',
    #                                                                                      'full_name').first()
    #
    # if top_player and top_player.wins_count > 0:
    #     return f"Top Tennis Player: {top_player.full_name} with {top_player.wins_count} wins."
    # else:
    #     return ""
    a = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    if a:
        return f"Top Tennis Player: {a.full_name} with {a.wins_count} wins."
    return ""


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.annotate(matches_count=Count('matches')).order_by('-matches_count', 'ranking').first()

    if player and player.matches_count > 0:
        return f"Tennis Player: {player.full_name} with {player.matches_count} matches played."
    else:
        return ""


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments = Tournament.objects.filter(surface_type__icontains=surface).annotate(
        num_matches=Count('match')).order_by('-start_date')

    if tournaments.exists():
        return "\n".join(
            [f"Tournament: {tournament.name}, start date: {tournament.start_date}, matches: {tournament.num_matches}"
             for tournament in tournaments]
        )
    else:
        return ""


def get_latest_match_info():
    latest_match = Match.objects.order_by('-date_played', '-id').first()

    if not latest_match:
        return ""

    players = sorted([player.full_name for player in latest_match.players.all()])
    players_str = " vs ".join(players)
    winner_str = "TBA" if latest_match.winner is None else latest_match.winner.full_name

    return (f"Latest match played on: {latest_match.date_played}, tournament: {latest_match.tournament.name}, "
            f"score: {latest_match.score}, players: {players_str}, winner: {winner_str}, summary: {latest_match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    try:
        tournament = Tournament.objects.get(name=tournament_name)
    except Tournament.DoesNotExist:
        return "No matches found."

    matches = Match.objects.filter(tournament=tournament).order_by('-date_played')

    if not matches.exists():
        return "No matches found."

    return "\n".join(
        [
            f"Match played on: {match.date_played}, score: {match.score}, winner: {'TBA' if match.winner is None else match.winner.full_name}"
            for match in matches]
    )
