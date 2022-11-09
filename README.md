# quiz_game

![Screenshot 2022-11-09 113447](https://user-images.githubusercontent.com/113506949/200794226-2065f8ab-9b26-4745-89cf-1a8611d8a6ea.png)


Programoje naudojamos technologijos:
- Tkinter
- SQLAlchemy

Programa skirta viktorinos žaidimui su žaidėjų, bei žaidimo istorijos saugojimu, istorinių rezultatų paieška.

Paleidus programą sukuriamas pradinis langas su trimis mygtukais - <ins>Register</ins>, <ins>Top scores</ins>, <ins>Score history</ins>.
Taip pat kontekstinis meniu per kurį galima išeiti iš programos.

![image](https://user-images.githubusercontent.com/113506949/196032589-1134e6fb-d1e2-45a5-b9f3-d2e3a7f60cfd.png)

## 1) Register: 

Paspaudus <ins>Register</ins> mygtuką sunaikinami visi pradžioje sukurti elementai ir kviečiama <ins>Registration</ins> klasė, kuri sukuria
visus elementus naudojamus žaidėjo registracijai. Į datos lauką automatiškai įrašoma dabartinė data ir laikas.

![image](https://user-images.githubusercontent.com/113506949/196032753-eec32768-d342-4fdb-8f73-de4337ce3c59.png)

- Paspaudus <ins>Start Game</ins> mygtuką tikrinama ar įrašytas žaidėjo vardas bei pavardė. Jei ne metamas error, jei taip, sunaikinami visi registracijai
sukurti elementai ir kviečiama <ins>PlayGame</ins> klasė.

- Paspaudus <ins>Back to Main menu</ins> mygtuką sunaikinami visi registracijai sukurti elementai ir kviečiama <ins>MainWindow</ins> klasė, kuri
atstato pradinę programos būseną.

## 1a) Start Game:

Paspaudus <ins>Start Game</ins> mygtuką kviečiama <ins>PlayGame</ins> klasė, kuri sukuria visus žaidimui reikalingus elementus. Paima visus klausimus
bei atsakymus į juos ir išmaišo atsitiktinai neatskyrus klausimų nuo atsakymų ir sudeda į sąrašus. Tada išmaišo klausimo atsakymus dar kartą,
iteruoja klausimą bei atsakymus ir jį pateikia programoje.

![image](https://user-images.githubusercontent.com/113506949/196033215-64157b96-d96c-436d-90e8-2d3607f31113.png)

- Paspaudus <ins>Next</ins> mygtuką į duomenų bazę įrašomas žaidėjo atsakytas klausimas, taip pat kokius atsakymus jis pasirinko. Pasirinkti
atsakymai lyginami su teisingais atsakymais, apsakičiuojami taškai ir taip pat įrašomi į DB. Tada iteruojami klausimų bei atsakymų sąrašai,
paimamas sekantis elementas ir pateikiamas programoje. Iteratoriui ištuštėjus, sunaikinami visi žaidimui sukurti elementai ir kviečiama
<ins>FinalScore</ins> klasė.

- <ins>FinalScore</ins> ši klasė parodo galutinį žaidėjo rezultatą, lentelę kurioje parodo visus jam duotus klausimus ta tvarka kuria jie buvo pateikti, 
žaidėjo pasirinktus atsakymus į kiekvieną klausimą, taip pat teisingus atsakymus į tą klausimą.

  ![image](https://user-images.githubusercontent.com/113506949/196033525-e695094a-1c0e-4b2b-b0bf-e00ec3dce4a6.png)

- Paspaudus <ins>Back to Main menu</ins> mygtuką, sunaikinami visi <ins>FinalScore</ins> klasės sukurti elementai ir kviečiama <ins>MainWindow</ins>
klasė, kuri grąžina pradinę programos būseną.

## 2) Top Scores:

Paspaudus <ins>Top Scores</ins> mygtuką sunaikinami visi pradiniai programos elementai ir kviečiama <ins>TopScores</ins> klasė, kuri
sukuria antraštę, bei lentelę, kurioje atvaizduojami top10 daugiausiai taškų surinkusių žaidėjų su data, vardu, pavarde bei taškų skaičiumi.
Taip pat <ins>Back to Main menu</ins> mygtukas.

![image](https://user-images.githubusercontent.com/113506949/196033807-ebf9d823-f60e-4f06-a6bd-e372865e20b2.png)

- Paspaudus <ins>Back to Main menu</ins> mygtuką, sunaikinami visi <ins>TopScores</ins> klasės sukurti elementai ir kviečiama <ins>MainWindow</ins>
klasė, kuri grąžina pradinę programos būseną.

## 3) Score History:

Paspaudus <ins>Score History</ins> mygtuką, sunaikinami pradiniai programos elementai ir kviečiama <ins>FilteredSearch</ins> klasė, kuri sukuria
rezultatų filtravimui naudojamus elementus, su datų ruožais From - To combobox. Į To combobox surašoma dabartinė data, į From 2022-01-01. 
Combobox pasikeitimai pririšami prie funkcijos kuri atnaujiną sukurtą rezultatų lentelę ir ji yra automatiškai atnaujinama pakeitus bent vieną combobox.
Taip pat sukuriamas <ins>Back to Main menu</ins> mygtukas.

![image](https://user-images.githubusercontent.com/113506949/196033982-f69668e2-8b4d-4cdb-87f0-6800345a0562.png)

- Paspaudus <ins>Back to Main menu</ins> mygtuką, sunaikinami visi <ins>ScoreHistory</ins> klasės sukurti elementai ir kviečiama <ins>MainWindow</ins>
klasė, kuri grąžina pradinę programos būseną.
