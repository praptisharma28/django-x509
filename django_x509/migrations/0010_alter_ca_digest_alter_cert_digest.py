# Generated by Django 4.2.13 on 2024-05-21 18:07

from django.db import migrations, models
import django_x509.base.models


class Migration(migrations.Migration):

    dependencies = [
        ("django_x509", "0009_alter_ca_digest_alter_ca_key_length_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ca",
            name="digest",
            field=models.CharField(
                choices=[
                    ("sha1", "SHA1"),
                    ("sha224", "SHA224"),
                    ("sha256", "SHA256"),
                    ("sha384", "SHA384"),
                    ("sha512", "SHA512"),
                    ("ecdsa-with-sha1", "ECDSA with SHA1"),
                    ("ecdsa-with-sha256", "ECDSA with SHA256"),
                    ("ecdsa-with-sha384", "ECDSA with SHA384"),
                    ("ecdsa-with-sha512", "ECDSA with SHA512"),
                    ("dsaWithSHA1", "DSA with SHA1"),
                    ("dsaWithSHA256", "DSA with SHA256"),
                    ("ed25519", "Ed25519"),
                    ("ed448", "Ed448"),
                ],
                default=django_x509.base.models.default_digest_algorithm,
                help_text="bits",
                max_length=20,
                verbose_name="digest algorithm",
            ),
        ),
        migrations.AlterField(
            model_name="cert",
            name="digest",
            field=models.CharField(
                choices=[
                    ("sha1", "SHA1"),
                    ("sha224", "SHA224"),
                    ("sha256", "SHA256"),
                    ("sha384", "SHA384"),
                    ("sha512", "SHA512"),
                    ("ecdsa-with-sha1", "ECDSA with SHA1"),
                    ("ecdsa-with-sha256", "ECDSA with SHA256"),
                    ("ecdsa-with-sha384", "ECDSA with SHA384"),
                    ("ecdsa-with-sha512", "ECDSA with SHA512"),
                    ("dsaWithSHA1", "DSA with SHA1"),
                    ("dsaWithSHA256", "DSA with SHA256"),
                    ("ed25519", "Ed25519"),
                    ("ed448", "Ed448"),
                ],
                default=django_x509.base.models.default_digest_algorithm,
                help_text="bits",
                max_length=20,
                verbose_name="digest algorithm",
            ),
        ),
    ]
