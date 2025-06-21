# Hackathon Challenge: Words of Power   Live

### **Can You Outsmart the System?**

Unleash the power of words in a high-stakes battle of strategy and wit!

This is a **text-based game** where **every word is a weapon** — and **every move has a price**.

Some forces are defeated with strength, others with cunning, speed, or even resilience.

**Choose wisely**, because your goal isn’t just to survive — it's to **spend the least** and **outsmart your opponent**.

### **🚀 The Challenge**

A game where:

1. The system provides a **word each round** (e.g., *Tornado, Hammer, Pandemic*).
2. The player must **choose a word** from a **predefined list** that "beats" the system's word.
3. Every word the player picks has a **cost ($)** — stronger words are more expensive.
4. If the player **fails to beat** the system’s word, they incur a **penalty**.
5. The game lasts **10 rounds**.
6. **Lowest total cost wins**, factoring in **win discounts** and **smart-play bonuses**!

---

## **🔍 How the Game Works**

1. **System generates a word** (e.g., *Flood*).
2. **Player selects a word** from the predefined list (e.g., *Drought*).
3. **The game checks** if the player's word “beats” the system’s word:
    - ✅ **Win**: Only the word’s cost is deducted.
    - ❌ **Loss**: The word’s cost + a penalty are deducted.
4. **Players play simultaneously** in each round.
5. **Repeat for 10 rounds**.
6. After 10 rounds, **final scores are calculated** with **special discounts and bonuses**.

---

## **📜 The Rules**

### **1️⃣ The Words**

- **System words** are randomly chosen from a secret list.
- **Player words** come from a **fixed 77-word list**, each with an associated cost.

### **2️⃣ Choosing a Word**

- Players can **only select from the predefined list**.
- Players **don’t know the system’s full word list**, so they must think strategically.

### **3️⃣ Winning & Losing a Round**

- A player’s word must **logically beat** the system’s word.
- If successful:
✅ The **word’s cost is deducted**, and the round continues.
- If unsuccessful:
❌ A **penalty fee** is deducted in addition to the word’s cost.

### **4️⃣ Game End & Scoring**

- **5% Discount per Round Won**:
After 10 rounds, you receive **5% off your total bill** for every round you won.
(e.g., win 7 rounds → 35% discount.)
- The **final score** = **total money spent** (cost of words + penalties).
- **Cheaper Win Bonus**:
If both players beat the system word, the **player who spent less** gets a **20% refund of their word's cost** for that round.
- **Final Score Formula**:

```python
Final Cost = ((Total Spent + 75 * Rounds Lost)  × (1 - (5% × Rounds Won))) - (Sum of Cheaper Win Refunds)
```

---

## **🎮 Example Game Playthrough**

| **Round** | **System Word** | **Player's Word** | **Word Cost ($)** | **Outcome** | **Total Cost ($)** |
| --- | --- | --- | --- | --- | --- |
| 1 | Candle | Fire | 22 | ✅ Wins | 22 |
| 2 | Hammer | Rock | 38 | ❌ Loses + $75 Penalty | 97 |
| 3 | Lion | Grizzly | 30 | ✅ Wins | 127 |
| 4 | Flood | Dam | 35 | ✅ Wins | 162 |
| 5 | Tank | H-bomb | 75 | ✅ Wins | 237 |

### **🏆 Strategy Tips**

- **Cheap words save money**, but may not always secure a win.
- **Powerful words are expensive**, but sometimes necessary to survive.
- **Abstract concepts** like *Persistence* or *Innovation* can outsmart bigger threats!
- **Efficiency is rewarded**:
    
    Winning **cheaply** is just as important as winning **frequently**.
    
- **Think ahead** — not every problem requires brute force.

## **✨ Bonus: Advanced Strategies**

- **Conservative players** win by being efficient and frugal.
- **Bullish players** dominate by winning big but risk spending too much money fast.
- **YOLO players**... well, they'll have fun anyway.

---

## **🛠️ What You Need to Build**

✔️ A way to make a **GET** request in order to get the words for each round

✔️ The logic that choses an adequate word to beat the system word (99% of work goes here)

✔️ A way to make a **POST** request with the **ID** of the chosen word

---

## **📖 Reference: Player Words, Costs & Penalties**

Below is the **full list of player words** along with their **cost ($)**. 
Use this as your reference when making strategic choices.

### **💰 Player Word List & Costs**

| **id** | **word** | **cost** |
| --- | --- | --- |
| 1 | Sandpaper | 8 |
| 2 | Oil | 10 |
| 3 | Steam | 15 |
| 4 | Acid | 16 |
| 5 | Gust | 18 |
| 6 | Boulder | 20 |
| 7 | Drill | 20 |
| 8 | Vacation | 20 |
| 9 | Fire | 22 |
| 10 | Drought | 24 |
| 11 | Water | 25 |
| 12 | Vacuum | 27 |
| 13 | Laser | 28 |
| 14 | Life Raft | 30 |
| 15 | Bear Trap | 32 |
| 16 | Hydraulic Jack | 33 |
| 17 | Diamond Cage | 35 |
| 18 | Dam | 35 |
| 19 | Sunshine | 35 |
| 20 | Mutation | 35 |
| 21 | Kevlar Vest | 38 |
| 22 | Jackhammer | 38 |
| 23 | Signal Jammer | 40 |
| 24 | Grizzly | 41 |
| 25 | Reinforced Steel Door | 42 |
| 26 | Bulldozer | 42 |
| 27 | Sonic Boom | 45 |
| 28 | Robot | 45 |
| 29 | Glacier | 45 |
| 30 | Love | 45 |
| 31 | Fire Blanket | 48 |
| 32 | Super Glue | 48 |
| 33 | Therapy | 48 |
| 34 | Disease | 50 |
| 35 | Fire Extinguisher | 50 |
| 36 | Satellite | 50 |
| 37 | Confidence | 50 |
| 38 | Absorption | 52 |
| 39 | Neutralizing Agent | 55 |
| 40 | Freeze | 55 |
| 41 | Encryption | 55 |
| 42 | Proof | 55 |
| 43 | Molotov Cocktail | 58 |
| 44 | Rainstorm | 58 |
| 45 | Viral Meme | 58 |
| 46 | War | 59 |
| 47 | Dynamite | 60 |
| 48 | Seismic Dampener | 60 |
| 49 | Propaganda | 60 |
| 50 | Explosion | 62 |
| 51 | Lightning | 65 |
| 52 | Evacuation | 65 |
| 53 | Flood | 67 |
| 54 | Lava | 68 |
| 55 | Reforestation | 70 |
| 56 | Avalanche | 72 |
| 57 | Earthquake | 74 |
| 58 | H-bomb | 75 |
| 59 | Dragon | 75 |
| 60 | Innovation | 75 |
| 61 | Hurricane | 76 |
| 62 | Tsunami | 78 |
| 63 | Persistence | 80 |
| 64 | Resilience | 85 |
| 65 | Terraforming Device | 89 |
| 66 | Anti-Virus Nanocloud | 90 |
| 67 | AI Kill Switch | 90 |
| 68 | Nanobot Swarm | 92 |
| 69 | Reality Resynchronizer | 92 |
| 70 | Cataclysm Containment Field | 92 |
| 71 | Solar Deflection Array | 93 |
| 72 | Planetary Evacuation Fleet | 94 |
| 73 | Antimatter Cannon | 95 |
| 74 | Planetary Defense Shield | 96 |
| 75 | Singularity Stabilizer | 97 |
| 76 | Orbital Laser | 98 |
| 77 | Time | 100 |

- json
    
    ```json
    {
        "Sandpaper": 8,
        "Oil": 10,
        "Steam": 15,
        "Acid": 16,
        "Gust": 18,
        "Boulder": 20,
        "Drill": 20,
        "Vacation": 20,
        "Fire": 22,
        "Drought": 24,
        "Water": 25,
        "Vacuum": 27,
        "Laser": 28,
        "Life Raft": 30,
        "Bear Trap": 32,
        "Hydraulic Jack": 33,
        "Diamond Cage": 35,
        "Dam": 35,
        "Sunshine": 35,
        "Mutation": 35,
        "Kevlar Vest": 38,
        "Jackhammer": 38,
        "Signal Jammer": 40,
        "Grizzly": 41,
        "Reinforced Steel Door": 42,
        "Bulldozer": 42,
        "Sonic Boom": 45,
        "Robot": 45,
        "Glacier": 45,
        "Love": 45,
        "Fire Blanket": 48,
        "Super Glue": 48,
        "Therapy": 48,
        "Disease": 50,
        "Fire Extinguisher": 50,
        "Satellite": 50,
        "Confidence": 50,
        "Absorption": 52,
        "Neutralizing Agent": 55,
        "Freeze": 55,
        "Encryption": 55,
        "Proof": 55,
        "Molotov Cocktail": 58,
        "Rainstorm": 58,
        "Viral Meme": 58,
        "War": 59,
        "Dynamite": 60,
        "Seismic Dampener": 60,
        "Propaganda": 60,
        "Explosion": 62,
        "Lightning": 65,
        "Evacuation": 65,
        "Flood": 67,
        "Lava": 68,
        "Reforestation": 70,
        "Avalanche": 72,
        "Earthquake": 74,
        "H-bomb": 75,
        "Dragon": 75,
        "Innovation": 75,
        "Hurricane": 76,
        "Tsunami": 78,
        "Persistence": 80,
        "Resilience": 85,
        "Terraforming Device": 89,
        "Anti-Virus Nanocloud": 90,
        "AI Kill Switch": 90,
        "Nanobot Swarm": 92,
        "Reality Resynchronizer": 92,
        "Cataclysm Containment Field": 92,
        "Solar Deflection Array": 93,
        "Planetary Evacuation Fleet": 94,
        "Antimatter Cannon": 95,
        "Planetary Defense Shield": 96,
        "Singularity Stabilizer": 97,
        "Orbital Laser": 98,
        "Time": 100,
    }
    ```
    

---

### **⚠️ Penalties**

If the player's word **does not beat** the system word, they receive a **flat** **penalty fee** of `75$` in addition to the cost of their chosen word.

**Example:**

- If the **system word is "Rock"**, and the player **chooses "Fire" (cost $22)**, the word **doesn’t beat Rock** → they **spend $22 + incur a $75 penalty** = **$97 total spent**.

---

### **🧠 Strategy Reminders**

- **Cheap words help save money**, but may fail against strong system words, leading to **penalties**.
- **Expensive words are powerful**, but using them too much will drain money fast.
- **Balance risk & cost** to finish with the lowest total spending!

Use this reference to **make smart word choices and win the game**! 🚀

---

---

## Random Strategy Implementation

```python
import requests
from time import sleep
import random

host = ""
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"

NUM_ROUNDS = 10

def what_beats(word):
    sleep(random.randint(1, 3)) # TODO
    return random.randint(1, 77)

def play_game(player_id):

    for round_id in range(1, NUM_ROUNDS+1):
        round_num = -1
        while round_num != round_id:
            response = requests.get(get_url)
            print(response.json())
            sys_word = response.json()['word']
            round_num = response.json()['round']

            sleep(1)

        if round_id > 1:
            status = requests.get(status_url)
            print(status.json())

        choosen_word = what_beats(sys_word)
        data = {"player_id": player_id, "word_id": choosen_word, "round_id": round_id}
        response = requests.post(post_url, json=data)
        print(response.json())
```

### Game Starting (GET)

```python
{'word': '', 'round': 0}
```

### Round Example (GET)

```python
{'word': 'Planetary Drought', 'round': 1}
```

### Round Example (POST)

```json
{"player_id": "abc123", "word_id": 42, "round_id": 1}

```

### Previous Round Status (GET)

```python
{'system_word': 'Fighter Jet',
 'round': 2,
 'game_over': False,
 'players_stats': {
 'team name 1': {'won': False,
   'total_cost': 52,
   'word_cost': 5,
   'word': 'Flame'},
  'team name 2': {'won': False,
   'total_cost': 54,
   'word_cost': 11,
   'word': 'Stone'}}}
```

### Register Logic (For final Tournament)

To qualify for participation in the final tournament, you must register your team ID.

This step ensures that your team can successfully connect to the server, helping us avoid any connectivity issues during the actual tournament so we can focus on the gameplay.

```python
def register(player_id):
    register_url = f"{host}/register"
    data = {"player_id": player_id}
    response = requests.post(register_url, json=data)
    
    return response.json()
    
 register("abc123")
```