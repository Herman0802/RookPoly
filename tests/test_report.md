Herman Lazarchyk, Maksim Zdobnikau

# Kompleksowy Raport z Testów Jednostkowych Projektu RookPoly

## Kontekst Projektu i Baza Matematyczna
- **Nazwa Projektu**: RookPoly
- **Obszar Tematyczny**: Matematyka Dyskretna - Wielomian Szachowy
- **Źródło Matematyczne**: [Wikipedia: Rook Polynomial](https://en.wikipedia.org/wiki/Rook_polynomial)
- **Opis Projektu**: Projekt RookPoly skupia się na implementacji i analizie wielomianu szachowego. Składa się z dwóch głównych komponentów: klasy `Board`, która odpowiada za reprezentację i manipulację stanem planszy, oraz klasy `Polynomial`, która umożliwia wykonywanie operacji matematycznych na wielomianach.

## Cele Testowania
### Klasa `Board`
- **Cel**: Zapewnienie, że klasa `Board` dokładnie obsługuje operacje na planszy, co jest kluczowe dla obliczeń wielomianu szachowego.
- **Ważność**: Dokładność każdej operacji w klasie `Board` jest krytyczna dla matematycznej wiarygodności wyników wielomianu szachowego.

### Klasa `Polynomial`
- **Cel**: Zapewnienie, że klasa `Polynomial` poprawnie wykonuje operacje matematyczne na wielomianach.
- **Ważność**: Dokładność i poprawność matematyczna operacji klasy `Polynomial` są niezbędne do wiarygodnych obliczeń matematycznych.

## Proces Testowania
### Metoda Testowania
- **Testowanie Jednostkowe**: Wykorzystano `unittest` w Pythonie do testowania funkcji obu klas.
- **Weryfikacja Matematyczna**: Kontrola zgodności operacji obu klas z matematycznymi założeniami wielomianu szachowego.

### Metryki Wykorzystane w Procesie Testowym
- **Przypadki Testowe**: Liczba i różnorodność testów, mierząca kompleksowość testów dla obu klas.
- **Wyniki Testów**: Ilość testów zakończonych pozytywnie i negatywnie, wskazująca na jakość kodu i skuteczność testowania.
- **Poprawność Matematyczna**: Ocena zgodności operacji obydwu klas z matematycznymi założeniami wielomianu szachowego, w tym dokładność obliczeń.

## Zrealizowane Testy
### Klasa `Board`

| Nazwa Testu                | Opis                                                | Wynik    |
|----------------------------|-----------------------------------------------------|----------|
| test_init                  | Prawidłowa inicjalizacja planszy                    | PASS ✅   |
| test_n                     | Właściwość `n` (liczba wierszy)                     | PASS ✅   |
| test_m                     | Właściwość `m` (liczba kolumn)                      | PASS ✅   |
| test_flip                  | Odwracanie planszy                                  | PASS ✅   |
| test_rotate                | Obracanie planszy                                   | PASS ✅   |
| test_rtrim                 | Przycinanie planszy z prawej strony                 | PASS ✅   |
| test_remove_filled_rows    | Usuwanie wypełnionych rzędów                        | PASS ✅   |
| test_simplify              | Uproszczenie planszy                                | PASS ✅   |
| test_get_empty_squares     | Pobieranie pustych kwadratów                        | PASS ✅   |
| test_get_set               | Pobieranie i ustawianie wartości komórek            | PASS ✅   |
| test_is_valid_cut_column   | Sprawdzanie czy kolumna może być cięta              | PASS ✅   |
| test_get_cuttable_columns  | Pobieranie kolumn, które można ciąć                 | PASS ✅   |
| test_cut_columns           | Cięcie kolumn                                       | PASS ✅   |
| test_get_sub_board         | Pobieranie podplanszy                               | PASS ✅   |
| test_get_poly              | Generowanie wielomianu na podstawie stanu planszy   | PASS ✅   |
| test_eq                    | Porównywanie plansz                                 | PASS ✅   |
| test_repr                  | Reprezentacja obiektu planszy                       | PASS ✅   |
| test_str                   | Reprezentacja planszy jako string                   | PASS ✅   |

### Klasa `Polynomial`

| Nazwa Testu                | Opis                                                  | Wynik    |
|----------------------------|-------------------------------------------------------|----------|
| test_init                  | Testy inicjalizacji wielomianu                        | PASS ✅   |
| test_add                   | Dodawanie wielomianów                                 | PASS ✅   |
| test_add_scalar            | Dodawanie skalaru do wielomianu                       | PASS ✅   |
| test_call                  | Wywołanie wielomianu jako funkcji                     | PASS ✅   |
| test_eq                    | Test równości wielomianów                             | PASS ✅   |
| test_eq_scalar             | Test równości wielomianu i skalaru                    | PASS ✅   |
| test_mul                   | Mnożenie wielomianów                                  | PASS ✅   |
| test_mul_scalar            | Mnożenie wielomianu przez skalar                      | PASS ✅   |
| test_neg                   | Negacja wielomianu                                    | PASS ✅   |
| test_pow                   | Test podnoszenia wielomianu do potęgi (niezaimplementowane) | PASS ✅   |
| test_radd                  | Prawostronne dodawanie                                | PASS ✅   |
| test_repr                  | Reprezentacja wielomianu                              | PASS ✅   |
| test_rmul                  | Prawostronne mnożenie                                 | PASS ✅   |
| test_rsub                  | Prawostronne odejmowanie                              | PASS ✅   |
| test_str                   | Reprezentacja wielomianu jako łańcuch znaków          | PASS ✅   |
| test_sub                   | Odejmowanie wielomianów                               | PASS ✅   |
| test_sub_scalar            | Odejmowanie skalaru od wielomianu                     | PASS ✅   |
| test_trim                  | Przycinanie zer na końcu wielomianu                   | PASS ✅   |

## Analiza i Dalsze Kierunki
- **Zgodność z Teorią Matematyczną**: Testy obu klas potwierdzają ich zgodność z zasadami wielomianu szachowego, co jest kluczowe dla wiarygodności projektu.
- **Możliwości Rozwoju**: Rozważenie implementacji dodatkowych funkcji i scenariuszy testowych, zwłaszcza dla klasy `Polynomial`, może wzbogacić funkcjonalność projektu.
- **Rekomendacje**: Zaleca się przeprowadzenie dodatkowych testów w bardziej złożonych scenariuszach, aby w pełni wykorzystać potencjał obu klas w kontekście matematycznym.

## Podsumowanie
Testy jednostkowe klas `Board` i `Polynomial` skutecznie potwierdziły ich poprawność i skuteczność w kontekście projektu RookPoly. Obie klasy spełniają matematyczne wymagania związane z wielomianem szachowym i stanowią solidną podstawę dla dalszych badań i rozwoju w dziedzinie matematyki dyskretnej. Wyniki testów dostarczają mocnych fundamentów do dalszej pracy nad projektem.
