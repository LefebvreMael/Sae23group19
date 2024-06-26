from django import forms
from .models import Categorie, Film, Acteur, Personne, Commentaire

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class ActeurForm(forms.ModelForm):
    films = forms.ModelMultipleChoiceField(
        queryset=Film.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Films"
    )

    class Meta:
        model = Acteur
        fields = ['prenom', 'nom', 'age', 'photo', 'films']

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = '__all__'

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = '__all__'
