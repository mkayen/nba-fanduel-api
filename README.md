# NBA FanDuel Data Scraper and API

This application crawls NBA player data from FanDuel's DFS projections page and provides a JSON API with automatic refresh every 2 hours.

## Features

- **Web Scraping**: Automatically scrapes player data from FanDuel NBA projections
- **Database Storage**: Stores data in SQLite database
- **JSON API**: RESTful API endpoints for accessing player data
- **Auto Refresh**: Automatically updates data every 2 hours
- **Position Filtering**: Filter players by position (PG, SG, SF, PF, C)

## Data Fields

- Player Name
- Position
- Price
- Projected FanDuel Points
- Points
- Rebounds
- Assists
- Steals

## API Endpoints

- `GET /api/players` - Get all players
- `GET /api/players/{position}` - Get players by position
- `POST /api/refresh` - Manually trigger data refresh
- `GET /api/status` - Get API status and last update time

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Chrome Browser** (required for Selenium):
   - Download and install Google Chrome
   - The application will automatically download ChromeDriver

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the API**:
   - API will be available at `http://localhost:5000`
   - Example: `http://localhost:5000/api/players`

## Usage Examples

### Get All Players
```bash
curl http://localhost:5000/api/players
```

### Get Players by Position
```bash
curl http://localhost:5000/api/players/PG
```

### Manual Refresh
```bash
curl -X POST http://localhost:5000/api/refresh
```

### Check Status
```bash
curl http://localhost:5000/api/status
```

## Response Format

```json
{
  "success": true,
  "count": 150,
  "data": [
    {
      "player_name": "LeBron James",
      "position": "SF",
      "price": 12000,
      "projected_fanduel_points": 45.2,
      "points": 25.1,
      "rebounds": 7.8,
      "assists": 6.9,
      "steals": 1.2,
      "last_updated": "2024-01-15 10:30:00"
    }
  ]
}
```

## Notes

- The scraper uses Selenium with Chrome in headless mode
- Data is automatically refreshed every 2 hours
- The application creates a SQLite database file (`nba_data.db`)
- All scraping is done in compliance with FanDuel's terms of service

## Troubleshooting

- Ensure Chrome browser is installed
- Check that all dependencies are properly installed
- Monitor logs for any scraping errors
- The application may need adjustments if FanDuel changes their HTML structure
