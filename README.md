### ⭐About the Project
CryptoTracker is a versatile tool designed to track real-time cryptocurrency prices across multiple exchanges. With CryptoTracker, users can monitor the prices of their favorite cryptocurrencies from popular exchanges such as Binance, Bybit, and Coinbase, not only via the command line interface, but also the Telegram bot.

<h3 align="center">
    🔹
    <a href="https://github.com/7GitGuru/crypto-tracker/issues">Report Bug</a>
    🔹
    <a href="https://github.com/7GitGuru/crypto-tracker/issues">Request Feature</a>
</h3>

---

<h3 align="center">
    
[![GitHub license](https://img.shields.io/github/license/7GitGuru/crypto-tracker.svg)](https://github.com/7GitGuru/crypto-tracker/blob/main/LICENSE)
[![GitHub branches](https://badgen.net/github/branches/7GitGuru/crypto-tracker)](https://github.com/7GitGuru/crypto-tracker/branches)
[![GitHub release](https://img.shields.io/github/release/7GitGuru/crypto-tracker.svg)](https://github.com/7GitGuru/crypto-tracker/releases/)
[![GitHub commits](https://badgen.net/github/commits/7GitGuru/crypto-tracker)](https://github.com/7GitGuru/crypto-tracker/)
[![GitHub stars](https://badgen.net/github/stars/7GitGuru/crypto-tracker)](https://github.com/7GitGuru/crypto-tracker/)

</h3>

### 🚀Features
- 💰Track the prices of various cryptocurrencies.
- 📈Sends updates to a Telegram channel every 15 seconds.
- 🧑‍💻Flexible Command-line Usage.
- ⚙️Easy configuration via a [`config.ini`](https://github.com/7GitGuru/crypto-tracker/blob/telegram/config/config.ini) file.
- 💡Simple and lightweight.

### 🔥The bot utilizes emojis to indicate cryptocurrency price changes:

- 📈: Indicates that the price has increased since the last check.
- 📉: Indicates that the price has decreased since the last check.
- 💲: Indicates that the price remains unchanged since the last check.

These emojis provide a visual representation of the direction in which the cryptocurrency prices are moving, making it easier for users to interpret the changes at a glance.

### 🛠️Project Structure:
<details>
  <summary><b>Structure</b></summary>
    
```
crypto_tracker/
│
├── config/
│   └── config.ini
│  
├── api_handling.py
├── main.py
├── telegram_bot.py
├── requirements.txt
├── LICENSE
└── README.md
```
</details>

### 👨‍💻Installation:
1. **Clone the repository:**
   ```
   git clone https://github.com/7GitGuru/crypto-tracker.git
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Set up a [`config.ini`](https://github.com/7GitGuru/crypto-tracker/blob/telegram/config/config.ini) file.**

4. **Run the bot:**
   ```
   python main.py
   ```
<!--- 🤖 Discord bot [installation instructions](https://github.com/7GitGuru/crypto-tracker/blob/discord/README.md) -->
- 👩‍💻 PyPI package **[installation instructions](https://github.com/7GitGuru/crypto-tracker/blob/cmd/README.md)**

### ⚙️DEMO

<details>
  <summary><b>Telegram</b></summary>
  
![image](https://github.com/7GitGuru/crypto-tracker/assets/154711952/a3c2e1b7-8fc3-41cf-9f3f-6d5a6eebb158)

</details>

<!--- <details>
  <summary><b>Discord</b></summary>
  
![image](https://github.com/7GitGuru/crypto-tracker/assets/154711952/62c2ecb4-01dd-4d11-92a5-0ba406ec585d)

</details> -->

<details>
  <summary><b>PyPI package</b></summary>

![Screenshot 2024-03-17 232730](https://github.com/7GitGuru/crypto-tracker/assets/154711952/88ad5947-9e46-40b8-a3ee-637f650ff96a)

</details>

### ❗Contributions Welcome!

We welcome all forks, suggestions, and improvements to this project. Your contributions help make this project better for everyone. Whether it's fixing a bug, adding a feature, or improving documentation, we appreciate your help in making this project the best it can be.

### ❤️Show your support:

Give a ⭐ if you like this repo!

<a href="https://www.buymeacoffee.com/bohd4n" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-violet.png" alt="Buy Me A Coffee" height= "50px" width= "200px" ></a>
