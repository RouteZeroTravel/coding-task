<img src="images/GithubBanner.png">

<br>

# Coding Task

Hello! Thanks for taking some time to complete this coding task. It's very relevant to our work at RouteZero, so it should provide more insight into the company. If you have any questions or clarifications about anything, don't hesitate to drop us an email and ask (part of working in a team is discussing any parts you're not sure about)!

The task is split into two parts:

1. Building a small API + server to calculate carbon emissions
2. Code review for a small (one file) Flutter web-app

# Part 1: Carbon API

## 🛠 Setup

Over this task, you'll develop a small API + server, starting with calculating travel carbon and ending with creating functionality to help organisations hit their climate goals!

We'd like you to build a server with three endpoints; you can use a language of your choice. 
We've used Typescript + NodeJS for our backend, but you won't be judged on your choice of language. Preferably not something super esoteric (like [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck#:~:text=The%20language's%20name%20is%20a,the%20boundaries%20of%20computer%20programming.)), so we'll be able to understand your code. 

We're looking for:
- Clean logic
- Error handling / edge cases
- Validation of behaviour

### 1. Download the repo
Download this Github repo: https://github.com/RouteZeroTravel/coding-task

### 2. Install test requirements
We've provided tests written in Python to check the functionality of your new API. These call endpoints on your API, and so there's no requirement for your server to be written in Python. To run the tests, you'll need Python3.8+ installed.

```
cd backend/tests
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the tests
Confirm the tests currently all fail (for now).

```
pytest test_carbon_emissions.py
pytest test_journey.py
```

## ☁️ Endpoint 1: Carbon emissions

First, we'd like you to create a RESTful HTTP GET endpoint that uses the Greenhouse Gas Protocol (GHG) "Distance Method" to estimate carbon emissions for a journey. The endpoint should: 

- Parse transport type and distance from the GET request parameters
- Return the estimated carbon emissions for the journey

### ✅ Re-running the tests
To complete this section, the `pytest test_carbon_emissions.py` tests need to pass. The tests expect your server to be running locally. 

⚠️ <b>Be aware you may need to change the `HOST` and/or `PORT` in `backend/test/helper.py` to ensure the tests call your server.</b>

### ☁️ GHG Protocol
In the GHG Distance Method, travel carbon emissions are calculated using the formula:

```
distance (km) * kgCO₂ per km (for a specific transport method)
```

The CO₂ emissions per km can be obtained through various sources, but in this case, we'll be using a subset of the UK Government's DEFRA emissions factors:

| | Transport method | Emissions (kgCO₂/km) |
|--|--|--|
| 🚝 |  Train | 0.03549 |
| 🛫 | Economy flight (short-haul, less than 3600km) | 0.15102 |
| 🛩 | Economy flight (long haul, more than 3600km) | 0.14787  |
| 🛬 | Business flight (short-haul, less than 3600km) | 0.22652 |
| ✈️ | Business flight (long haul, more than 3600km) | 0.42882  |

### 👩‍💻 Example
As an example, to calculate the carbon emissions for a 50km train journey, you'd call:

```
/carbon-emissions/train/50
```

which should return 

```
{
  "emissionsKgCO2": 1.7745
}
```

## 🚝 Part 2: Store a Journey

For step 2, we'd like you to create another RESTful HTTP POST endpoint that:

- Parses a JSON description of a journey (see example below) from the request body 
- Stores a representation of the journey <b>in-memory</b> (you <b>don't</b> need to set up a database)

### ✅ Success criteria

To complete this section, the `pytest test_journey.py` tests need to pass. The tests expect your server to be running locally.

### 👩‍💻 Example
As an example, POSTing to 

```
/journey
```

with the JSON body:

```json
{
  "transport": "economyFlight",
  "distanceKm": 450,
  "durationHours": 1.5
}
```

should return an id that identifies the journey and store the POSTed journey. For example:

```json
{
  "id": "abcdefg"
}
```

## 📉 Endpoint 3: Carbon-cutting actions 

We're working with companies to develop a suite of tools and actions that they can use to cut their carbon emissions. We also want to provide organisations with a way to predict the carbon impact of these actions _before_ rolling them out to staff.

For this task, we'll evaluate the impact of two "carbon actions":

1. Only allowing business class flights over 12 hours; any flights under 12 hours must be economy class
2. Only allowing economy flights over 500km; any economy flights under 500km must be taken by train

### ✅ Spec

We'd like you to design an HTTP POST endpoint that:

- Accepts an argument describing one _or more_ of the carbon action(s) above
- Accept a list of journey IDs returned by the `"/journey"` endpoint
- Returns the sum of carbon emissions for selected journeys after adopting the chosen carbon action(s)
- Written in a way that allows new carbon actions to be easily added in the future (e.g. think about how you're storing the actions)
- Write test case(s) to demonstrate the functionality (these can continue with the existing Python script, or you can use a different language)

### 🤔 Tips

- If replacing one transport type with another (e.g. swapping an economy flight for a train), you can assume the journey distance and time is unchanged

### 👩‍💻 Example
Say a company records that they've taken two journeys:

1. Train journey (100km, 2 hours, 3.549 kgCO2)
2. Economy flight (450km, 1.5 hours, 67.959 kgCO2)

Next, the company wants to evaluate the impact of adopting carbon action #2 (no economy flights over 500km) on both journeys. 

The API endpoint should:
- Accept a list of journey IDs representing both the journeys above
- Accept an argument describing carbon action #2
- Return 19.5195 kgCO2, because: 
  - The 450km economy flight was shifted to a train journey of the same distance and time (train @ 450km = 15.9705 kgCO2)
  - The original 100km train journey was unchanged (3.549 kgCO2)

## 🌍 Part 4: All new carbon-cutting actions!

For this final part, imagine a company has implemented the two carbon actions above. Now, they're looking for new ways to cut carbon. We'd like you to come up with a new carbon-cutting action and add the new action to Endpoint #3. Be as creative as you like!

### ✅ Spec

- Add a new carbon-cutting action to Endpoint #3
- Add test(s) to show us how it works

## 🚀 To submit
- Push code to a private repository
- Add collaborator `bakersmitha`
- We'll clone and run locally, so let us know if there are any commands to run your server and additional test case(s)

# Part 2: Frontend code review

For this part of the task, we'd like you to take a look at a small Flutter web app (just one file), and tell us what you think. We're specifically looking for you to highlight specific problems around coding best practises and any associated changes you'd make to fix those problems.

The web app is available in this repo in the [`carbon_app`](carbon_app) directory. The file we'd like you to look is [`carbon_app/lib/main.dart`](carbon_app/lib/main.dart), specifically the `TransportCarbonAppState` class.

## 🤔 Tips
- You don't need to make any changes. Instead, just tell or show us your thoughts.
- You don't need to run the app, but feel free to if it helps you (it requires Flutter to be installed and can be run with `flutter run -d chrome`)
- A lot of our frontend codebase is written in Flutter, and so we've written this app in Flutter. However, the problems in the app aren't Flutter specific. Instead, they relate to coding best practises in-general
- This is a toy example, but imagine it was part of a larger, production codebase

## 🚀 To submit
- Use your preferred text editor to write up your thoughts
- Send an email to jobs@routezero.world with a PDF or doc attachment 
- Include "technical frontend review" in the email subject