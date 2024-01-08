'''
This file contains function responsible responsible for populating first two rows of CBC model and VitMin model
when the migrations are made for the very first time. This helps in ensuring that the lower and upper ranges
for each parameter are already available when a user starts interacting with the application after initial migration.

It utilizes Django's in-built signals to check if the migrated models are empty.
'''

# Django-based imports
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Internal imports
from TestTubeYumYums.models import CBC, VitMin

# Whenever a model is migrated, trigger this function through Django's in-built signal
@receiver(post_migrate)
def populate_ranges(sender, **kwargs):
    print("Post migrate signal received.")

    # Check whether the migration that triggered the function was for this app(TestTubeYumYums)'s model
    if sender.name == 'TestTubeYumYums':
        print("App name matches.")
        
        # Check if the CBC table is migrated for the first time
        if CBC.objects.count() == 0:
            print("CBC table is empty. Populating initial data.")
            # Create lower range for CBC
            CBC.objects.create(
                Hb=12.0,
                PCV=36.0,
                RBC_count=3.80,
                MCV=83.0,
                MCH=27.0,
                MCHC=31.5,
                RDW=11.6,
                TLC=4.0,
                DLC_N=40.0,
                DLC_L=20.0,
                DLC_M=2.0,
                DLC_E=1.0,
                DLC_B=0.01,
                ALC_N=2.0,
                ALC_L=1.0,
                ALC_M=0.2,
                ALC_E=0.02,
                ALC_B=0.02,
                Platelets=150.0,
                MPV=6.5
            )

            # Create upper arange for CBC
            CBC.objects.create(
                Hb=15.0,
                PCV=46.0,
                RBC_count=4.80,
                MCV=101.0,
                MCH=32.0,
                MCHC=34.5,
                RDW=14.0,
                TLC=10.0,
                DLC_N=80.0,
                DLC_L=40.0,
                DLC_M=10.0,
                DLC_E=6.0,
                DLC_B=2.0,
                ALC_N=7.0,
                ALC_L=3.0,
                ALC_M=1.0,
                ALC_E=0.5,
                ALC_B=0.1,
                Platelets=410.0,
                MPV=12.0
            )

        # Check if the VitMin table is migrated for the first time
        if VitMin.objects.count() == 0:
            print("VitMin table is empty. Populating initial data.")
            # Create lower range for VitMin
            VitMin.objects.create(
                A=300.0,
                B1=0.5,
                B2=1.6,
                B3=0.3,
                B5=11.0,
                B6=5.0,
                B7=0.2,
                B9=0.2,
                B12=211.0,
                C=0.6,
                D=30.0,
                E=5500.0,
                K=0.130,
                Ca=9.0,
                P=2.8,
                Mg=1.7,
                Zn=70.0
            )

            # Create upper arange for VitMin
            VitMin.objects.create(
                A=800.0,
                B1=4.0,
                B2=68.2,
                B3=9.8,
                B5=150.0,
                B6=50.0,
                B7=3.0,
                B9=20.0,
                B12=911.0,
                C=2.0,
                D=100.0,
                E=18000.0,
                K=1.190,
                Ca=11.0,
                P=4.5,
                Mg=2.2,
                Zn=120.0
            )
