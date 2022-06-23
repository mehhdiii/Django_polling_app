from django.db import models


class Question(models.Model): 
    question_text = models.CharField('question text', max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    #In case of deletion of question, deletes the entry here too: 
    question = models.ForeignKey(Question ,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)



    
