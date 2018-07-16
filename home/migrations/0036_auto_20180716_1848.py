# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 18:48
from __future__ import unicode_literals

from django.db import migrations
import home.models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20180518_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', home.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('one_column', wagtail.core.blocks.StructBlock([('back_image', wagtail.images.blocks.ImageChooserBlock(blank=True)), ('background_size', wagtail.core.blocks.ChoiceBlock(choices=[('auto', 'Auto'), ('cover', 'Cover'), ('50%', 'Small'), ('200%', 'Large')])), ('background_x_position', wagtail.core.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('background_y_position', wagtail.core.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Centre')])), ('one_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock())], icon='arrow-left', label='Parallax content'))])), ('two_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Right column content'))])), ('three_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-left', label='Left column content')), ('center_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Center column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', home.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('one_column', wagtail.core.blocks.StructBlock([('back_image', wagtail.images.blocks.ImageChooserBlock(blank=True)), ('background_size', wagtail.core.blocks.ChoiceBlock(choices=[('auto', 'Auto'), ('cover', 'Cover'), ('50%', 'Small'), ('200%', 'Large')])), ('background_x_position', wagtail.core.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('background_y_position', wagtail.core.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Centre')])), ('one_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock())], icon='arrow-left', label='Parallax content'))])), ('two_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Right column content'))])), ('three_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-left', label='Left column content')), ('center_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Center column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())]),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', home.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('one_column', wagtail.core.blocks.StructBlock([('back_image', wagtail.images.blocks.ImageChooserBlock(blank=True)), ('background_size', wagtail.core.blocks.ChoiceBlock(choices=[('auto', 'Auto'), ('cover', 'Cover'), ('50%', 'Small'), ('200%', 'Large')])), ('background_x_position', wagtail.core.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('background_y_position', wagtail.core.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Centre')])), ('one_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock())], icon='arrow-left', label='Parallax content'))])), ('two_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Right column content'))])), ('three_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-left', label='Left column content')), ('center_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Center column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))]))], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('google_map', wagtail.core.blocks.StructBlock([('map_long', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.core.blocks.CharBlock(default=14, max_length=3, required=True))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())]),
        ),
    ]
