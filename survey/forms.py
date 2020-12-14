from django import forms

class UserDataForm(forms.Form):
    varsta= forms.DecimalField()
    
    optiuni = ( ( "F" , "F"), ("M", "M"))
    gen=forms.ChoiceField(widget=forms.RadioSelect,choices=optiuni)
    
    optiuni= (( "Navigant", "Navigant"), ("Nenavigant", "Nenavigant"))
    tip_personal=forms.ChoiceField(widget=forms.RadioSelect,choices=optiuni)
    
    grad_militar=forms.CharField()
    durata_functie_ani=forms.DecimalField()
    durata_functie_luni=forms.DecimalField()
    durata_unitate_ani=forms.DecimalField()
    durata_unitate_luni=forms.DecimalField()
    ore_pe_zi=forms.DecimalField()
    
    optiuni= (( "Da", "Da"), ("Nu", "Nu"))
    ture=forms.ChoiceField(widget=forms.RadioSelect,choices=optiuni)
    program_ture=forms.CharField(required=False)

    def clean_varsta(self, *args, **kwargs):
        varsta=self.cleaned_data.get("varsta")
        if (varsta < 18 ):
            raise forms.ValidationError("Introduceti o valore valida !")
        return varsta

    def clean_durata_functie_ani(self, *args, **kwargs):
        durata_functie_ani=self.cleaned_data.get("durata_functie_ani")
        if (durata_functie_ani <0):
            raise forms.ValidationError("Introduceti un numar de ani valid !")
        return durata_functie_ani

    def clean_durata_functie_luni(self, *args, **kwargs):
        durata_functie_luni=self.cleaned_data.get("durata_functie_luni")
        if (durata_functie_luni <0 or durata_functie_luni > 11):
            raise forms.ValidationError("Introduceti un numar de luni valid !")
        return durata_functie_luni

    def clean_durarata_unitate_ani(self, *args, **kwargs):
        durata_unitate_ani= self.cleaned_data.get("durata_unitate_ani")
        if (durata_unitate_ani < 0):
            raise forms.ValidationError("Introduceti un numar de ani valid !")
        return durarata_unitate_ani

    def clean_durata_unitate_luni(self, *args, **kwargs):
        durata_unitate_luni=self.cleaned_data.get("durata_unitate_luni")
        if (durata_unitate_luni <0 or durata_unitate_luni > 11):
            raise forms.ValidationError("Introduceti un numar valid de luni !")
        return durata_unitate_luni
    def clean_ore_pe_zi(self, *args, **kwargs):
        ore_pe_zi=self.cleaned_data.get("ore_pe_zi")
        if (ore_pe_zi < 0 or ore_pe_zi >24):
            raise forms.ValidationError("Introduceti un numar valid de ore !")
        return ore_pe_zi
        

class UserCodeForm(forms.Form):
    litera_oras=forms.CharField(max_length=1)
    litera_judet=forms.CharField(max_length=1)
    suma_cifre_an_nastere=forms.DecimalField(max_digits=2)
    suma_cifre_zi_luna=forms.DecimalField(max_digits=2)

    def clean_litera_oras(self, *args, **kwargs):
        litera_oras=self.cleaned_data.get("litera_oras")
        print(litera_oras)
        if not litera_oras.isalpha():
            raise forms.ValidationError("Introduceti o litera!")
        return litera_oras

    def clean_litera_judet(self, *args, **kwargs):
        litera_judet=self.cleaned_data.get("litera_judet")
        if not litera_judet.isalpha():
            raise forms.ValidationError("Introduceti o litera!")
        return litera_judet

    def clean_suma_cifre_an_nastere(self, *args, **kwargs):
        suma_cifre_an_nastere=self.cleaned_data.get("suma_cifre_an_nastere")
        print(suma_cifre_an_nastere)
        if (suma_cifre_an_nastere<0 or suma_cifre_an_nastere > 18):
            raise forms.ValidationError("Numarul introdus nu este valid.")
        return suma_cifre_an_nastere

    def clean_suma_cifre_zi_luna(self, *args, **kwargs):
        suma_cifre_zi_luna=self.cleaned_data.get("suma_cifre_zi_luna")
        if (suma_cifre_zi_luna < 0 or suma_cifre_zi_luna > 43):
            raise forms.ValidationError("Numarul introdus nu este valid.")
        return suma_cifre_zi_luna


