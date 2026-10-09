from rest_framework import serializers
from .models import Check, Book


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = "__all__"

    def validate_money(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Баланс не может быть отрицательным."
            )
        return value

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Название книги не может быть пустым."
            )
        return value

    def validate_author(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Имя автора не может быть пустым."
            )
        return value