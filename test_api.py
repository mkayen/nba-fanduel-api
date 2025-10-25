#!/usr/bin/env python3
"""
Test script for NBA FanDuel API
"""

import requests
import json
import time

def test_api():
    base_url = "http://localhost:5000"
    
    print("Testing NBA FanDuel API...")
    print("=" * 50)
    
    # Test 1: Check API status
    print("1. Testing API status...")
    try:
        response = requests.get(f"{base_url}/api/status")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ API Status: {data.get('status', 'unknown')}")
            print(f"✓ Last Update: {data.get('last_update', 'never')}")
        else:
            print(f"✗ Status check failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Status check error: {e}")
    
    print()
    
    # Test 2: Get all players
    print("2. Testing get all players...")
    try:
        response = requests.get(f"{base_url}/api/players")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Retrieved {data.get('count', 0)} players")
            if data.get('data'):
                print(f"✓ Sample player: {data['data'][0].get('player_name', 'Unknown')}")
        else:
            print(f"✗ Get players failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Get players error: {e}")
    
    print()
    
    # Test 3: Get players by position
    print("3. Testing get players by position (PG)...")
    try:
        response = requests.get(f"{base_url}/api/players/PG")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Retrieved {data.get('count', 0)} point guards")
        else:
            print(f"✗ Get PG players failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Get PG players error: {e}")
    
    print()
    
    # Test 4: Manual refresh
    print("4. Testing manual refresh...")
    try:
        response = requests.post(f"{base_url}/api/refresh")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Manual refresh: {data.get('message', 'Success')}")
        else:
            print(f"✗ Manual refresh failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Manual refresh error: {e}")
    
    print()
    print("API testing completed!")

if __name__ == "__main__":
    test_api()
