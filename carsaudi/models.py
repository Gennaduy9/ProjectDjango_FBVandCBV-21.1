from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    color = models.CharField(max_length=50, **NULLABLE, verbose_name='Цвет')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, **NULLABLE, verbose_name='Категория')
    available = models.BooleanField(default=True, verbose_name='Наличие')



    @property
    def audi_description(self) -> str:
        return self.description[:400]

    def __str__(self):
        return f'{self.name} ({self.category}) - {self.price} руб.'



    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


