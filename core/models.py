from django.db import models

class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    edv = models.IntegerField()
    city = models.CharField(max_length=30, null=True, blank=True)
    treatment_name = models.CharField(max_length=20, blank=True)
    photo = models.BinaryField(editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        # if not self.pk:
        #     super().save(*args, **kwargs)
        # else:
        # original = Collaborator.objects.get(pk=self.pk)
        # if not self.city:
        #     self.city = original.city
        
        if not self.treatment_name:
            self.treatment_name = self.name.split()[0]
        
        super().save(*args, **kwargs)
