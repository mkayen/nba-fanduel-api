#!/usr/bin/env python3
"""
API Health Monitor for NBA FanDuel API
"""

import requests
import time
import json
from datetime import datetime

class APIMonitor:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.last_check = None
        self.health_status = "unknown"
    
    def check_health(self):
        """Check API health status"""
        try:
            response = requests.get(f"{self.base_url}/api/status", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.health_status = "healthy"
                self.last_check = datetime.now()
                return {
                    'status': 'healthy',
                    'last_update': data.get('last_update'),
                    'timestamp': datetime.now().isoformat()
                }
            else:
                self.health_status = "unhealthy"
                return {
                    'status': 'unhealthy',
                    'error': f"HTTP {response.status_code}",
                    'timestamp': datetime.now().isoformat()
                }
        except requests.exceptions.RequestException as e:
            self.health_status = "unreachable"
            return {
                'status': 'unreachable',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def get_player_count(self):
        """Get current player count"""
        try:
            response = requests.get(f"{self.base_url}/api/players", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('count', 0)
            return 0
        except:
            return 0
    
    def monitor_continuously(self, interval=60):
        """Monitor API continuously"""
        print(f"🔍 Starting API monitoring (checking every {interval} seconds)")
        print(f"🌐 API URL: {self.base_url}")
        print("=" * 60)
        
        while True:
            health = self.check_health()
            player_count = self.get_player_count()
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status_icon = "✅" if health['status'] == 'healthy' else "❌"
            
            print(f"{timestamp} {status_icon} Status: {health['status']} | Players: {player_count}")
            
            if health['status'] != 'healthy':
                print(f"   ⚠️  Error: {health.get('error', 'Unknown error')}")
            
            time.sleep(interval)
    
    def run_health_check(self):
        """Run a single health check"""
        health = self.check_health()
        player_count = self.get_player_count()
        
        print("�� NBA FanDuel API Health Check")
        print("=" * 40)
        print(f"Status: {health['status']}")
        print(f"Players in database: {player_count}")
        print(f"Last update: {health.get('last_update', 'Never')}")
        print(f"Check time: {health['timestamp']}")
        
        if health['status'] != 'healthy':
            print(f"Error: {health.get('error', 'Unknown error')}")
            return False
        
        return True

if __name__ == "__main__":
    import sys
    
    monitor = APIMonitor()
    
    if len(sys.argv) > 1 and sys.argv[1] == "continuous":
        try:
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
            monitor.monitor_continuously(interval)
        except KeyboardInterrupt:
            print("\n👋 Monitoring stopped")
    else:
        success = monitor.run_health_check()
        sys.exit(0 if success else 1)
