from data_collection.twitter_collector import TwitterCollector
import json
from datetime import datetime

def main():
    collector = TwitterCollector()
    
    # Test collection
    tweets = collector.get_naval_activity_tweets()
    
    # Save to JSON for inspection
    output_file = f"collected_tweets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(tweets, f, default=str, indent=2)
    
    print(f"Collected {len(tweets)} tweets")
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    main() 