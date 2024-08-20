from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pnumber = models.IntegerField()
    query = models.CharField(max_length=20000)

    def __str__(self):
        return f"{self.name}    -   {self.email}    -   {self.pnumber} "
    
class product(models.Model):
    product_name = models.CharField(max_length=1000)
    Choices =[('Chair Mechanism','Chair Mechanism'),('Arm Rest','Arm Rest'),('Height Adjustment & Legs','Height Adjustment & Legs'),('Fitting & Accessories','Fitting & Accessories'),('Castor & Adjustment','Castor & Adjustment'),('Plastic Net Back','Plastic Net Back'),('AC & Washing machine stand','AC & Washing machine stand'),('Inner outer & Plastic accessories','Inner outer & Plastic accessories'),('Chair Base','Chair Base')]
    product_choice = models.CharField(max_length=400, choices=Choices)
    slug = models.SlugField(max_length=1000,unique=True)
    product_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.product_name}    -   {self.product_choice}"
    
class company_details(models.Model):
    company_name = models.CharField(max_length=200)
    gst = models.IntegerField()
    mobile_number = models.IntegerField()
    email = models.EmailField(max_length=300)


class usb_product(models.Model):
    product_name = models.CharField(max_length=1000)
    Choices =[('Chair Mechanism','Chair Mechanism'),('Arm Rest','Arm Rest'),('Height Adjustment & Legs','Height Adjustment & Legs'),('Fitting & Accessories','Fitting & Accessories'),('Castor & Adjustment','Castor & Adjustment'),('Plastic Net Back','Plastic Net Back'),('AC & Washing machine stand','AC & Washing machine stand'),('Inner outer & Plastic accessories','Inner outer & Plastic accessories'),('Chair Base','Chair Base')]
    product_choice = models.CharField(max_length=400, choices=Choices)
    slug = models.SlugField(max_length=1000,unique=True)
    product_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.product_name}    -   {self.product_choice}"