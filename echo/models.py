from django.db import models

os_choices=(
  ('oscammand','oscammand'),
  ('mathcocommand','mathcocommand')
)


class OsTyper (models.Model):
  name=models.CharField(choices=os_choices,max_length=50)
  def __str__(self):
    return self.name



class OsCommand(models.Model):
  command_type=models.OneToOneField(OsTyper, on_delete=models.CASCADE,null=False,blank=False)
  command_name=models.CharField(max_length=50)
  paramet = models.ForeignKey('Parameter', on_delete=models.PROTECT ,null=True)

  def __str__(self):
    return self.command_name



class Parameter(models.Model):
  name=models.CharField(max_length=50)
  def __str__(self):
    return f"{self.name}"



class MathCommand(models.Model):
  command_type=models.OneToOneField(OsTyper, on_delete=models.CASCADE , null=False,blank=False)
  expression=models.CharField(max_length=50)

  def __str__(self):
    return self.expression

