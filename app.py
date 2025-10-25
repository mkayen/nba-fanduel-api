#!/usr/bin/env python3
"""
NBA FanDuel API - Minimal Railway Version
"""

import sqlite3
import json
from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Sample data
SAMPLE_PLAYERS = [
    {
        'player_name': 'LeBron James',
        'position': 'SF',
        'price': 12000,
        'projected_fanduel_points': 45.2,
        'points': 25.1,
        'rebounds': 7.8,
        'assists': 6.9,
        'steals': 1.2,
        'last_updated': '2025-01-24 10:30:00'
    },
    {
        'player_name': 'Stephen Curry',
        'position': 'PG',
        'price': 11500,
        'projected_fanduel_points': 42.8,
        'points': 28.4,
        'rebounds': 4.2,
        'assists': 6.1,
        'steals': 1.1,
        'last_updated': '2025-01-24 10:30:00'
    },
    {
        'player_name': 'Giannis Antetokounmpo',
        'position': 'PF',
        'price': 13000,
        'projected_fanduel_points': 48.5,
        'points': 30.2,
        'rebounds': 11.8,
        'assists': 5.4,
        'steals': 1.0,
        'last_updated': '2025-01-24 10:30:00'
    },
    {
        'player_name': 'Luka Doncic',
        'position': 'PG',
        'price': 12500,
        'projected_fanduel_points': 46.3,
        'points': 27.8,
        'rebounds': 8.1,
        'assists': 8.9,
        'steals': 1.3,
        'last_updated': '2025-01-24 10:30:00'
    },
    {
        'player_name': 'Joel Embiid',
        'position': 'C',
        'price': 11000,
        'projected_fanduel_points': 44.7,
        'points': 26.9,
        'rebounds': 11.2,
        'assists': 3.2,
        'steals': 0.9,
        'last_updated': '2025-01-24 10:30:00'
    },
    {
        'player_name': 'Kevin Durant',
        'position': 'SF',
        'price': 10800,
        'projected_fanduel_points': 43.1,
        'points': 27.3,
        'rebounds': 6.7,
        'assists': 5.0,
        'steals': 0.8,
        'last_updated': '2025-01-24 10:30:00'
    },
    {
        'player_name': 'Nikola Jokic',
        'position': 'C',
        'price': 12800,
        'projected_fanduel_points': 47.8,
        'points': 24.8,
        'rebounds': 11.8,
        'assists': 9.8,
        'steals': 1.3,
        'last_updated': '2025-01-24 10:30:00'
    },
    {
        'player_name': 'Jayson Tatum',
        'position': 'SF',
        'price': 11200,
        'projected_fanduel_points': 44.5,
        'points': 26.9,
        'rebounds': 8.1,
        'assists': 4.9,
        'steals': 1.0,
        'last_updated': '2025-01-24 10:30:00'
    }
]

@app.route('/')
def home():
    """Home page with API documentation"""
    return jsonify({
        'message': 'NBA FanDuel Data API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'GET /api/players': 'Get all players',
            'GET /api/players/{position}': 'Get players by position (PG, SG, SF, PF, C)',
            'GET /api/status': 'API health status'
        },
        'example': '/api/players'
    })

@app.route('/api/players', methods=['GET'])
def get_players():
    """Get all players"""
    return jsonify({
        'success': True,
        'count': len(SAMPLE_PLAYERS),
        'data': SAMPLE_PLAYERS
    })

@app.route('/api/players/<position>', methods=['GET'])
def get_players_by_position(position):
    """Get players by position"""
    position = position.upper()
    filtered_players = [p for p in SAMPLE_PLAYERS if p['position'] == position]
    
    return jsonify({
        'success': True,
        'count': len(filtered_players),
        'position': position,
        'data': filtered_players
    })

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get API status"""
    return jsonify({
        'success': True,
        'status': 'running',
        'last_update': '2025-01-24 10:30:00',
        'players_count': len(SAMPLE_PLAYERS)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
