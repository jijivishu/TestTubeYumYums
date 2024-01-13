# TestTubeYumYums

TestTubeYumYums is a Django-based application designed to provide custom food recommendations to users based on their blood test results. The application utilizes React and Tailwind (both CDN-based) for the front-end and PostgreSQL for the database. \
![alt text](https://github.com/jijivishu/TestTubeYumYums/blob/main/TestTubeYumYums/static/TestTubeYumYums/images/readme/LandingPage.png?raw=true)

## Tech Stack

- Django
- React (CDN-based)
- Tailwind (CDN-based)
- PostgreSQL

## Distinctiveness and Complexity

TestTubeYumYums aims to target a unique blend of the health, pathology, and nutrition sectors by offering users food recommendations based on their blood test reports. The project takes a unique approach because it is uncommon to find applications that use blood test results to recommend foods based on nutritional deficits and excess. Actually, the original plan was to integrate the app with a public API that would provide dietary options based on a range of nutrients. However, because there isn't a similar API available, a self-made food database that is integrated into the programme and accessible as a CSV file makes recommendations. The intricacy of the project is found in its algorithm, which examines blood test results according to variations in report parameters and related illnesses, extracts nutrients that are lacking, compares those deficiencies to the user's precise vitamin and mineral reports, and retrieves food recommendations from the local CSV database based on the nutritional content of the items.

A multi-page registration form with responsiveness, validated entries, bespoke error messages, and incomplete submissions is another element of the project.

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

## Contributing

Please read our [Contribution Guidelines](.github/CONTRIBUTING.md) before contributing to the project.

*Thank you for using TestTubeYumYums!*
