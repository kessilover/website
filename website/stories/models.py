from django.db import models

class Story(models.Model):
    status_choice = (
        ('complete', 'Complete'),
        ('ongoing', 'Ongoing')
    )
    title = models.CharField(max_length=200, null=False)
    summary = models.CharField(max_length=250, null=False)
    status = models.CharField(max_length=20,null=False, choices=status_choice,default='ongoing')
    chapter = models.IntegerField(null=False, )
    link = models.URLField(max_length=200, null=False)
    fandom = models.CharField(max_length=20, null=False)


    def __str__(self):
        return (self.title  )

