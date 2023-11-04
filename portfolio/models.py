from django.db import models

SOCIAL_CHOICES = (

    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("tiktok", "Tiktok"),
    ("telegram", "Telegram"),
    ("linkedin", "linkedin"),
    ("github", "GitHub"),

)

class About(models.Model):
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Ad")
    surname = models.CharField(max_length=255, verbose_name="Soyad")
    location = models.CharField(max_length=255, verbose_name="Ünvan")
    phone_number = models.CharField(max_length=255, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email")
    description = models.TextField(verbose_name="Məlumat")

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", )
        verbose_name = "About"
        verbose_name_plural = "About"


class Experience(models.Model):
    position = models.CharField(max_length=255, verbose_name="Pozisiya")
    date_interval = models.CharField(max_length=255, verbose_name="Tarix")
    company_name = models.CharField(max_length=255, verbose_name="Şirkət adı")
    info = models.TextField(verbose_name="Məlumat")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Iş təcrübəsi"
        verbose_name_plural = "Iş təcrübəsi"


class Education(models.Model):
    school_name = models.CharField(max_length=255, verbose_name="Adı")
    degree = models.CharField(max_length=255, verbose_name="Dərəcə")
    date_interval = models.CharField(max_length=255, verbose_name="Tarix")
    profession = models.CharField(max_length=255, verbose_name="Ixtisas")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Təhsil"
        verbose_name_plural = "Təhsil"


class Awards(models.Model):
    name = models.CharField(max_length=255, verbose_name="Adı")
    date = models.CharField(max_length=255, verbose_name="Tarix")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    active = models.BooleanField(default=False)


class Interest(models.Model):
    description = models.TextField(verbose_name="Məlumat")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Maraq"
        verbose_name_plural = "Maraq"


class SocialMedia(models.Model):
    social_media = models.CharField(max_length=255, choices=SOCIAL_CHOICES, verbose_name="Sosial media")
    social_link = models.TextField(verbose_name="Link")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.social_media

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Sosial media"
        verbose_name_plural = "Sosial media hesabları"



class Skills(models.Model):
    image = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=255, verbose_name="Bacarıq")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Bacarıq"
        verbose_name_plural = "Bacarıqlar"

class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ad")
    image = models.ImageField(upload_to="media/")
    link = models.TextField(verbose_name="Link", null=True, blank=True)
    info = models.TextField(verbose_name="Məlumat")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Proyekt"
        verbose_name_plural = "Proyektlər"

