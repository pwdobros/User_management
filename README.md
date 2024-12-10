# Dokumentacja programu do zarządzania użytkownikami

## Instalacja

Aby uruchomić program, wykonaj następujące kroki:

1. **Klonowanie repozytorium**: Sklonuj repozytorium z kodem na swój lokalny komputer.
   ```bash
   git clone <link_do_repozytorium>
   ```

2. **Zainstaluj wymagane biblioteki**: Upewnij się, że masz zainstalowanego Pythona. Następnie potrzebne biblioteki można zainstalować za pomocą pip.
   ```bash
   pip install -r requirements.txt
   ```

3. **Uruchom program**: Przejdź do katalogu, w którym znajduje się skrypt i uruchom go.
   ```bash
   python main.py
   ```

## Używanie programu

### Dodawanie użytkownika

Aby dodać nowego użytkownika:

1. Wywołaj funkcję `add_user(user_data)`.
2. Przekaż dane użytkownika w formacie słownika, zawierające następujące pola:
   - `"username"`: imię i nazwisko użytkownika.
   - `"nip"`: NIP użytkownika (9 cyfr).
   - `"pesel"`: PESEL użytkownika (11 cyfr).
   - `"regon"`: REGON użytkownika (9 lub 14 cyfr).
   - `"password"`: hasło użytkownika.
   
3. Program automatycznie nada użytkownikowi unikalny identyfikator.

### Edytowanie użytkownika

Edycja użytkownika nie została zaimplementowana w obecnej wersji programu. Można to dodać w przyszłych wersjach.

### Usuwanie użytkownika

Aby usunąć użytkownika:

1. Wywołaj funkcję `remove_user(user_id)`.
2. Przekaż identyfikator użytkownika, którego chcesz usunąć (zmiana statusu na "Inactive").

### Walidacja danych użytkownika

Program sprawdza poprawność danych użytkownika przed ich dodaniem. Oto zasady walidacji:

- **NIP**: Musi składać się z 10 cyfr. Walidacja polega na zastosowaniu wag i sprawdzeniu poprawności sumy kontrolnej.
- **PESEL**: Musi składać się z 11 cyfr. Walidacja również polega na zastosowaniu wag i sprawdzeniu poprawności sumy kontrolnej.
- **REGON**: Może mieć długość 9 lub 14 cyfr. Walidacja opiera się na zastosowaniu wag i sprawdzeniu sumy kontrolnej.

## Najlepsze praktyki dotyczące zarządzania danymi użytkowników

1. **Bezpieczeństwo danych**: Zawsze przechowuj dane w sposób bezpieczny. Używaj silnych metod kryptograficznych do przechowywania haseł (np. bcrypt).

2. **Minimalizacja danych**: Przechowuj jedynie dane osobowe, które są absolutnie niezbędne do działania aplikacji.

3. **Dostęp do danych**: Ogranicz dostęp do danych osobowych. Upewnij się, że tylko uprawnione osoby mają dostęp do danych użytkowników.

4. **Regularne aktualizacje**: Utrzymuj swój oprogramowanie i zależności w aktualnej wersji, aby uniknąć znanych luk bezpieczeństwa.

5. **Szkolenie użytkowników**: Edukuj użytkowników o zasadach bezpieczeństwa, aby zmniejszyć ryzyko kradzieży danych.

6. **Użyj szyfrowania**: Zastosuj szyfrowanie dla danych w czasie przechowywania oraz w czasie przesyłania.

## Licencja

Ten projekt jest udostępniony na licencji MIT. Szczegóły można znaleźć w pliku LICENSE.
