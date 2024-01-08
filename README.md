# TestTubeYumYums

TestTubeYumYums is a Django-based application designed to provide custom food recommendations to users based on their blood test results. The application utilizes React and Tailwind (both CDN-based) for the front-end and PostgreSQL for the database./
![alt text](https://github.com/jijivishu/TestTubeYumYums/blob/main/TestTubeYumYums/static/TestTubeYumYums/images/readme/LandingPage.png?raw=true)

## Tech Stack

- Django
- React (CDN-based)
- Tailwind (CDN-based)
- PostgreSQL

## Distinctiveness and Complexity

TestTubeYumYums aims to target a unique blend of the health, pharmaceutical, and nutrition sectors by offering users food recommendations based on their blood test reports. The project is distinct in its approach, as it is rare to find applications recommending foods based on nutritional deficiencies using blood test results. In fact, the initial idea was to connect the app with an API, which would offer food items when a certain range of nutrients is given. But due to absence of any such API available, an in-built self-made food database is located as csv file and is hooked with the application for providing recommendations. The complexity of the project lies in its algorithm, which analyzes blood test reports based on permutations of report paramteters and relatable diseases, extracts deficient nutrients based on the analysis, compares them with the user's exact vitamin and mineral reports, and fetches food recommendations from a local CSV database based on nutritional values of the foods.

The project also features a multi-page registration form with partial submissions, validated entries, custom error messages, and responsiveness.

## extra Files and their usage
   ### food_data.csv
   CSV database of food items that contains name of food, their description, image link and all nutritional infos includidng average serving(named recommended portion).
   ### tailwind.config
   Helps in using Tailwind CSS through CDN
   ### LICENSE, .gitignore and README.md
   Self-explanatory names
   ### TestTubeYumYums > apps.py
   Modified to load csv database whenever the app is initialized. Also, when the tables are created for the first time in database, CBC and VitMin tables are populated with high and low range values provided by Dr. LalPathLab.
   ### TestTubeYumYums > analysis_messages.py
   Contains pre-wrote analysis messages for possible combinations of CBC parameters.
   ### TestTubeYumYums > api_codes.py
   No longer in use.
   ### TestTubeYumYums > cbc_analyser.py
   Contains helper functions to return nutrient variation based on low and high CBC parameters
   ### TestTubeYumYums > csv_codes.py
   Contains a global dictionary which links each nutrient with it's csv database table heading and howmuch of that nutrient is considered high/low differentiator in a food item.
   ### TestTubeYumYums > helpers.py
   Contains functions that take in reports and ranges and return dictionary of report analysis and recommended food items.
   ### TestTubeYumYums > nutrient_imbalance.py
   Contains info about what type of parameter deviation can point towards which kind of nutrient imbalance.
   ### TestTubeYumYums > signals.py
   Utilizes Django's in-built post migration signals for populating first two rows of CBC model and VitMin model
when the migrations are made for the very first time.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/jijivishu/TestTubeYumYums.git
   ```

2. Switch to the project directory and create a Python virtual environment:

   ```bash
   cd TestTubeYumYums
   python -m venv env
   ```

3. Activate the virtual environment:

   * Windows:
   ```bash
   env\Scripts\activate
   ```

   * macOS/Linux:
   ```bash
   source env/bin/activate
   ```

   * Windows (using bash):
   ```bash
   source env/Scripts/activate
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
   **Note**: Ensure that PostgreSQL is running at port **5432** with the username and password set to **postgres** and the database name set to **TestTubeYumYumsDB**. Modify settings.py if needed for customisation. \
![alt text](https://github.com/jijivishu/TestTubeYumYums/blob/main/TestTubeYumYums/static/TestTubeYumYums/images/readme/pgadmin.png)
5. Create migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
6. Run the application:

   ```bash
   python manage.py runserver
   ```
   Access the application at http://127.0.0.1:8000/. Ensure an internet connection.

## Registration

The registration process consists of three steps, with the first step being mandatory. Users provide their name, email (unique identifier), date of birth, and password in the first step. Subsequent steps collect additional information such as country, weight, height, blood pressure, and diabetes data.
![alt text](https://github.com/jijivishu/TestTubeYumYums/blob/main/TestTubeYumYums/static/TestTubeYumYums/images/readme/Register%20Menu.png?raw=true)

## Working

Food recommendations are provided based on users' previous test reports. If a user has no test reports uploaded, they are prompted to do so. Users can upload test reports through the '/add' route, customizing the ranges associated with a test report at the time of upload.
![alt text](https://github.com/jijivishu/TestTubeYumYums/blob/main/TestTubeYumYums/static/TestTubeYumYums/images/readme/Form.png?raw=true)

Upon submission, users are redirected to the home page, where they can view recommended food items based on their test results and analysis report.
![alt text](https://github.com/jijivishu/TestTubeYumYums/blob/main/TestTubeYumYums/static/TestTubeYumYums/images/readme/Demo.png?raw=true)

## Future Expectations

### Minor:
* Display nutritional values of individual food items on click.
* Allow partial page submission in the registration form.

### Major:
* Migrate to React instead of using CDN.
* Install Tailwind instead of using CDN.
* Customize food recommendations based on BMI, location, diabetic info, and blood pressure info.
* Consider previous test reports when analyzing the current test report.

Thank you for using TestTubeYumYums!
