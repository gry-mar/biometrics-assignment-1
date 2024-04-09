## Facial Recognition

Projekt realizaowany w ramach kursu Biometria an Politechnice Wrocławskiej. Szczegółowe informacje [tutaj](https://www.syga.ai.pwr.edu.pl/courses/bio/P1.pdf).

# Dane


[LINK](https://drive.google.com/file/d/1RWcZi_GpCUI-EaS9ja3ThF8cDT_MZvee/view?usp=sharing)


Struktura:

```
dataset
├── profiles
│   ├── Name_Surname
│   │   ├── profile
│   │   ├── test_negative
│   │   └── test_positive
│   ├── Name_Surname
│   │   ├── profile
│   │   ├── test_negative
│   │   └── test_positive
|   ...
└── unregistered

```
- 20 aktorów i 20 aktorek w folderze profiles/\[nazwa aktora\]
    - profile - bazowy folder do utworzenia profilu danego aktora/aktorki, 5 obrazków
    - test_positive - folder z 4 obrazkami tego samego aktora/aktorki do testów false-negative
    - test_negative - folder z obrazkami innych aktorów/aktorek tej samej płci co dany aktor do testów false-positive (4 osoby, 1 obrazek na każdą)
- 100 zdjęć przypadkowych osób w folderach unregistered
    - 50 aktorów i 50 aktorek
    - osoby nieobecne w folderach profiles/*
 
Wytyczne stosowane przy selekcji zdjęć - starałem się brać zdjęcia które najlepiej pasowały do wytycznych przy zdjęciach do dokumentów ale nie wszystkie wymagania są zawsze spełnione, mamy zatem ogólne cechy wybranych zdjęć:
- Twarz zwrócona w stronę obiektywu lub delikatnie obrócona, ale z możliwością dostrzeżenia policzka od obiektywu
- Oczy - jak najbardziej patrzą w obiektyw
- Twarz odsłonięta - brwi, oczy, nos, policzki, kości policzkowe, usta, podbródek - brak obiektów zasłaniających poza włosami
- Oświetlenie - jak najbardziej naturalne, brak świecenia/przyciemnienia/światłocienia
- Kolorystyka - jak najbardziej naturalna, bez klisz, czarno-białych lub artystycznych
- Wyraz twarzy - jak najbliższy do neutralnego, ewentualnie uśmiech (uniesienie kącików ust i/lub pokazanie zębów), bez śmiechu i bardziej złożonych min
- Rozmiar obrazu i twarzy - min 256px w każdym wymiarze i twarz jak największa
- Jakość zdjęcia - zdjęcie ostre i wyraźne
