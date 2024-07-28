# Generated by Django 5.0 on 2024-07-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_product_category_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quantiy',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('MS', 'Milkshake'), ('CZ', 'Cheese'), ('IC', 'Ice-cream'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('BT', 'Butter'), ('ML', 'Milk')], max_length=2),
        ),
    ]