from django.db import models
from django.urls import reverse


# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    """아래 메서드는 객체의 상세 화면 주소를 반환하는 기능을 한다.
    reverse 는 url 패턴의 이름과 추가 인자를 전달받아 url 을 생성하는 메서드다."""
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])