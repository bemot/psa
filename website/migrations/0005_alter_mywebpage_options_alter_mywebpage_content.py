# Generated by Django 4.1.10 on 2023-07-30 15:51

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_mywebpage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mywebpage',
            options={'verbose_name': 'Web Page with video cards'},
        ),
        migrations.AlterField(
            model_name='mywebpage',
            name='content',
            field=wagtail.fields.StreamField([('extended_card', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', max_length=255, required=False)), ('title', wagtail.blocks.CharBlock(label='Title', max_length=255, required=False)), ('subtitle', wagtail.blocks.CharBlock(label='Subtitle', max_length=255, required=False)), ('description', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link'], label='Body')), ('links', wagtail.blocks.StreamBlock([('Links', wagtail.blocks.StructBlock([('settings', wagtail.blocks.StructBlock([('custom_template', wagtail.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.blocks.CharBlock(label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.blocks.CharBlock(label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.blocks.CharBlock(label='Tracking Event Label', max_length=255, required=False))])), ('page_link', wagtail.blocks.PageChooserBlock(label='Page link', required=False)), ('doc_link', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False)), ('other_link', wagtail.blocks.CharBlock(label='Other link', max_length=255, required=False)), ('button_title', wagtail.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-outline-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False))]))], blank=True, label='Links', required=False))]))], use_json_field=True),
        ),
    ]
