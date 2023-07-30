# Generated by Django 3.1.13 on 2021-07-31 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('coderedcms', '0021_auto_20210730_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='coderedpage',
            name='canonical_url',
            field=models.URLField(blank=True, help_text="Leave blank to use the page's URL.", max_length=255, verbose_name='Canonical URL'),
        ),
        migrations.AlterField(
            model_name='coderedpage',
            name='og_image',
            field=models.ForeignKey(blank=True, help_text='Shown when linking to this page on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Preview image'),
        ),
        migrations.AlterField(
            model_name='coderedpage',
            name='struct_org_geo_lat',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='Geographic latitude'),
        ),
        migrations.AlterField(
            model_name='coderedpage',
            name='struct_org_geo_lng',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='Geographic longitude'),
        ),
        migrations.DeleteModel(
            name='SeoSettings',
        ),
    ]
