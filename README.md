Skrypt "cutAndJoinIntoNewMovie.py" służy do automatycznego cięcia filmu na kawałki a następnie przyśpieszania wybranych fragmentów i łączenia później tego wszystkiego w gotowy film.
Skrypt "sortGOPROFilenamesInThisDir.py" służy do sortowania plików z kamery GOPRO.
Skrypt "joinMoviesInDir.sh" służy do łączenia wszystkich plików video danego formatu w jeden film.

Czyli najpierw sortujemy sobie pliki z kamery za pomocą "sortGOPROFilenamesInThisDir.py" (UWAGA: skrypt zmienia nazwy plików) i łączymy je w jeden film za pomocą "joinMoviesInDir.sh". Następnie powstały film oglądamy i zapisujemy sobie znaczniki czasu dla fragmentów, które nas interesują (początek i koniec danego urywka). Znaczniki następnie zapisujemy do pliku "czasy.dat". Gdy plik "czasy.dat" jest już gotowy to uruchamiamy skrypt "cutAndJoinIntoNewMovie.py" i po jego zakończeniu mamy gotowy film.

#----------------------FORMAT PLIKU czasy.dat----------------------#
#                                                                  #
#   W celu określenia przedziałów materiału video, które mają      #
#   zostać poddane obróbce należy podać zakresy czasu <od>-<do>    #
#   w fomacie HH:mm:ss-HH:mm:ss dla każdego kawałka filmu o        #
#   normalnej prędkości (np. 00:00:15-1:03:47) oraz w formacie     #
#   tHH:mm:ss-HH:mm:ss dla fragmentów filmu które mają być         #
#   przyśpieszone (np. t1:03:47-02:13:70). Kolejne zakresy czasów  #
#   wpisujemy jeden pod drugim. Ważne jest aby nie popełniać       #
#   błędów ponieważ program w tym momencie nie posiada żadnej      #
#   funkcji sprawdzania poprawności składni dla danych z pliku     #
#   więc po napotkaniu błędnego zapisu po prostu się wysypie.      #
#                                                                  #
#------------------------------------------------------------------#

