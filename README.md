# ETAS: Emerging Threats Alert System

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)

## Overview

ETAS (Emerging Threats Alert System) is an open-source intelligence tool designed to detect early warning signals of naval military exercises and activities in the Pacific region. Using natural language processing and a specialized scoring algorithm, ETAS monitors social media and news sources to identify patterns that may indicate emerging geopolitical developments.

### Key Features

- **Real-time monitoring** of Twitter/X and other open sources
- **Advanced NLP processing** to identify naval exercise indicators
- **Risk scoring algorithm** to assess significance of detected signals
- **Automated alerts** via email/SMS when significant events are detected
- **Focused primarily on Pacific naval activities** with potential to expand to other scenarios

## Project Motivation

The gap between when geopolitical events begin developing and when they're widely reported can be critical for analysts, journalists, and decision-makers. ETAS aims to narrow this gap by providing earlier detection of potential naval activities through the analysis of open-source signals.

This project explores the intersection of defense intelligence, natural language processing, and real-time alert systems to create a practical tool for open-source intelligence gathering.

## Technology Stack

- **Backend:** Python
- **Data Processing:** spaCy, HuggingFace Transformers
- **Data Collection:** Tweepy (Twitter/X API)
- **Storage:** PostgreSQL
- **Alerting:** Twilio (SMS), SendGrid (Email)
- **Deployment:** Docker, AWS

## Current Status

ETAS is currently in active development. The initial focus is on building a reliable detection system for naval exercises in the Pacific region, with plans to expand to other scenarios in the future.

### Roadmap

- [x] Project planning and architecture
- [ ] Data collection framework
- [ ] NLP processing pipeline
- [ ] Scoring algorithm development
- [ ] Alert system implementation
- [ ] Initial deployment and testing
- [ ] User feedback integration
- [ ] Expansion to additional scenarios

## Getting Started

*Detailed installation and setup instructions will be added as the project develops*

### Prerequisites

- Python 3.9+
- Twitter/X API credentials
- PostgreSQL database
- Twilio account (for SMS alerts)

### Basic Setup

```bash
# Clone repository
git clone https://github.com/yourusername/etas.git
cd etas

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys and configuration

# Run initial setup
python setup.py
```

## Usage Examples

```python
# Example code will be provided as the project develops
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project is inspired by the need for better early warning systems in the open-source intelligence community
- Thanks to all contributors and feedback providers
