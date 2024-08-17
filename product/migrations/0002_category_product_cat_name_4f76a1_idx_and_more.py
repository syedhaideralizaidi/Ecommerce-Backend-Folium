# Generated by Django 5.1 on 2024-08-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='product_cat_name_4f76a1_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['parent'], name='product_cat_parent__b54811_idx'),
        ),
        migrations.AddIndex(
            model_name='productrecommendation',
            index=models.Index(fields=['product'], name='product_pro_product_257f8c_idx'),
        ),
        migrations.AddIndex(
            model_name='productrecommendation',
            index=models.Index(fields=['recommended_product'], name='product_pro_recomme_ffe804_idx'),
        ),
    ]
