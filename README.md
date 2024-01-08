# TestTubeYumYums

TestTubeYumYums is a Django-based application designed to provide custom food recommendations to users based on their blood test results. The application utilizes React and Tailwind (both CDN-based) for the front-end and PostgreSQL for the database.

## Tech Stack

- Django
- React (CDN-based)
- Tailwind (CDN-based)
- PostgreSQL

## Distinctiveness and Complexity

TestTubeYumYums aims to target a unique blend of the health, pharmaceutical, and nutrition sectors by offering users food recommendations based on their blood test reports. The project is distinct in its approach, as it is rare to find applications recommending foods based on nutritional deficiencies using blood test results. The complexity of the project lies in its algorithm, which analyzes blood test reports, extracts deficient nutrients, compares them with the user's exact vitamin and mineral reports, and fetches food recommendations from a local CSV database.

The project also features a multi-page registration form with partial submissions, validated entries, custom error messages, and responsiveness.

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
