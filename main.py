from flask import Flask, render_template, request, redirect, url_for
import random
import json
import string

app = Flask(__name__)

games = {}  # In-memory game sessions

# --- Helper: generate a unique 5-character game code ---
def generate_room_code(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# --- Home page ---
@app.route('/')
def home():
    return render_template('index.html')

# --- Create game (Player 1) ---
@app.route('/create', methods=['POST'])
def create():
    room_id = generate_room_code()
    games[room_id] = {}  # Empty game state
    return redirect(url_for('game_with_code', room_id=room_id))

# --- Join existing game (Player 2) ---
@app.route('/join', methods=['POST'])
def join():
    room_id = request.form.get('room_id').upper()
    if room_id not in games:
        return "Game not found."
    return redirect(url_for('guess_with_code', room_id=room_id))

# --- Player 1 game screen ---
@app.route('/game/<room_id>')
def game_with_code(room_id):
    with open('cards.json', 'r') as f:
        all_cards = json.load(f)

    selected_cards = random.sample(all_cards, 5)
    games[room_id]['cards'] = selected_cards
    return render_template('game.html', cards=selected_cards, room_id=room_id)

# --- Player 1 submits ranking ---
@app.route('/submit-ranking/<room_id>', methods=['POST'])
def submit_ranking_with_code(room_id):
    cards, ranks = [], []
    for i in range(5):
        card = request.form.get(f'card_{i}')
        rank = request.form.get(f'rank_{i}')
        cards.append(card)
        ranks.append(int(rank))

    ranking = dict(zip(cards, ranks))
    games[room_id]['player1'] = ranking
    return redirect(url_for('waiting_for_player2', room_id=room_id))

# --- Player 1 waits after submitting ---
@app.route('/waiting/<room_id>')
def waiting_for_player2(room_id):
    return render_template('waiting_player2.html', room_id=room_id)

# --- Player 2 guessing screen ---
@app.route('/guess/<room_id>')
def guess_with_code(room_id):
    game = games.get(room_id, {})
    player1_ranking = game.get('player1')
    if not player1_ranking:
        return render_template('waiting_player1.html', room_id=room_id)
    cards = list(player1_ranking.keys())
    return render_template('guess.html', cards=cards, room_id=room_id)

# --- Player 2 submits guess ---
@app.route('/submit-guess/<room_id>', methods=['POST'])
def submit_guess_with_code(room_id):
    cards, ranks = [], []
    for i in range(5):
        card = request.form.get(f'card_{i}')
        rank = request.form.get(f'rank_{i}')
        cards.append(card)
        ranks.append(int(rank))

    guess_ranking = dict(zip(cards, ranks))
    games[room_id]['player2'] = guess_ranking
    return redirect(url_for('show_score', room_id=room_id))

# --- Show results ---
@app.route('/show-score/<room_id>')
def show_score(room_id):
    game = games.get(room_id, {})
    player1 = game.get('player1', {})
    player2 = game.get('player2', {})

    if not player1 or not player2:
        return "Game not complete."

    score = sum(1 for card in player1 if player1[card] == player2.get(card))

    return render_template('score.html', score=score, total=5, player1=player1, player2=player2, room_id=room_id)

@app.route('/status/<room_id>')
def game_status(room_id):
    game = games.get(room_id, {})
    if 'player1' in game and 'player2' in game:
        return {'ready': True}
    return {'ready': False}

if __name__ == '__main__':
    app.run(debug=True)
