from django.db import models

#�����ϴ�������Ĵ���·��
def ana_version_path(instance, filename):
    return 'analysis/{0}/{1}/{2}'.format(instance.ana, instance.version, filename)

class Files(models.Model):
    ana = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    pFile = models.FileField(upload_to=ana_version_path)
