# Python-based imports
import csv
import logging
import re

# Django-based imports
from django.core.management.base import BaseCommand

# Internal imports
from yum_yums.models import FoodItem

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Load food data from CSV file into FoodItem model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        # Retrieve the path to the CSV file from command line arguments
        csv_file_path = kwargs['csv_file']
        
        # Variable to track the number of successfully loaded food items
        success_count = 0
        
        try:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                # Create a CSV reader
                csv_reader = csv.DictReader(file)
                
                # Iterate over each row in the CSV file
                for row in csv_reader:
                    print(row)
                    try:
                        # Modify the column names to replace non-ASCII characters
                        row = {re.sub(r'[^\x00-\x7F]+', '', key): value for key, value in row.items()}
                        
                        print(row)
                        # Create a FoodItem object from the CSV data and save it to the database
                        FoodItem.objects.create(
                            S_NO=row['S. No.'],
                            name=row['Name'],
                            short_description=row['Short Description'],
                            image_url=row['Image URL'],
                            type=row['Type'],
                            calories=row['Calories (in Kcal)'],
                            total_fat=row['Total Fat (in g)'],
                            saturated_fat=row['Saturated Fat (in g)'],
                            trans_fat=row['Trans Fat (in g)'],
                            cholesterol=row['Cholesterol (in mg)'],
                            sodium=row['Sodium (in mg)'],
                            carbohydrate=row['Carbohydrate (in g)'],
                            dietary_fiber=row['Dietary Fiber (in g)'],
                            sugar=row['Sugar (in g)'],
                            protein=row['Protein (in g)'],
                            calcium=row['Calcium (in mg)'],
                            iron=row['Iron (in mg)'],
                            potassium=row['Potassium (in mcg)'],
                            vitamin_a=row['Vitamin A (in mcg)'],
                            vitamin_b1=row['Vitamin B1 (in mg)'],
                            vitamin_b2=row['Vitamin B2 (in mg)'],
                            vitamin_b3=row['Vitamin B3 (in mg)'],
                            vitamin_b4=row['Vitamin B4 (in mg)'],
                            vitamin_b5=row['Vitamin B5 (in mg)'],
                            vitamin_b6=row['Vitamin B6 (in mg)'],
                            vitamin_b9=row['Vitamin B9 (in mcg)'],
                            vitamin_b12=row['Vitamin B12 (in mcg)'],
                            vitamin_c=row['Vitamin C (in mg)'],
                            vitamin_d=row['Vitamin D (in mcg)'],
                            vitamin_e=row['Vitamin E (in mg)'],
                            vitamin_k=row['Vitamin K (in mcg)'],
                            phosphorus=row['Phosphorus (in mg)'],
                            magnesium=row['Magnesium (in mg)'],
                            zinc=row['Zinc (in mg)'],
                            copper=row['Copper (in mg)'],
                            recommended_portion=row['Recommended portion (in g)'],
                        )
                        
                        # Increment the success count
                        success_count += 1
                    except Exception as e:
                        # Log any errors that occur during creation of FoodItem objects
                        logger.error(f"Error occurred while creating FoodItem: {e}")
                        continue
        except FileNotFoundError:
            # Log an error if the specified CSV file is not found
            logger.error("File not found. Please provide a valid CSV file path.")
            return

        # Display a success message indicating the number of food items loaded
        self.stdout.write(self.style.SUCCESS(f'{success_count} food items loaded successfully :)'))
