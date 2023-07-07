# Generated by Django 4.0.1 on 2023-06-29 15:46

from django.db import models, migrations

def load_horizon(apps, schema_editor):
    Spirit = apps.get_model("pbf", "Spirit")
    Card = apps.get_model("pbf", "Card")
    teeth = Spirit(name="Teeth")
    teeth.save()
    Card(name="Ferocious Rampage", cost=2, type=2, spirit=teeth, elements="Fire,Animal").save()
    Card(name="Gift of Furious Might", cost=1, type=2, spirit=teeth, elements="Moon,Fire,Animal").save()
    Card(name="Herd Towards the Lurking Maw", cost=1, type=2, spirit=teeth, elements="Water,Earth,Animal").save()
    Card(name="Mark Territory with Scars and Teeth", cost=2, type=2, spirit=teeth, elements="Sun,Earth,Animal").save()
    eyes = Spirit(name="Eyes")
    eyes.save()
    Card(name="Boon of Watchful Guarding", cost=0, type=2, spirit=eyes, elements="Earth,Plant,Animal").save()
    Card(name="Eerie Noises and Moving Trees", cost=2, type=2, spirit=eyes, elements="Moon,Air,Plant").save()
    Card(name="Mysterious Abductions", cost=1, type=2, spirit=eyes, elements="Moon,Fire,Plant").save()
    Card(name="Whispered Guidance Through the Night", cost=0, type=2, spirit=eyes, elements="Moon,Air,Plant").save()
    mud = Spirit(name="Mud")
    mud.save()
    Card(name="Exaltation of Tangled Growth", cost=0, type=2, spirit=mud, elements="Water,Earth,Plant").save()
    Card(name="Foul Vapors and Fetid Muck", cost=0, type=2, spirit=mud, elements="Fire,Air,Water,Earth").save()
    Card(name="Intractable Thickets and Thorns", cost=2, type=2, spirit=mud, elements="Moon,Water,Earth,Plant").save()
    Card(name="Open Shifting Waterways", cost=1, type=2, spirit=mud, elements="Moon,Water,Animal").save()
    heat = Spirit(name="Heat")
    heat.save()
    Card(name="Call on Herders for Aid", cost=1, type=2, spirit=heat, elements="Sun,Fire,Earth,Animal").save()
    Card(name="Gift of Searing Heat", cost=0, type=2, spirit=heat, elements="Sun,Fire,Air").save()
    Card(name="Stinging Sandstorm", cost=1, type=2, spirit=heat, elements="Fire,Air,Earth").save()
    Card(name="Sweltering Exhaustion", cost=2, type=2, spirit=heat, elements="Fire,Air").save()
    whirlwind = Spirit(name="Whirlwind")
    whirlwind.save()
    Card(name="Gift of the Sunlit Air", cost=0, type=2, spirit=whirlwind, elements="Sun,Fire,Air").save()
    Card(name="Gift of Wind-Sped Steps", cost=1, type=2, spirit=whirlwind, elements="Sun,Air,Animal").save()
    Card(name="Scatter to the Winds", cost=1, type=2, spirit=whirlwind, elements="Fire,Air,Water").save()
    Card(name="Tempest of Leaves and Branches", cost=2, type=2, spirit=whirlwind, elements="Sun,Air,Plant").save()

def delete_horizon(apps, schema_editor):
    Spirit = apps.get_model("pbf", "Spirit")
    Card = apps.get_model("pbf", "Card")
    Card.objects.filter(spirit=Spirit.objects.get(name="Teeth")).delete()
    Spirit.objects.get(name="Teeth").delete()
    Card.objects.filter(spirit=Spirit.objects.get(name="Eyes")).delete()
    Spirit.objects.get(name="Eyes").delete()
    Card.objects.filter(spirit=Spirit.objects.get(name="Mud")).delete()
    Spirit.objects.get(name="Mud").delete()
    Card.objects.filter(spirit=Spirit.objects.get(name="Heat")).delete()
    Spirit.objects.get(name="Heat").delete()
    Card.objects.filter(spirit=Spirit.objects.get(name="Whirlwind")).delete()
    Spirit.objects.get(name="Whirlwind").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('pbf', '0021_alter_game_discord_channel'),
    ]

    operations = [
        migrations.RunPython(load_horizon, delete_horizon),
    ]
