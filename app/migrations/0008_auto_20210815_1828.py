# Generated by Django 3.2.5 on 2021-08-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_professional_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professional',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='College',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='Currently_or_was_working_for',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='Fifth_Experience',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='First_Experience',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='Fourth_Experience',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='School',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='Second_Experience',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='Seventh_Skill',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='Sixth_Skill',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='Third_Experience',
        ),
        migrations.AddField(
            model_name='professional',
            name='Board',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='City',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='College_Duration',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='College_Location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='College_Name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Company_Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fifth_Experience_Company_Duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fifth_Experience_Company_Location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fifth_Experience_Company_Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fifth_Experience_Job_Title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fifth_Skill_category',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='First_Experience_Company_Duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='First_Experience_Company_Location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='First_Experience_Company_Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='First_Experience_Job_Title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='First_Skill_category',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fourth_Experience_Company_Duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fourth_Experience_Company_Location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fourth_Experience_Company_Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fourth_Experience_Job_Title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fourth_Language',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Fourth_Skill_category',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Job_Title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Locaton',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Regional_place',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='School_Duration',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='School_Location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='School_Name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Second_Experience_Company_Duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Second_Experience_Company_Location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Second_Experience_Company_Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Second_Experience_Job_Title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Second_Skill_category',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Specialization',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='State',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Third_Experience_Company_Duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Third_Experience_Company_Location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Third_Experience_Company_Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Third_Experience_Job_Title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='Third_Skill_category',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fifth_Skill',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='First_Skill',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fist_Language',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fourth_Skill',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Language',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Skill',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Language',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Skill',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
