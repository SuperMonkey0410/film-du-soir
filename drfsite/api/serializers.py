from rest_framework import serializers
from cinema.models import Director, Film, Genre, Grades, Awards, Nomination

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ['title', 'marks']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title',)

class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True,)
    grade = GradesSerializer(many=True,)
    director = serializers.StringRelatedField()  # Добавляем это поле для отображения имени режиссера вместо id :)


    class Meta:
        model = Film
        fields = "__all__"

    def create(self, validated_data):
        return Film.objects.create(**validated_data)


class DirectorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    films = FilmSerializer(many=True, read_only=True)
    best_films = FilmSerializer(many=True, read_only=True)
    class Meta:
        model = Director
        fields = ('name', 'birthday', 'films', 'best_films', 'user')




    # def save(self, validated_data):
    #     return Director.objects.create(**validated_data)