'''
Note: Every time the word range is used, it denotes safe range for each blood test parameter.
As the ranges vary depending on your pathology, functionality to alter them for each user is provided infinite times.
'''


'''
List of units used for storing the parameters of the following models:

USER
- weight:       Kilograms(kg)
- height:       Centimetres(cm)
- systolic:     Millemetres(mm) of Mercury(Hg)
- diastolic:    Millemetres(mm) of Mercury(Hg)


Common Blood Test (CBC)
- Haemoglobin (Hb):                                     Grams Per Deciliter (g/dL)
- Packed Cell Volume (PCV):                             Percentage of blood made up of cells (%)
- Erythrocyte Count (RBC_Count):                        Millions per cubic millimeter (mil/mm³)
- Mean Corpuscular Volume (MCV):                        Femtoliters (fL)
- Mean Corpuscular Hemoglobin (MCH):                    Picograms (pg)
- Mean Corpuscular Hemoglobin Concentration (MCHC):     Grams Per Deciliter (g/dL)
- Red Cell Distribution Width (RDW):                    Percentage (%)
- Total Leukocyte Count (TLC):                          Thousands per cubic millimeter (thou/mm³)
- Differential Neutrophils Count (DLC_N):               Percentage (%)
- Differential Lymphocytes Count (DLC_L):               Percentage (%)
- Differential Monocytes Count (DLC_M):                 Percentage (%)
- Differential Eosinophils Count (DLC_E):               Percentage (%)
- Differential Basophils Count (DLC_B):                 Percentage (%)
- Absolute Neutrophils Count (ALC_N):                   Thousands per cubic millimeter (thou/mm³)
- Absolute Lymphocytes Count (ALC_L):                   Thousands per cubic millimeter (thou/mm³)
- Absolute Monocytes Count (ALC_M):                     Thousands per cubic millimeter (thou/mm³)
- Absolute Eosinophils Count (ALC_E):                   Thousands per cubic millimeter (thou/mm³)
- Absolute Basophils Count (ALC_B):                     Thousands per cubic millimeter (thou/mm³)
- Platelets:                                            Thousands per cubic millimeter (thou/mm³)
- Mean Platelet Volume (MPV):                           Femtoliters (fL)


Vitamin and Minerals (VITMIN)
- Vitamin A:                        Nanograms per milliliter (ng/mL)
- Vitamin B1 (Thiamin):             Nanograms per milliliter (ng/mL)
- Vitamin B2 (Riboflavin):          Nanograms per milliliter (ng/mL)
- Vitamin B3 (Nicotinic Acid):      Nanograms per milliliter (ng/mL)
- Vitamin B5 (Pantothenic):         Nanograms per milliliter (ng/mL)
- Vitamin B6 (P5P):                 Nanograms per milliliter (ng/mL)
- Vitamin B7 (Biotin):              Nanograms per milliliter (ng/mL)
- Vitamin B9 (Folic Acid):          Nanograms per milliliter (ng/mL)
- Vitamin B12:                      Nanograms per milliliter (ng/mL)
- Vitamin C:                        Nanograms per milliliter (ng/mL)
- Vitamin D:                        Nanograms per milliliter (ng/mL)
- Vitamin E:                        Nanograms per milliliter (ng/mL)
- Vitamin K:                        Nanograms per milliliter (ng/mL)

- Calcium (Ca):         Milligrams per deciliter (mg/dL)
- Phosphorus (P):       Milligrams per deciliter (mg/dL)
- Magnesium (Mg):       Milligrams per deciliter (mg/dL)
- Zinc (Zn):            Micrograms per deciliter (mcg/dL)
'''

# Django-based Imports
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_countries.fields import CountryField
from django.db import models


# AUTHENTICATION MODELS

class CustomUserManager(BaseUserManager):
    '''
    Portrays functionality of Django's in-built UserManager class but 
    making email, password, first_name and date of birth mandatory for every user.
    '''

    def create_user(self, email, password, first_name, dob):
        '''
        Modified in-built method of Django to create a user 
        with mandatory email, password, first_name and date of birth.
        '''
        if not email:
            raise ValueError('Users must have an email address')
        
        if not password:
            raise ValueError('Users must have a password')
        
        if not first_name:
            raise ValueError('Users must have a first name')
        
        if not dob:
            raise ValueError('Users must have a date of birth')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            dob=dob
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password, first_name, dob):
        '''
        Modified in-built method of Django to create a superuseruser 
        with mandatory email, password, first_name and date of birth.
        '''
        user = self.create_user(
            email,
            password, 
            first_name,
            dob
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        Range.objects.create(user=user)
        return user


class User(AbstractUser):
    '''
    Django's in-built User model extended to contain (optional) personal info 
    of every user, later handy in providing customised food recommendations.
    '''
    username = None
    email = models.EmailField(unique=True)
    dob = models.DateField()
    country = CountryField(blank=True)
    diabetes = models.BooleanField(blank=False, null=True)
    bp = models.BooleanField(blank=False, null=True)

    # When creating superUser, UserManager is called. It is now incompatible since we removed username field.
    # Create custom UserManager
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'dob']

# Fields holding primary data are similar in nature and can be efficiently added through loop
user_fields = ['weight', 'height', 'bmi', 'ast', 'systolic', 'diastolic']
for field in user_fields:
    User.add_to_class(field, models.DecimalField(blank=False, null=True, decimal_places=3, max_digits=6))



# LABTEST DATA MODELS
    
class CBC(models.Model):
    '''
    Responsible for storing CBC test values and CBC ranges corresponding to every user. \n\n

    get_low(): Designated function to return default lower range value for every CBC parameter. \n
    get_high(): Designated function to return default upper range value for every CBC parameter. \n\n\n

    NOTE: DO NOT alter values for pk=1 and pk=2 in this model as they hold default lower and upper ranges for every user.
    '''
    @classmethod
    def get_low(cls):
        return cls.objects.get(pk=1).pk
    
    @classmethod
    def get_high(cls):
        return cls.objects.get(pk=2).pk

# Fields holding labtest data are similar in nature for every parameter and can be efficiently added through loop
cbc_fields = ['Hb', 'PCV', 'RBC_count', 'MCV', 'MCH', 'MCHC', 'RDW', 'TLC', 'DLC_N', 'DLC_L', 'DLC_M', 'DLC_E', 'DLC_B', 'ALC_N', 'ALC_L', 'ALC_M', 'ALC_E', 'ALC_B', 'Platelets', 'MPV']
for field in cbc_fields:
    CBC.add_to_class(field, models.DecimalField(blank=False, null=True, decimal_places=3, max_digits=6))


class VitMin(models.Model):
    '''
    Responsible for storing Vitamin and Mineral test values and ranges corresponding to every user. \n\n

    get_low(): Designated function to return default lower range value for every Vitamin and Mineral parameter. \n
    get_high(): Designated function to return default upper range value for every Vitamin and Mineral parameter. \n
    
    NOTE: DO NOT alter values for pk=1 and pk=2 in this model as they hold default lower and upper ranges for every user.
    '''
    @classmethod
    def get_low(cls):
        return cls.objects.get(pk=1).pk
    
    @classmethod
    def get_high(cls):
        return cls.objects.get(pk=2).pk

# Fields holding labtest data are similar in nature for every parameter and can be efficiently added through loop
vitmin_fields = ['A', 'B1', 'B2', 'B3', 'B5', 'B6', 'B7', 'B9', 'B12', 'C', 'D', 'E', 'K', 'Ca', 'P', 'Mg', 'Zn']
for field in vitmin_fields:
    VitMin.add_to_class(field, models.DecimalField(blank=False, null=True, decimal_places=3, max_digits=8))



# USER-LABTEST DATA relational models

class Range(models.Model):
    '''
    Model responsible for holding relation between custom ranges of every user. By default it holds default app-wide ranges.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    cbc_upper = models.ForeignKey(CBC, on_delete=models.SET_DEFAULT, related_name='cbc_upper', default=CBC.get_high)
    cbc_lower = models.ForeignKey(CBC, on_delete=models.SET_DEFAULT, related_name='cbc_lower', default=CBC.get_low)
    vitmin_upper = models.ForeignKey(VitMin, on_delete=models.SET_DEFAULT, related_name='vitmin_upper', default=VitMin.get_high)
    vitmin_lower = models.ForeignKey(VitMin, on_delete=models.SET_DEFAULT, related_name='vitmin_lower', default=VitMin.get_low)


class CBCStat(models.Model):
    '''
    Model storing relation of every CBC test result with it's patient(user), and range related to user when that individual test was registered.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cbc_patient')
    cbc = models.ForeignKey(CBC, on_delete=models.CASCADE, related_name='cbcc_report', blank=False, null=True)
    upper_range = models.ForeignKey(CBC, on_delete=models.RESTRICT, related_name='cbc_upper_range')
    lower_range = models.ForeignKey(CBC, on_delete=models.RESTRICT, related_name='cbc_lower_range')

    def save(self, *args, **kwargs):
        '''
        Everytime a new test result is registered, current range of user (already updated if simultaneously entered) is associated with it.
        '''
        if not self.pk:
            try:
                range = Range.objects.get(user=self.user)
                self.upper_range = range.cbc_upper
                self.lower_range = range.cbc_lower
            except:
                self.upper_range = CBC.get_high()
                self.lower_range = CBC.get_low()

        super().save(*args, **kwargs)


class VitMinStat(models.Model):
    '''
    Model storing relation of every Vitamin and Minerals test result with it's patient(user), and range related to user when that individual test was registered.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vitmin_patient')
    vitmin = models.ForeignKey(VitMin, on_delete=models.CASCADE, related_name='vitmin_report', blank=False, null=True)
    upper_range = models.ForeignKey(VitMin, on_delete=models.RESTRICT, related_name='vitmin_upper_range')
    lower_range = models.ForeignKey(VitMin, on_delete=models.RESTRICT, related_name='vitmin_lower_range')

    def save(self, *args, **kwargs):
        '''
        Everytime a new test result is registered, current range of user (already updated if simultaneously entered) is associated with it.
        '''
        if not self.pk:
            try:
                range = Range.objects.get(user=self.user)
                self.upper_range = range.vitmin_upper
                self.lower_range = range.vitmin_lower
            except:
                self.upper_range = VitMin.get_high()
                self.lower_range = VitMin.get_low()

        super().save(*args, **kwargs)