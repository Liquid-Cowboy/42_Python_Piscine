from ex4.TournamentCard import TournamentCard
from typing import Any


class TournamentPlatform():
    def __init__(self) -> None:
        self._tournament_cards: dict = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        try:
            if not isinstance(card, TournamentCard):
                raise TypeError(f'{card} is not a valid TournamentCard')
        except TypeError as e:
            print('[ERROR]:', e)
            print('card id set to ""')
            return ''
        card_name: list[str] = card._name.split()
        card_id: str = card_name[-1].lower()
        i: int = 1
        for ident in list(self._tournament_cards.keys()):
            if card_id in ident:
                i += 1
        if i > 999:
            return ''
        count: str = '00' if i < 10 else '0' if i < 100 else ''
        card_id += '_' + count + str(i)
        self._tournament_cards.update({card_id: card})
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        try:
            if not isinstance(card1_id, str):
                raise TypeError(f'{card1_id} is not a valid str')
            if not isinstance(card2_id, str):
                raise TypeError(f'{card2_id} is not a valid str')
            player1: TournamentCard = self._tournament_cards[card1_id]
            player2: TournamentCard = self._tournament_cards[card2_id]
        except (TypeError, KeyError) as e:
            print('[ERROR]:', e)
            return {}

        self._matches_played += 1

        if player1._health <= 0 and player2._health <= 0:
            return {
                'match_result': 'draw',
                'player1': card1_id,
                'player2': card2_id,
                'player1_rating': player1._rating,
                'player2_rating': player2._rating,
                }

        while player1._health > 0 and player2._health > 0:
            player1.attack(player2)
            if player2._health > 0:
                player2.attack(player1)
        match_result: dict[str, Any] = {
            'winner': None,
            'loser': None,
            'winner_rating': None,
            'loser_rating': None,
        }

        if player1._health > 0 and player2._health <= 0:
            player1.update_wins(player1._record[0] + 1)
            player2.update_losses(player2._record[1] + 1)
            match_result['winner'] = card1_id
            match_result['loser'] = card2_id
            match_result['winner_rating'] = player1.calculate_rating()
            match_result['loser_rating'] = player2.calculate_rating()
            return match_result

        player2.update_wins(player2._record[0] + 1)
        player1.update_losses(player1._record[1] + 1)
        match_result['winner'] = card2_id
        match_result['loser'] = card1_id
        match_result['winner_rating'] = player2.calculate_rating()
        match_result['loser_rating'] = player1.calculate_rating()
        return match_result

    def get_leaderboard(self) -> list:
        sorted_ratings: list[TournamentCard] = sorted(
            self._tournament_cards.values(),
            key=lambda card: card._rating, reverse=True)
        i: int = 0
        leaderboard: list[str] = []
        for card in sorted_ratings:
            i += 1
            leaderboard.append(f'{i}. {card._name} - Rating: {card._rating} '
                               f'({card._record[0]}-{card._record[1]})')
        return leaderboard

    def generate_tournament_report(self) -> dict:
        return {
            'total_cards': len(self._tournament_cards.values()),
            'matches_played': self._matches_played,
            'avg_rating': int(sum(
                [r._rating for r in self._tournament_cards.values()]) /
                           len(self._tournament_cards)),
            'platform_status': 'active'
        }
